# Manifest to raise user limit in the OS configuration

exec {'raise_user_limit':
  command => "sed -i -E 's/nofile [0-9]+/nofile 1200000/g' /etc/security/limits.conf",
  path    => '/bin:/usr/bin',
}
