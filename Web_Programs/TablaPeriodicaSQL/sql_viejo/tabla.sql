use TablaPeriodica;
drop table if exists Elementos;
create table Elementos (
	 Boiling_Point varchar(255),
	 Lattice_Constant varchar(255),
	 Symbol varchar(255),
	Name varchar(255),
	 Thermal_Conductivity varchar(255),
	 Oxidation_States varchar(255),
	 Density varchar(255),
	 Atomic_Number varchar(255),
	 Pauling_Electronegativity varchar(255),
	 Heat_Evaporation varchar(255),
	 Specific_Heat varchar(255),
	 Atomic_Weight varchar(255),
	 Heat_Fusion varchar(255),
	 Ionic_Radius varchar(255),
	 Covalent_Radius varchar(255),
	 Electronic_Configuration varchar(255),
	 Lattice varchar(255),
	 First_Ionisation_Energy varchar(255),
	 Melting_Point varchar(255),
	 Atomic_Radius varchar(255),
	 Specific_Volume varchar(255),
	primary key (Symbol)
);
