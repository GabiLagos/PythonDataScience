import oracledb
import matplotlib.pyplot as plt

print ("Graficos con BBDD")
oficios=[]
media_salarios=[]
connection=connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')  
sql=("select oficio, avg(salario)as Media_Salario from emp group by oficio")
cursor=connection.cursor()
cursor.execute(sql)
for row in cursor:
    oficios.append(row[0])
    media_salarios.append(row[1])
cursor.close()
connection.close()

plt.pie (media_salarios, labels=oficios)
plt.title(f"MEDIA SALARIAL")
plt.savefig("imagenes/pie_mediasalarial.png")
plt.show()


