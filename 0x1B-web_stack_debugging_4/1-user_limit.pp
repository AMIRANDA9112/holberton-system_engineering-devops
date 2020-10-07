# Chanfe the error meessage
file { 'login':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#This file has been delete'
}
