# Finds out why Apache is returning a 500 error.

exec { '/var/www/html/wp-includes/class-wp-locale.phpp':
  cwd = > '/var/www/html/', 
  creates => '/wp-includes/class-wp-locale.php',
}