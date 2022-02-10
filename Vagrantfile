# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.box_check_update = false
  config.vm.synced_folder '.', '/vagrant'
  config.vm.provision "shell", inline: "apt-get update && apt-get install -y docker.io python3-pip && pip3 install molecule[docker] ansible ansible-lint pytest pytest-testinfra"
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
  end
end
