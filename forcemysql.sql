CREATE TABLE REGISTER(
ENTNO INT AUTO_INCREMENT,
USERNAME VARCHAR(40) NOT NULL,
MOBILE INT,
ADDRESS VARCHAR(40),
PRIMARY KEY(ENTNO)
);
SELECT *
FROM register;
alter table  register
change ENTNO ID INT;

create table CHECKIN(
GENTNO INT auto_increment,
GNAME varchar(40),
GMOBILE int,
GADDRESS VARCHAR(40),
GDAYS int,
GROOMNO INT,
GPAY varchar(10),
primary key(GENTNO)
);
select *
FROM checkin;

