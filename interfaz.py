"""
este archivo contiene interfaz, con las siguientes funcionalidades
- iniciar programa
- imprimir menu
- leer comando
- ejecutar comando
- salir
"""
from copy import copy
import os

from ModeladoDonJulian import RegistroDeVentas,RegistroDeClientes,RegistroDeMuebles

MENU = """
1- agregar cliente
2- agrega mueble
3- agregar venta
4- lista de cliente
5- listar mueble
6- listar venta
7 -borrar cliente
8 - imprimir ventas por clientes
9- listar venta por mueble 
10- consultar montos de ventas
11- gasto por cliente
12- salir
13 - parchar ventas
14 - parchar ventas para que funcionen los items
15 - parchar ventas cambiar a nuevo indice
16 - Editar cliente
17 - Editar mueble
18 - Editar Venta
19 - parchar fecha
"""
class Interfaz:
    def __init__(self,prefix='registro'):
        self.registro_de_ventas = RegistroDeVentas(prefix)
        self.registro_de_clientes = self.registro_de_ventas.registro_de_clientes
        self.registro_de_muebles = self.registro_de_ventas.registro_de_muebles
        self.corriendo = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.registro_de_ventas.data_path):
            os.remove(self.registro_de_ventas.data_path)
        if os.path.exists(self.registro_de_clientes.data_path):
            os.remove(self.registro_de_clientes.data_path)
        if os.path.exists(self.registro_de_muebles.data_path):
            os.remove(self.registro_de_muebles.data_path)

    def iniciar_programa(self):
        imprimir_menu()
        while self.corriendo == True:
            comando = leer_comando()
            if comando == -1:
                self.comando_invalido()
            else:
                self.ejecutar_comando(comando)
            imprimir_menu()

    def salir(self):
        self.corriendo = False
        print("nos vemos")
        self.registro_de_clientes.guardar()
        self.registro_de_muebles.guardar()
        self.registro_de_ventas.guardar()
    #     todo: implementar la funcion guardar muebles

    def ejecutar_comando(self,comando):

        if comando not in (1,2,3,4,5,6,7,8,9,10,11,12,13, 14,15, 16, 17, 18, 19):

            self.comando_invalido()

        else:
            if comando == 1 :
                return self.registro_de_clientes.agregar_input()
            if comando == 2:
                return self.registro_de_muebles.agregar_input()
            #     falta metodo
            if comando == 3:
                return self.registro_de_ventas.agregar_input()
            if comando == 4:
                return self.registro_de_clientes.listar()
            if comando == 5:
                return self.registro_de_muebles.listar()
            if comando == 6:
                return self.registro_de_ventas.listar()
            if comando == 7:
                return self.registro_de_clientes.borrar()
            if comando == 8:
                return self.registro_de_ventas.imprimir_ventas_de_cliente()
            if comando == 9:
                return self.registro_de_ventas.imprimir_ventas_de_mueble()
            if comando == 10:
                return self.registro_de_ventas.total_de_ventas()
            if comando == 11:
                return self.registro_de_ventas.gasto_por_cliente()
            if comando == 12:
                return self.salir()
            if comando == 13:
                return self.registro_de_ventas.parchar_ventas()
            if comando == 14:
                return self.registro_de_ventas.parchar_items()
            if comando == 15:
                return self.registro_de_ventas.parchar_indices()
            if comando == 16:
                return self.registro_de_clientes.editar_cliente()
            if comando == 17:
                return self.registro_de_muebles.editar_mueble()
            if comando == 18:
                return self.registro_de_ventas.editar_venta()
            if comando == 19:
                return self.registro_de_ventas.parchar_fechas()



#            no esta definido
    def comando_invalido(self):
        print("la opcion elegida esta fuera del menu")
        print("elija una opcion valida")

def imprimir_menu():
    """mostrar menu"""
    print (MENU)


    pass

def leer_comando():
    """leer comando"""
    comando = input("ingrese el comando:\n")
    if not comando.isdigit():
        return -1
    comando = int(comando) if comando else -1
    return comando

    pass
