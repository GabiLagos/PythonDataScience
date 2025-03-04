import pandas as pd

print("Primer ejemplo DataFrame")

#creamos un diccionario con elemento que se llama series, es un diccionario con valores correspondientes entre ellos (aunque podrian no serlo)
datos= {'nombres':['Lucia', 'Andrea', 'Alex', "Antonia"] , 'edad':[22,17,48,70] , 'ciudad':["Segovia", 'Parla', 'Madrid', "Toledo"]}

#almacenamos las datos en un dataframe con la libreria de pandas (pd)
df =pd.DataFrame(datos)
print("Listado de todos los datos")
print(df)
print("----------------------------")

#podemos filtrar los datos de un dataframe con la siguente sintaxis: df[df[columna]== valor]. por ejemple
df_filtrado=df[df['edad']>30]
print("Datos filtrados")
print (df_filtrado)
print("----------------------------")
#tambien se puede ordenar por una o varias columnas: df.dort:values(columna)
df_sorted= df.sort_values('edad')
print("Datos Ordenados")
print(df_sorted)
print("----------------------------")