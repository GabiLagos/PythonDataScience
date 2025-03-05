import matplotlib.pyplot as plt
#vamos apedir el nombre del comercial y sus ventas por producto
# pedimos los datos al ususario con input()

productos=[]
ventas=[]
row=1
print("Nombre del Comercial")
comercial= input()
for row in range(5):
    print(f"Nombre del producto {row}")
    prod=input()
    print(f"Ventas del producto {row}")
    vent=int(input())
    row=row+1
    productos.append(prod)
    ventas.append(vent)
    
plt.pie(ventas,labels=productos)
plt.title(f"Gráfico de VentaProductos de {comercial}")
plt.legend()
plt.savefig("imagenes/piechart_productos.png")
plt.show()