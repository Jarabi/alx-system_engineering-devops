# Manifest to increate limit of files open for Nginx service

exec {'/etc/default/nginx':
  command => 'sed -i "s/-n 15/-n unlimited/" /etc/default/nginx/',
  path    => '/bin:/usr/bin',
}

exec {'restart_nginx':
  command => 'sudo service nginx restart',
  path    => '/bin:/usr/bin',
}
