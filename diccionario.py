# integrantes: Javier Eduardo Guerrero Buendia
# ---          luis Enrrique Cortes 
marca = []
modelo = []
propietario = []
color = []

vehiculos = {
    "Marca": marca,
    "Modelo": modelo,
    "Propietario": propietario,
    "Color": color
}

def agregar_vehiculo():
    marca.append(input("Ingrese la marca del vehículo: "))
    modelo.append(input("Ingrese el modelo del vehículo: "))
    propietario.append(input("Ingrese el propietario del vehículo: "))
    color.append(input("Ingrese el color del vehículo: "))
    print("Vehículo agregado con éxito.")

def buscar_vehiculo():
    keyword = input("Ingrese una palabra clave para buscar: ")
    for i in range(len(marca)):
        if keyword in marca[i] or keyword in modelo[i] or keyword in propietario[i] or keyword in color[i]:
            print(f"Vehículo {i + 1}:")
            print(f"Marca: {marca[i]}")
            print(f"Modelo: {modelo[i]}")
            print(f"Propietario: {propietario[i]}")
            print(f"Color: {color[i]}")

def actualizar_vehiculo():
    num = int(input("Ingrese el número de vehículo que desea actualizar: "))
    if num >= 1 and num <= len(marca):
        marca[num - 1] = input("Ingrese la nueva marca del vehículo: ")
        modelo[num - 1] = input("Ingrese el nuevo modelo del vehículo: ")
        propietario[num - 1] = input("Ingrese el nuevo propietario del vehículo: ")
        color[num - 1] = input("Ingrese el nuevo color del vehículo: ")
        print("Vehículo actualizado con éxito.")
    else:
        print("Número de vehículo fuera de rango.")

def eliminar_vehiculo():
    num = int(input("Ingrese el número de vehículo que desea eliminar: "))
    if num >= 1 and num <= len(marca):
        del marca[num - 1]
        del modelo[num - 1]
        del propietario[num - 1]
        del color[num - 1]
        print("Vehículo eliminado con éxito.")
    else:
        print("Número de vehículo fuera de rango.")

while True:
    print("\nMenú:")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Actualizar vehículo")
    print("4. Eliminar vehículo")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    
    if opcion == "1":
        agregar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        actualizar_vehiculo()
    elif opcion == "4":
        eliminar_vehiculo()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print(vehiculos)