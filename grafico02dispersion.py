import matplotlib.pyplot as plt
x=['Real Betis', 'Atlético de Madrid', 'Barcelona F.C.', 'Real Madrid']     #equipos
y=[5,10,15,20]                                                              #valor de merado

plt.scatter(x,y)
plt.title("Gráfico de Dispersión")
plt.xlabel("Equipos")
plt.ylabel(("Valor de Mercado"))


#podemos almacenar el gráfico en una imágen
plt.savefig("imagenes/puntos.png")
plt.show()