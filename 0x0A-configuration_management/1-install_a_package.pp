# install package puppet
exec { 'apt-get update':
  command   => '/usr/bin/apt-get update'
}

package {'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
