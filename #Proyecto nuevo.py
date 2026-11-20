
# Proyecto nuevo
import json
import os

carpeta_programa = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(carpeta_programa, "empleados.json")


class Empleado:
    def __init__(self, nombre, puesto, sueldo):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo

    def aumentar_sueldo(self, porcentaje):
        aumento = self.sueldo * porcentaje / 100
        self.sueldo += aumento

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Sueldo: {self.sueldo}")

    def Calcular_sueldo_anual(self):
        return self.sueldo * 12

    def Convertir_a_diccionario(self):
        return {
            "nombre": self.nombre,
            "puesto": self.puesto,
            "sueldo": self.sueldo
        }


# 1. Crear lista vacía
empleados = []

# 2. Intentar recuperar los empleados guardados
try:
    with open(ruta_json, "r") as archivo:
        resultado = json.load(archivo)

    for i in resultado:
        dato_empleado = Empleado(
            i["nombre"],
            i["puesto"],
            i["sueldo"]
        )
        empleados.append(dato_empleado)

except FileNotFoundError:
    print("No existe el archivo. Se iniciará una lista vacía.")

#Funcion guardar empleados:
def guardar_empleados():
    datos_empleados = []
    for dato in empleados:
        datos = dato.Convertir_a_diccionario()
        datos_empleados.append(datos)
    with open(ruta_json, "w") as archivo:
        json.dump(datos_empleados, archivo, indent=4)
# 3. Menú principal
opciones = 0

while opciones != 6:

    print("\n1. Agregar Empleado")
    print("2. Mostrar Empleado")
    print("3. Buscar empleado")
    print("4. modificar sueldo")
    print("5. Eliminar empleado")
    print("6. Salir")
    opciones = int(input("Seleccione una opción: "))

    while opciones < 1 or opciones > 6:
        print("Opción incorrecta. Debe seleccionar entre 1 y 6.")
        opciones = int(input("Seleccione una opción: "))

    if opciones == 1:
        cantidad = int(input("Cuántos empleados desea ingresar: "))

        while cantidad <= 0:
            print("La cantidad debe ser mayor a cero")
            cantidad = int(input("Cuántos empleados desea ingresar: "))

        for i in range(cantidad):
            nombre = input("Ingrese el Nombre: ")
            puesto = input("Ingrese el Puesto: ")
            sueldo = float(input("Ingrese el sueldo: "))

            while sueldo <= 0:
                print("El sueldo debe ser mayor a cero!!!")
                sueldo = float(input("Ingrese el sueldo: "))

            empleado = Empleado(nombre, puesto, sueldo)
            empleados.append(empleado)
            guardar_empleados()
    elif opciones == 2:
        if len(empleados) == 0:
            print("No hay empleados cargados.")
        else:
            for empleado in empleados:
                empleado.mostrar_datos()

    elif opciones == 3:
        buscar = input("Nombre del empleado que desea buscar: ")
        encontrado = False

        for empleado in empleados:
            if empleado.nombre.lower() == buscar.lower():
                empleado.mostrar_datos()
                encontrado = True

        if encontrado == False:
            print("No se encontró empleado con ese nombre!!!")

    elif opciones == 6:
        print("Programa finalizado....")
    elif opciones == 4:
        buscar = input("Nombre del empleado que desea buscar: ")
        empleado_encontrado= None
        for empleado in empleados:
            if empleado.nombre.lower() == buscar.lower():
                empleado_encontrado = empleado
                empleado.mostrar_datos()
                break
            
        if empleado_encontrado is None:
            print("Empleado no encontrado!!")
        else:
            nuevo_sueldo = float(input("Escriba el nuevo sueldo: "))
            while nuevo_sueldo <= 0:
                print("El sueldo debe ser mayor a cero")
                nuevo_sueldo = float(input("Escriba el nuevo sueldo: "))
            empleado_encontrado.sueldo = nuevo_sueldo
            empleado_encontrado.mostrar_datos()
            guardar_empleados()
    elif opciones == 5:
        buscar = input("Nombre del empleado que desea buscar para eliminar: ")
        empleado_encontrado = None
        for empleado in empleados:
            if empleado.nombre.lower() == buscar.lower():
                empleado_encontrado = empleado
                break
        if empleado_encontrado is None:
            print("Empleado no encontrado!")
        else:
            empleados.remove(empleado_encontrado)
            print("Se elimino empleado de la lista!")
            guardar_empleados()
# 5. Guardar los empleados en JSON
guardar_empleados()
print("Empleados guardados correctamente.")


