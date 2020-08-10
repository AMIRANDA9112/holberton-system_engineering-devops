# kill process puppet
$paths = ['/usr/bin']

exec { 'killmenow':
  path    => $paths,
  command => 'pkill -f killmenow',
}
