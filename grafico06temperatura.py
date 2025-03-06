import matplotlib.pyplot as plt
# vamos apedir la temperatura de cada dia de la semama
# pedimos los datos de temperatura al ususario con input()

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado','Domingo']
temperatura=[]

for dia in semana:
    # Pedir al usuario que ingrese la temperatura
    print(f"Ingresa la temperatura para el {dia}")
    temp = int(input())
    temperatura.append(temp) # Agrega la temperatura a la lista
    
plt.plot(semana,temperatura, label="Semana1")
# Podemos incluir mas datos dentro del gráfico lineal siempre que demos un label a cada plot
temperatura2=[5,6,10,12,8,6,8]
plt.plot(semana, temperatura2, label="Semana2")
plt.title(f"Temperatura Semanales")
plt.ylabel("Temperatura ºC")
plt.legend()
plt.savefig("imagenes/linea_temperatura.png")
plt.show()