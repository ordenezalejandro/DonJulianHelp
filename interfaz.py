"""
este archivo contiene interfaz, con las siguientes funcionalidades
- iniciar programa
- imprimir menu
- leer comando
- ejecutar comando
- salir
"""
from .ModeladoDonJulian import RegistroDeVentas,RegistroDeClientes,RegistroDeMuebles
class Interfaz:
    def __init__(self):
        self.registro_de_ventas = RegistroDeVentas()
        self.registro_de_clientes = RegistroDeClientes()
        self.registro_de_muebles = RegistroDeMuebles()

def imprimir_menu():
"""mostrar menu"""

    pass

def leer_comando():

    pass