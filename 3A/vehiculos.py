class Vehiculo:
    def __init__(self, marca, modelo, año, mensual):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.mensual = mensual

    def mostrar_informacion(self):
        info = f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\nPrecio Alquiler Mensual: {self.mensual} USD"
        return info

class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, mensual, num_puertas):
        super().__init__(marca, modelo, año, mensual)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"\nNúmero de Puertas: {self.num_puertas}"
        return info

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, mensual, cilindrada):
        super().__init__(marca, modelo, año, mensual)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"\nCilindrada: {self.cilindrada} cc"
        return info

# Nueva clase para manejar la lista de vehículos
class SistemaAlquiler:
    def __init__(self):
        self.carros = []
        self.motos = []

    def agregar_carro(self, carro):
        self.carros.append(carro)

    def agregar_moto(self, moto):
        self.motos.append(moto)

    def mostrar_lista_carros(self):
        print("Lista de Carros:")
        for i, carro in enumerate(self.carros, 1):
            print(f"{i}. {carro.marca} {carro.modelo} ({carro.año})")

    def mostrar_lista_motos(self):
        print("Lista de Motos:")
        for i, moto in enumerate(self.motos, 1):
            print(f"{i}. {moto.marca} {moto.modelo} ({moto.año})")

    def mostrar_informacion_carro(self, indice):
        if 0 < indice <= len(self.carros):
            print(self.carros[indice - 1].mostrar_informacion())
        else:
            print("Carro no encontrado.")

    def mostrar_informacion_moto(self, indice):
        if 0 < indice <= len(self.motos):
            print(self.motos[indice - 1].mostrar_informacion())
        else:
            print("Moto no encontrada.")

# Ejemplo de uso
sistema_alquiler = SistemaAlquiler()

# Agregando carros y motos
sistema_alquiler.agregar_carro(Carro("Toyota", "Corolla", 2022, 500, 4))
sistema_alquiler.agregar_carro(Carro("Honda", "Civic", 2021, 450, 4))

sistema_alquiler.agregar_moto(Moto("Yamaha", "MT-07", 2021, 300, 689))
sistema_alquiler.agregar_moto(Moto("Honda", "CBR600RR", 2020, 350, 599))

# Mostrar listas de carros y motos
sistema_alquiler.mostrar_lista_carros()
sistema_alquiler.mostrar_lista_motos()

# Elegir carro o moto por número para mostrar información
print("\nInformación del Carro seleccionado:")
sistema_alquiler.mostrar_informacion_carro(1)

print("\nInformación de la Moto seleccionada:")
sistema_alquiler.mostrar_informacion_moto(2)
