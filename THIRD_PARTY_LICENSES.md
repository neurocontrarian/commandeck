# Third-Party Licenses — Commandeck

Commandeck includes or dynamically links the following third-party components.
Their licenses are listed below. **For the LGPL components, you may replace the
library with your own (possibly modified) version**; the corresponding source
code is available at the URLs given, and the libraries are shipped as separate
files inside the application directory so they can be relinked.

Commandeck itself: the free core is licensed under the **GNU AGPL-3.0**
(<https://github.com/neurocontrarian/commandeck>); the Pro build is proprietary
(see `LICENSE-PRO.md`).

---

## Desktop builds (Linux AppImage / macOS .dmg / Windows .exe)

### Used under the GNU LGPL (weak copyleft — replaceable)

| Component | License | Source code |
|-----------|---------|-------------|
| **Qt 6** (the GUI toolkit) | LGPL-3.0 | <https://www.qt.io/download-open-source> · <https://code.qt.io/> |
| **PySide6 / shiboken6** (Qt for Python) | LGPL-3.0 | <https://code.qt.io/cgit/pyside/pyside-setup.git/> |
| **Paramiko** (SSH — Pro builds only) | LGPL-2.1 | <https://github.com/paramiko/paramiko> |

> Only the **QtCore, QtGui, QtSvg and QtWidgets** modules are used. GPL-only Qt
> modules (e.g. Qt Charts, Qt Data Visualization) are **not** included. The Qt
> shared libraries ship as separate files in the app folder and may be replaced
> with a compatible build of your own.

### Used under permissive licenses (MIT / BSD / Apache-2.0)

| Component | License | Source code |
|-----------|---------|-------------|
| cryptography (Pro) | Apache-2.0 / BSD-3 | <https://github.com/pyca/cryptography> |
| bcrypt (Pro) | Apache-2.0 | <https://github.com/pyca/bcrypt> |
| PyNaCl (Pro) | Apache-2.0 | <https://github.com/pyca/pynacl> |
| cffi | MIT | <https://github.com/python-cffi/cffi> |
| pycparser | BSD-3 | <https://github.com/eliben/pycparser> |
| Fabric (Pro) | BSD-2 | <https://github.com/fabric/fabric> |
| Invoke (Pro) | BSD-2 | <https://github.com/pyinvoke/invoke> |
| keyring | MIT | <https://github.com/jaraco/keyring> |
| SecretStorage (Linux) | BSD-3 | <https://github.com/mitya57/secretstorage> |
| jeepney (Linux) | MIT | <https://gitlab.com/takluyver/jeepney> |
| tomli_w | MIT | <https://github.com/hukkin/tomli-w> |
| Bootstrap Icons (SVG assets) | MIT | <https://github.com/twbs/icons> |

### Build tooling (NOT distributed inside the application)

| Tool | License | Note |
|------|---------|------|
| PyInstaller | GPL-2.0 **with bootloader exception** | The exception explicitly permits proprietary frozen apps. |
| UPX | GPL + special exception | Permits compressing proprietary executables. |
| CairoSVG | LGPL-3.0 | Used **only at build time** to pre-render icon assets. Not shipped — runtime SVG rendering uses Qt's own QtSvg. |

---

## Mobile build (Android — in development)

| Component | License | Source code |
|-----------|---------|-------------|
| Toga / toga-android (BeeWare) | BSD-3 | <https://github.com/beeware/toga> |
| **Chaquopy** (Python-on-Android runtime) | **MIT** (open source since 12.0.1) | <https://github.com/chaquo/chaquopy> |
| Paramiko | LGPL-2.1 | <https://github.com/paramiko/paramiko> |
| cryptography / bcrypt / PyNaCl / cffi | Apache-2.0 / BSD / MIT | (see desktop table) |

---

*Generated 2026-06-02 from the project's declared dependencies and PyInstaller
specs. Regenerate (e.g. with `pip-licenses`) when dependencies change.*
