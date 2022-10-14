"""
este archivo contiene interfaz, con las siguientes funcionalidades
- iniciar programa
- imprimir menu
- leer comando
- ejecutar comando
- salir
"""
from ModeladoDonJulian import RegistroDeVentas,RegistroDeClientes,RegistroDeMuebles

MENU = """
1- agregar cliente
2- agrega mueble
3- agregar venta
4- lista de cliente
5- listar mueble
6- listar venta
7- salir
"""
class Interfaz:
    def __init__(self):
        self.registro_de_ventas = RegistroDeVentas()
        self.registro_de_clientes = RegistroDeClientes()
        self.registro_de_muebles = RegistroDeMuebles()
        self.corriendo = True

    def iniciar_programa(self):
        imprimir_menu()

        while self.corriendo == True:
            comando = leer_comando()
            self.ejecutar_comando(comando)
            imprimir_menu()
    def salir(self):
        self.corriento = False
        print("nos vemos")
        self.registro_de_clientes.guardar_clientes()
        self.registro_de_muebles.guardar_muebles()
    #     todo: implementar la funcion guardar muebles
    def ejecutar_comando(self,comando):

        if comando not in (1,2,3,4,5,6,7):

            self.comando_invalido()

        else:
            if comando == 1 :
                self.registro_de_clientes.agregar_cliente_input()

            if  comando == 2:
                self.registro_de_muebles.agregar_mueble_input()
            #     falta metodo
            if comando == 3:
                self.registro_de_ventas.registrar_venta_input()
            if comando == 4:
                self.registro_de_clientes.listar_cliente()
            if comando == 5:
                self.registro_de_muebles.listar_mueble()
            if comando == 6:
                self.registro_de_ventas.listar_ventas()
            if comando== 7:
                self.salir()
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
    comando = int(input("ingrese el comando"))
    return comando

    pass