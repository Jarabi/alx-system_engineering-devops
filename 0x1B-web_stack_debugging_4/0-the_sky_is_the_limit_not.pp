# Manifest to increate limit of files open for Nginx service

# Raise limit for number of files nginx can open
exec {'raise-nginx-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx/',
  path    => '/usr/local/bin:/bin/'
}

# Set number of nginx file descriptors
exec { 'set-file-descriptors':
  command => "sed -i '/events {/i worker_rlimit_nofile 100000;\n' /etc/nginx/nginx.conf",
  path    => '/bin:/usr/bin'
}

# Set worker connections
exec { 'set-worker-connections':
  command => "sed -i 's/worker-connections [0-9]\\+/worker_connections 4000/' /etc/nginx/nginx.conf",
  path    => '/bin:/usr/bin'
}

# Restart nginx
exec {'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
