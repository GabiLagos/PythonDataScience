import pandas as pd
print("Lectura de CSV")
#almacenamos los datos del csv dentro de un datafra,e
df =  pd.read_csv('DATA/datos.csv',delimiter= ';') #hay que declarar el delimitador cuando NO es una como(,)
print("Listado de todo los datos")
print(df)
print("-------------------------------------")

#imprimir las 1ras 5 filas

print("Listado de las 1ras 5 filas")
print(df.head())
print("-------------------------------------")

#ordernar por edad
df_sorted= df.sort_values('edad')
print("Listado ordenado por edad")
print(df)
print("-------------------------------------")

#media de edad
media_edad= df['edad'].mean()
print("Media de  edad")
print(media_edad)
print("-------------------------------------")


#agrupar ppor columnas y recuperar datos
df_grupo= df.groupby( 'genero').size()
print("Agrupaciones")
print(df_grupo)
print("-------------------------------------")
