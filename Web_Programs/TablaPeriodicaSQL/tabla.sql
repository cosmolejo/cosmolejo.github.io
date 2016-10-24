use Pensum;
 drop table if exists Materias;
 create table Materias (
	NombreMateria varchar(255),
	Cred. varchar(255),
	Area varchar(255),
	Cod. varchar(255),
	Habilitable(H)Validable(V)Clasificable(C) varchar(255),
	Correquisitos(CO)Prerrequisitos(PRE) varchar(255),
	Cons. varchar(255),
	primary key (Cod)
);
