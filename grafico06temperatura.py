import matplotlib.pyplot as plt
#vamos apedir la temperatura de cada dia de la semama
# pedimos los datos al ususario con input()

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado','Domingo']
temperatura=[]
row=1


for dia in semana:
    # Pedir al usuario que ingrese la temperatura
    print("Ingresa la temperatura para {semana[row]}: ")
    temp = int(input())
    # Agregar la temperatura a la lista
    temperatura.append(temp)
    row=row+1
    
plt.plot(semana,temperatura)
plt.title(f"Temperatura de la semama")
plt.savefig("imagenes/linea_temperatura.png")
plt.show()