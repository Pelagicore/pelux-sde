#!/usr/bin/env python3
#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

"""
This script is used to configure qt-creator with a PELUX-SDK.

It is assumed that the environment-setup script for the SDK has
been sourced before this script is executed.
"""


import os
import shutil
import time
import sys

class CommandException(Exception):
    pass


class QtCreatorBootstrapper(object):

    def __init__(self, sdktool_path):
        self.rollback_stack = []

        epoch_time = int(time.time())
        self.name = "PELUX-SDK-{}".format(epoch_time)

        self.cxx_toolchain_id = "ProjectExplorer.ToolChain.Gcc:" + self.name + "CXX"
        self.cc_toolchain_id  = "ProjectExplorer.ToolChain.Gcc:" + self.name + "CC"
        self.device_id        = self.name + "_device"
        self.cmake_id         = self.name + "_cmake"
        self.qtversion_id     = self.name + "_qt"
        self.kit_id           = self.name + "_kit"

        arch_env_var = os.environ["ARCH"]
        if "arm" in arch_env_var:
            self.architecture = "arm"
            self.bits = "64bit" if "64" in arch_env_var else "32bit"
        elif "x86" in arch_env_var:
            self.architecture = "x86"
            self.bits = "64bit" if "64" in arch_env_var else "32bit"
        else:
            self.architecture = "unknown"
            self.bits = "unknown"

        self.sdktool = sdktool_path
        assert shutil.which(self.sdktool) is not None

    def __exec_cmd(self, cmd_to_exec):
        print("Executing command: {}".format(cmd_to_exec))
        complete_command = "{} {}".format(self.sdktool, cmd_to_exec)
        if os.system(complete_command) != 0:
            raise CommandException("Failed to execute {}".format(complete_command))

    def __add_rollback_cmd(self, rollback_cmd):
        self.rollback_stack.append(rollback_cmd)

    def add_cxx_toolchain(self):
        self.__add_toolchain(id=self.cxx_toolchain_id, compiler_env_var="CXX", lang="Cxx")

    def add_cc_toolchain(self):
        self.__add_toolchain(id=self.cc_toolchain_id, compiler_env_var="CC", lang="C")

    def __add_toolchain(self, id, compiler_env_var, lang):
        abi = "{}-linux-generic-elf-{}".format(self.architecture, self.bits)
        compiler_binary_name = os.environ[(str(compiler_env_var))].split()[0]
        compiler_path = shutil.which(compiler_binary_name)
        self.__exec_cmd("addTC"
                        + " --name " + self.name + "_" + compiler_env_var
                        + " --language " + lang
                        + " --id " + id
                        + " --abi " + abi
                        + " --path " + compiler_path
                        )
        self.__add_rollback_cmd("rmTC --id " + id)

    def add_cmake(self):
        cmake_path = shutil.which("cmake")
        self.__exec_cmd("addCMake"
                        + " --name " + self.name
                        + " --id " + self.cmake_id
                        + " --path " + cmake_path
                        )
        self.__add_rollback_cmd("rmCMake --id " + self.cmake_id)

    def add_qt_version(self):
        qmake = shutil.which("qmake")
        self.__exec_cmd("addQt"
                        + " --name " + self.name
                        + " --id " + self.qtversion_id
                        + " --type RemoteLinux.EmbeddedLinuxQt"
                        + " --qmake " + qmake
                        )
        self.__add_rollback_cmd("rmQt --id " + self.qtversion_id)

    def add_kit(self, use_qt=False):
        qt_params = ""
        if use_qt:
            qt_params += " --qt " + self.qtversion_id + " --mkspec \"" + os.environ["QMAKESPEC"] + "\""

        self.__exec_cmd("addKit"
                        + " --name " + self.name
                        + " --id " + self.kit_id
                        + " --debuggerengine 1"
                        + " --debugger " + shutil.which(os.environ["GDB"])
                        + " --devicetype GenericLinuxOsType"
                        + " --sysroot " + os.environ["SDKTARGETSYSROOT"]
                        + " --Cxxtoolchain " + self.cxx_toolchain_id
                        + " --Ctoolchain " + self.cc_toolchain_id
                        + " --cmake " + self.cmake_id
                        + qt_params
                        + self.generate_env_arguments()
                        )
        self.__add_rollback_cmd("rmKit --id " + self.kit_id)

    def generate_env_arguments(self):
        env_args = ""
        for key, value in os.environ.items():
            env_args += " --env \"{}={}\"".format(key, value.strip())
        return env_args

    def rollback(self):
        for _ in self.rollback_stack:
            rollback_cmd = self.rollback_stack.pop()
            self.__exec_cmd(rollback_cmd)

        self.rollback_stack = []

def qt_installed():
    return shutil.which("qmake") is not None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass path to the sdktool")
        quit()

    bootstrapper = QtCreatorBootstrapper(sys.argv[1])
    try:
        bootstrapper.add_cxx_toolchain()
        bootstrapper.add_cc_toolchain()
        bootstrapper.add_cmake()
        if qt_installed():
            bootstrapper.add_qt_version()
        bootstrapper.add_kit(qt_installed())
    except CommandException as e:
        bootstrapper.rollback()
        raise e

    print("QtCreator Successfully configured to use the PELUX-SDK")
