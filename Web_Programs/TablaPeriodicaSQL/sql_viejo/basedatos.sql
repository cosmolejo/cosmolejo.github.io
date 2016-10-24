create database TablaPeriodica;
create user 'tablaperiodica'@'localhost' identified by 'mendelev';
grant all privileges on TablaPeriodica.* to 'tablaperiodica'@'localhost';
flush privileges;
