/usr/bin/mysql -uroot -p1234 -e "grant all privileges on *.* to 'root'@'%';"
/usr/bin/mysql -uroot -p1234 -e "create database sample DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
