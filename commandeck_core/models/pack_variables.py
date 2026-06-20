"""Runtime command variables — `{{key}}` placeholders prompted at click time.

A button command may contain `{{container}}`, `{{service}}`, … ; when it does, the UI
asks for the value(s) just before running, substitutes them, and runs the resolved
command. Nothing is stored (runtime scope) — the value lives only for that run.

`STANDARD_VARIABLES` is a curated, **growing** dictionary of the most common variables,
so pack authors reuse the same keys and users get consistent prompts. An unknown key
still works — it falls back to a plain text prompt built from the key name — so the
dictionary can grow without breaking older packs.

Pure core (zero UI deps). Labels/prompts are English source strings; the UI wraps them
with `_()` at render time (so translation happens after the language is set, not at import).
"""
from __future__ import annotations

import re

# key → {label, prompt, type}. type: "text" | "number".
STANDARD_VARIABLES: dict[str, dict] = {
    "container": {"label": "Container", "prompt": "Docker container name", "type": "text"},
    "service":   {"label": "Service", "prompt": "systemd service name", "type": "text"},
    "path":      {"label": "Path", "prompt": "File or directory path", "type": "text"},
    "host":      {"label": "Host", "prompt": "Hostname or IP address", "type": "text"},
    "port":      {"label": "Port", "prompt": "Port number", "type": "number"},
    "branch":    {"label": "Branch", "prompt": "Git branch name", "type": "text"},
    "package":   {"label": "Package", "prompt": "Package name", "type": "text"},
    "user":      {"label": "User", "prompt": "User name", "type": "text"},
    "pid":       {"label": "PID", "prompt": "Process ID", "type": "number"},
    "lines":     {"label": "Lines", "prompt": "Number of lines", "type": "number"},
    "player":    {"label": "Player", "prompt": "Player name", "type": "text"},
    "message":   {"label": "Message", "prompt": "Message text", "type": "text"},
}

_VAR_RE = re.compile(r"\{\{\s*(\w+)\s*\}\}")


def find_variables(command: str) -> list[str]:
    """Variable keys used in ``command`` (e.g. ['container']), in first-seen order,
    de-duplicated. Empty if the command has no `{{ }}` placeholders."""
    seen: list[str] = []
    for m in _VAR_RE.finditer(command or ""):
        key = m.group(1)
        if key not in seen:
            seen.append(key)
    return seen


def spec_for(key: str) -> dict:
    """The spec for ``key`` — a standard one, or a generic text prompt for an unknown
    key (humanised from the key name), so the dictionary can grow without breaking packs."""
    if key in STANDARD_VARIABLES:
        return STANDARD_VARIABLES[key]
    label = key.replace("_", " ").replace("-", " ").strip().capitalize() or key
    return {"label": label, "prompt": label, "type": "text"}


def all_keys(saved: dict | None = None) -> list[str]:
    """Sorted union of the standard variable keys and any keys with saved values."""
    return sorted(set(STANDARD_VARIABLES) | set(saved or {}))


def standard_keys() -> list[str]:
    """The **authorized** variable keys a user may pick in the value-management and
    insert UIs — only the curated standard set, so users can't create unauthorized
    variables. (Unknown keys inside a *pack*'s command still resolve at run time via
    ``spec_for``; this only constrains what the UI lets a user add.)"""
    return sorted(STANDARD_VARIABLES)


def substitute(command: str, values: dict[str, str]) -> str:
    """Replace each `{{key}}` in ``command`` with ``values[key]`` (missing → empty)."""
    return _VAR_RE.sub(lambda m: str(values.get(m.group(1), "")), command or "")


def resolve_command(button, values: dict[str, str]):
    """Return a shallow copy of ``button`` with its command's `{{variables}}` filled in
    (runtime resolution shared by the desktop + mobile run paths). Original untouched."""
    import copy
    resolved = copy.copy(button)
    resolved.command = substitute(button.command, values)
    return resolved
