# Manifest to increate limit of files open for Nginx service

exec {'raise_limit':
  command => "/bin/sed -i 's/-n 15/-n 1024/' /etc/default/nginx/"
}

exec {'restart_nginx':
  command => '/usr/sbin/service nginx restart'
}
