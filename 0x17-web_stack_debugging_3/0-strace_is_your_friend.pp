# Fix apache 500 error

$file        = '/var/www/html/wp-settings.php',
$pattern     = '.phpp',
$replacement = '.php'

exec {'fix_apache':
  command => "/bin/sed -i \"s/${pattern}/${replacement}/\" ${file}",
  path    => '/bin:/usr/bin',
}