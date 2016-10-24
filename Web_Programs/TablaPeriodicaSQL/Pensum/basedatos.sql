create database Pensum;
create user 'estudiante'@'localhost' identified by 'astronomia';
grant all privileges on Pensum.* to 'estudiante'@'localhost';
flush privileges;
