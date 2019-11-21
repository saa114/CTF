service nginx start
service php7.0-fpm start
service mysql start
mysql -u root -e 'source  /home/sqli/mysql-alldbs.sql'
mysql -u root -e 'flush privileges'

#sudo -u ctfuser php /home/php/datai/index.php
sudo -u ctfuser python /home/sqli/question.py
