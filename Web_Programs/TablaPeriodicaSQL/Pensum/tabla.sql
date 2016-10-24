use Pensum;
 drop table if exists Materias;
 create table Materias (
	NombreMateria varchar(255),
	Cons varchar(255),
	HabValClas varchar(255),
	Area varchar(255),
	Cred varchar(255),
	Cod varchar(255),
	COPRE varchar(255),
	primary key (Cod)
);
