# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

VAGRANTFILE_API_VERSION = "2"

def setup_virtualbox_provider(config, num_cpus, ram_mb)
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    vb.gui = true unless ENV["NO_GUI"]

    vb.customize ["modifyvm", :id, "--memory", ram_mb]
    vb.cpus = num_cpus
  end
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  num_cpus = (ENV["VAGRANT_NUM_CPUS"] || "2").to_i
  ram_mb = ENV["VAGRANT_RAM"] || "4096"

  setup_virtualbox_provider(config, num_cpus, ram_mb)

end
