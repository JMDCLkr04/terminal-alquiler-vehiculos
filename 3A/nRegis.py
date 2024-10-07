from vehiculos import SistemaAlquiler  # Suponiendo que se necesita para otras partes del programa

class Registro:
    def __init__(self, cliente, idCliente, idVendedor, monto, tiempo):
        self.cliente = cliente
        self.idCliente = idCliente
        self.idVendedor = idVendedor
        self.monto = monto
        self.tiempo = tiempo
        self.registro = self.regis()

    def regis(self):
        ver = f"El cliente {self.cliente}, solicitó un vehículo por {self.tiempo}, con cédula {self.idCliente}"
        return ver

def opciones_menu():
    while True:
        print("---- Menú principal ----")
        print("Escoja una opción: \n")
        print("1. Reservar vehículo")
        print("2. Ver vehículos disponibles")
        print("3. Salir")
        
        opcion = int(input("Escriba la opción a elegir: "))
        
        if opcion == 1:
            # Aquí capturamos los datos del cliente
            cliente = input("Ingrese el nombre del cliente: ")
            idCliente = input("Ingrese la cédula del cliente: ")
            idVendedor = input("Ingrese el ID del vendedor: ")
            monto = float(input("Ingrese el monto del alquiler: "))
            tiempo = input("Ingrese el tiempo de alquiler (ej. '1 mes'): ")
            
            # Crear una instancia de la clase Registro con los datos
            registro_venta = Registro(cliente, idCliente, idVendedor, monto, tiempo)
            print(registro_venta.registro)
        
        elif opcion == 2:
            print("Aquí se mostrarán los vehículos disponibles.")
            # Llamar a la función que muestra vehículos (asumiendo que se implementará)
        
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
opciones_menu()
