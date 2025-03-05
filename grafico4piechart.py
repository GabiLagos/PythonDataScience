import matplotlib.pyplot as plt
etiquetas=['Real Betis', 'Atlético de Madrid', 'Barcelona F.C.', 'Real Madrid']
valores=[5,10,15,20]

plt.pie(valores,labels=etiquetas)

plt.title("Gráfico de Dispersión")
plt.legend()
plt.savefig("imagenes/piechart.png")
plt.show()