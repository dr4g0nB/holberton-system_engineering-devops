# Fixing request
exec { 'Fixes request':
  command => '/bin/echo ULIMIT="-n 32768" | sudo tee /etc/default/nginx',
}

exec { 'Restart nginx':
  command => '/usr/bin/service nginx restart'
}