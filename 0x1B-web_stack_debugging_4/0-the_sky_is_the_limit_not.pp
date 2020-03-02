# Fixing request
exec { 'Fixes':
  command => '/bin/echo ULIMIT="-n 32768" | sudo tee /etc/default/nginx',
}

exec { 'Restart' :
  command => '/usr/bin/service nginx restart'
}