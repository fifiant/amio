notify { 'Preparing box for Docker container': }

exec { "apt-get update":
  command => "/usr/bin/apt-get update",
  before => Exec["apt-get updates extras"]
}

exec { "apt-get updates extras":
  command => "/usr/bin/apt-get install linux-image-extra-`uname -r` -y",
  before => Exec["apt-get install wget"]
}

exec { "apt-get install wget":
  command => "/usr/bin/apt-get install wget -y",
  before => Exec["wget add docker key"]
}

exec { "wget add docker key":
  command => "/bin/sh -c \"/usr/bin/wget -qO- https://get.docker.io/gpg | apt-key add -\"",
  before => Exec["sh add docker repo"]
}

exec { "sh add docker repo":
  command => "/bin/sh -c \"echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list\"",
  before => Exec["apt-get update after updated list"]
}

exec { "apt-get update after updated list":
  command => "/usr/bin/apt-get update",
  before => Exec["apt-get install lxc-docker"]
}

exec { "apt-get install lxc-docker":
  command => "/usr/bin/apt-get install lxc-docker-0.8.1 -y",
  before => Exec["apt-get install git"]
}

exec { "apt-get install git":
  command => "/usr/bin/apt-get install git -y"
}
