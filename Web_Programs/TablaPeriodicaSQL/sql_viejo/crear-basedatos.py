import csv

csvfile=open("ElementosQuimicos.txt","rU")
elementos=csv.DictReader(csvfile,dialect="excel",delimiter=",")

i=0
fe=open("elementos.sql","w")
fe.write("use TablaPeriodica;\n")
for elemento in elementos:
    if i==0:
        f=open("tabla.sql","w")
        f.write("use TablaPeriodica;\ndrop table if exists Elementos;\ncreate table Elementos (\n")
        for key in elemento.keys():
            f.write("\t%s varchar(255),\n"%(key))
        f.write("\tprimary key (Symbol)\n")
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

    sql="insert into Elementos %s values %s;"%(campostxt,valorestxt)
    fe.write("%s\n"%sql)

fe.close()
