import matplotlib.pyplot as plt
#la mayoría de los gráficos suelen tener ejes de coordenadas para representar sus datos (x,y)
x=['Real Betis', 'Atlético de Madrid', 'Barcelona F.C.', 'Real Madrid'] #equipos
y=[5,10,15,20] #valor de merado

#creamos el gráfico mediante plt y con un método iremos indicando el tipo de gráfico que queremos
#BARRAS
plt.bar(x,y)
plt.title("Gráfico de Barras")
plt.xlabel("Equipos")
plt.ylabel(("Valor de Mercado"))


#podemos almacenar el gráfico en una imágen
plt.savefig("imagenes/barras.png")
plt.show()





