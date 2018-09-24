#!/usr/bin/env python3
#
# Copyright (C) 2017 Pelagicore AB
# Copyright (C) 2018 Luxoft Sweden AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

import pytest
import os
import subprocess
import sys

# Constants

SCRIPTS_PATH = os.path.dirname(__file__) + "/scripts/"

# Helper functions

def scripts_for(path):
    return [f for f in os.listdir(SCRIPTS_PATH + path) if f.endswith(".py")]


def scripts_path_on_vm(scripts_dirname):
    return "/vagrant/test/scripts/" + scripts_dirname + "/"


def run_test_script_inside_vm(script_type, script_name, script_args=""):
    command_to_run_in_vm = "python3 {}/{} {}".format(
        scripts_path_on_vm(script_type),
        script_name,
        script_args)

    args = ["vagrant", "ssh", "-c", command_to_run_in_vm]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    script_exit_code = process.wait()

    if script_exit_code != 0:
        print(pipe_to_str(process.stdout))
        print(pipe_to_str(process.stderr), file=sys.stderr)

    assert script_exit_code == 0


def pipe_to_str(pipe):
    return "\n".join([ x.decode() for x in pipe.readlines() ])


# Fixtures common code

def setup_sdk_stub_in_vm(stub_script_name):
    try:
        assert os.system("SDK_FILE_NAME=\"test/stubs/{}\" NO_GUI=1 vagrant up".format(stub_script_name)) == 0
        yield
    finally:
        os.system("vagrant destroy -f")

# Fixtures

@pytest.fixture(scope="class")
def vagrant():
    setup_sdk_stub_in_vm("full_sdk.sh")

@pytest.fixture(scope="class")
def vagrant_no_qt():
    setup_sdk_stub_in_vm("sans_qmake_sdk.sh")


# Tests

@pytest.mark.usefixtures("vagrant")
class Test(object):

    @pytest.mark.parametrize("script", scripts_for("base"))
    def test_script_inside_vm(self, script):
        run_test_script_inside_vm("base", script)

    @pytest.mark.parametrize("script", scripts_for("qt"))
    def test_script_inside_vm_qt(self, script):
        run_test_script_inside_vm("qt", script)


@pytest.mark.usefixtures("vagrant_no_qt")
class TestNoQt(object):

    @pytest.mark.parametrize("script", scripts_for("base"))
    def test_script_inside_vm(self, script):
        run_test_script_inside_vm("base", script)
