# Manifest to increate limit of files open for Nginx service

exec {'raise_limit':
  command => "sed -i 's/-n 15/-n 4096/' /etc/default/nginx/",
  path    => '/bin:/usr/bin'
} ->

exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
