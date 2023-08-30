#  Puppet script to install and configure an Nginx server
#  Update package repository
exec { 'package_update':
command => '/usr/bin/apt update'
}

# Install nginx
package { 'nginx':
ensure  => installed,
require => Exec['package_update']
}

# Configure homepage
file { '/var/www/html/index.html':
content => 'Hello World!',
require => Package['nginx']
}

# Configure redirect
$rdr_text = "\\\n\\n\tlocation /redirect_me {\\n\t\treturn 301 http://theuselessweb.com;\\n\t}"

exec { 'redirect_me':
command => "/usr/bin/sed -i \"/server_name _;/a\\${rdr_text}\" /etc/nginx/sites-available/default",
require => Package['nginx']
}

# Restart nginx service
service { 'nginx':
ensure  => running,
enable  => true,
require => Package['nginx'],
}
