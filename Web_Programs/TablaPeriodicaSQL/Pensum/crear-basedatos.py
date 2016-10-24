import csv

csvfile=open("Pensum.csv","rU")
materias=csv.DictReader(csvfile,dialect="excel",delimiter=",")

i=0
fe=open("pensum.sql","w")
fe.write("use Pensum;\n")
for elemento in materias:
    if i==0:
        f=open("tabla.sql","w")
        f.write("use Pensum;\n drop table if exists Materias;\n create table Materias (\n")
        for key in elemento.keys():
            f.write("\t%s varchar(255),\n"%(key))
        f.write("\tprimary key (Cod)\n")
        f.write(");\n")
        f.close()

    campos=elemento.keys()

    campostxt="("
    valorestxt="("
    for campo in campos:
        campostxt+="%s,"%campo
        valor=elemento[campo].strip()
        valorestxt+="'%s',"%valor
    campostxt=campostxt.strip(",")+")"
    valorestxt=valorestxt.strip(",")+")"

    sql="insert into Materias %s values %s;"%(campostxt,valorestxt)
    fe.write("%s\n"%sql)

fe.close()
