PELUX-SDE
=========

Software Development Environment for the PELUX distro.

Maintained at [https://github.com/Pelagicore/PELUX-SDE](https://github.com/Pelagicore/PELUX-SDE)

License: MPLv2.0

Build
-----
Dependencies:
* Vagrant
* VirtualBox

```bash
vagrant up
```

### Used environment variables:
Following is a list of environment variables used by vagrant when provisioning the SDE.

* SDK_FILE_NAME: Name of the self-exctracting SDK package to install into the SDE. Can include wildcards.
Defaults to `oecore*toolchain*sh`.
* NO_GUI: Will create a headless SDE when set.


Testing
-------
Dependencies:
* pytest

```bash
test/run-tests.sh
```
