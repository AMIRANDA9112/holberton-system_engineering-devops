# creating a custom HTTP header response, but with Puppet.
# -The name  must be X-Served-By
# -The value  must be the hostname
# server Nginx is running on
exec {'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line {'response_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['response_header'],
}
