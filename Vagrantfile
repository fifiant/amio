# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "DebianSqueeze64"
  config.vm.box_url = "http://dl.dropbox.com/u/937870/VMs/squeeze64.box"
  config.vm.provision :shell, :path => "authorized_key.sh"
  config.vm.host_name = "redmine.example.com"
  config.vm.network :hostonly, "192.168.33.10", :mac => "0800254a508c"
end