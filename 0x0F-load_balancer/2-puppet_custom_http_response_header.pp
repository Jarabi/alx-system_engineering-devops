# Manifest to automate the task of creating a custom HTTP header response

# Update package repositories
exec { 'package_update':
  command => '/usr/bin.apt update'
}

# Install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['package_update']
}

$new_header = "\\\n\n\tadd_header X-Served-By ${hostname};\\n"

# Add custom header
exec { 'add_header':
  command => "/usr/bin/sed -1 \"/http {/a\\${new_header}\" /etc/nginx/nginx.conf",
  require => Package['nginx']
}

# Start nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
