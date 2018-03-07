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

def install_with_apt(config, program)
  config.vm.provision "shell" do |s|
    s.inline = "apt-get update -y && apt-get install " + program + " -y"
  end
end

def install_sdk(config)

  sdk_file_name = (ENV["SDK_FILE_NAME"] || "oecore*toolchain*sh")
  config.vm.provision "sdk", type: "shell",
                      args: [sdk_file_name],
                      path: "sde-cookbook/sdk/install_sdk.sh"
end

def setup_virtualbox_provider(config, num_cpus, ram_mb)
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    vb.gui = true unless ENV["NO_GUI"]
    vb.name = "PELUX-SDE"

    vb.customize ["modifyvm", :id, "--memory", ram_mb]
    vb.cpus = num_cpus
  end
end

def start_desktop_environment(config)
  config.vm.provision "shell" do |s|
    s.inline = "systemctl start gdm3"
  end
end

def install_qtcreator(config, qtcreator_install_dir)
  install_with_apt(config, "wget")
  config.vm.provision "shell", args: [qtcreator_install_dir], path: "sde-cookbook/qtcreator/install_qtcreator.sh"
end

def add_template_service_wizard(config, qtcreator_install_dir)
  install_with_apt(config, "git")
  config.vm.provision "shell", args: [qtcreator_install_dir], path: "sde-cookbook/qtcreator/add-template-service-wizard.sh"
end

def configure_qtcreator_to_use_sdk(config, qtcreator_install_dir)
  config.vm.provision "shell", args: [qtcreator_install_dir], :inline => <<-SHELL
      QT_CREATOR_INSTALL_DIR=$1

      source /opt/pelux_sdk/environment-setup*
      /vagrant/sde-cookbook/qtcreator/configure-qtcreator.py "$QT_CREATOR_INSTALL_DIR/libexec/qtcreator/sdktool"
  SHELL
end

def install_dlt_viewer(config, num_cpus)
  install_with_apt(config, "git")
  config.vm.provision "shell", args: [num_cpus], path: "sde-cookbook/dlt-viewer/install_dlt-viewer.sh"
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  num_cpus = (ENV["VAGRANT_NUM_CPUS"] || "2").to_i
  ram_mb = ENV["VAGRANT_RAM"] || "4096"

  setup_virtualbox_provider(config, num_cpus, ram_mb)
  install_with_apt(config, "gnome-shell")
  install_with_apt(config, "gnome-terminal")
  install_sdk(config)

  qtcreator_install_dir = "/opt/qtcreator"
  install_qtcreator(config, qtcreator_install_dir)
  configure_qtcreator_to_use_sdk(config, qtcreator_install_dir)
  add_template_service_wizard(config, qtcreator_install_dir)

  install_with_apt(config, "g++")
  install_with_apt(config, "qt5-default")
  install_with_apt(config, "qt5-qmake")
  install_dlt_viewer(config, num_cpus)

  start_desktop_environment(config)

end
