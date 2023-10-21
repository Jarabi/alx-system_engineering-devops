# Manifest to increate limit of files open for Nginx service

exec {'raise-nginx-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx/',
  path    => '/usr/local/bin:/bin/'
}

exec {'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
