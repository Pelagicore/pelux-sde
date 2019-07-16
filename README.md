PELUX-SDE
=========

Software Development Environment for the PELUX distro.

Maintained at https://github.com/Pelagicore/PELUX-SDE

License: MPLv2.0

Build
-----
Dependencies:
* Vagrant
* VirtualBox
* Self-extracting SDK package to install into the SDE. See, [Building the SDK installer](http://pelux.io/software-factory/master/swf-blueprint/docs/articles/baseplatform/creating-sdk.html#building-the-sdk).

For building the SDK installer, fetch the PELUX sources as describe in [Prerequisites for building a PELUX image](http://pelux.io/software-factory/master/swf-blueprint/docs/articles/baseplatform/prerequisites.html).

After building SDK installer, copy the SDK installer into PELUX-SDE repository's root directory and run,

```bash
SDK_FILE_NAME=<SDK installer> vagrant up
```

### Used environment variables:
Following is a list of environment variables used by vagrant when provisioning the SDE.

* SDK_FILE_NAME: Name of the self-exctracting SDK package to install into the SDE. Can include wildcards.
Defaults to `oecore*toolchain*sh`. Note that this has to be an SDK with Qt on
it.
* NO_GUI: Will create a headless SDE when set.


Testing
-------
Dependencies:
* pytest-3

Note: In order to do clean tests, this script will tear down and destroy the VM if it is already created
```bash
test/run-tests.sh
```

Developing features
-------------------
Since the SDK takes a long time to download and a long time to extract the tests
use a stubbed version of the SDK. The stubbed version sets mock values for
everything that is needed during the setup but nothing is actually installed.
For instance is cmake setup by the stubbed SDK as a symlink to /bin/true.

Keep in mind that the stubbed SDK is intended to be minimal. Meaning it will not
set all environment variables and provide fake installations of all tools
installed by a real SDK. Therefore when developing new features for the SDE, it
is likely necessary to extend the stubbed SDK with more environment variables or
stubbed instances of tools.
