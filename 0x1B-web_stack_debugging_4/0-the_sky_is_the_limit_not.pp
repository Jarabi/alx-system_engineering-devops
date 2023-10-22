# Manifest to increate limit of files open for Nginx service

# Make sure nginx is installed
package { 'nginx':
  ensure => installed,
} ->

# Raise limit for number of files nginx can open
exec { 'raise-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',
  require => Package['nginx'],
} ->

# Restart nginx
exec { 'restart-nginx':
  command     => 'nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
  subscribe   => Exec['raise-ulimit'],
}

