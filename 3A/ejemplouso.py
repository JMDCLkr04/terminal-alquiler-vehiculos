from vehiculos import *
from sistema import *

sistema_alquiler = SistemaAlquiler()

sistema_alquiler.agregar_carro(Carro("toyota", "corolla", 2022, 500, 4))
sistema_alquiler.agregar_carro(Carro("honda", "civic", 2021, 450, 4))

sistema_alquiler.agregar_moto(Moto("yamaha", "asdafas", 2021, 300, 689))
sistema_alquiler.agregar_moto(Moto("honda", "mondongo", 2020, 350, 599))

sistema_alquiler.mostrar_lista_carros()
sistema_alquiler.mostrar_lista_motos()
sistema_alquiler.mostrar_informacion_carro(1)
sistema_alquiler.mostrar_informacion_moto(2)