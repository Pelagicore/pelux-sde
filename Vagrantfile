# -*- mode: ruby -*-
# vi: set ft=ruby :

# Copyright (C) 2017 Pelagicore AB
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