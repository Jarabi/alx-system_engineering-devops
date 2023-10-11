# Fix apache 500 error

exec {'fix_apache_500':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
}