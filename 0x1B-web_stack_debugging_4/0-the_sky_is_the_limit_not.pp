# Manifest to increate limit of files open for Nginx service

exec {'raise_limit':
  command => "sed -i 's/15/4096/' /etc/default/nginx/",
  path    => '/bin:/usr/bin',
}

exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/bin:/usr/bin',
}
