# Manifest to increate limit of files open for Nginx service

exec {'raise_limit':
  command => "/bin/sed -i 's/15/4096/' /etc/default/nginx/"
}

exec {'restart_nginx':
  command => '/usr/sbin/service nginx restart'
}
