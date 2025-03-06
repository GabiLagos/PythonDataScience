import oracledb
import matplotlib.pyplot as plt

print ("Graficos con DOCTORES-HOSPITAL")
hospital=[]
doctores=[]
connection=connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')  
sql=("""
select h.nombre, count(d.doctor_no) from doctor d 
join hospital h on h.hospital_cod= d.hospital_cod
group by h.nombre
""")
cursor=connection.cursor()
cursor.execute(sql)
for row in cursor:
    hospital.append(row[0])
    doctores.append(row[1])
cursor.close()
connection.close()

#plt.pie (doctores, labels=hospital)
plt.pie(doctores, labels=hospital, autopct='%1.1f%%', startangle=140,)
plt.title(f"HOSPITAL-DOCTORES")
plt.savefig("imagenes/pie_hospitaldoctores.png")
plt.show()
