# Copyright (C) 2016-2017 Pelagicore AB
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR
# BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.
#
# For further information see LICENSE

import pytest
import os

@pytest.fixture(scope="class")
def vagrant():
    os.system("NO_GUI=1 vagrant up")
    yield
    os.system("vagrant destroy -f")

@pytest.mark.usefixtures("vagrant")
class Test(object):

    def test_is_a_sane_ubuntu_system(self):
        self.__run_test_script_inside_vm("check_is_ubuntu.py")

    PATH_ON_VM_TO_TEST_SCRIPTS = "/vagrant/test/scripts"
    def __run_test_script_inside_vm(self, script_name, script_args=""):
        script_exec_result = os.system("vagrant ssh -c \"python3 {}/{} {}\"".format(self.PATH_ON_VM_TO_TEST_SCRIPTS,
                                                                                    script_name,
                                                                                    script_args))
        assert script_exec_result == 0

