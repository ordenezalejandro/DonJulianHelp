from ModeladoDonJulian import RegistroDeVentas,RegistroDeClientes,RegistroDeMuebles
from guizero import App, Window, ListBox, MenuBar, TitleBox
import os


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

# def listar_muebles():
#     print('asdfasdf')
#     #return interfaz.registro_de_muebles.listar()
# interfaz = Interfaz()
#
# def info_cliente(value):
#     result = []
#     for cliente in interfaz.registro_de_clientes.diccionario:
#         if cliente[1] == value:
#             result.append(f'name:{cliente[1]} last name:{cliente[0]}')
#
#     app.info('info', f'clientes que matchea {",".join(result)}\n')
#
# class persona:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = 30
#         self.direccion = 'ropberto sironi'
#
#     def __str__(self):
#         return f'{self.nombre}, {self.apellido}'
# def mostrar_info(event):
#     app.info('info', f'La informacion de la persona es{event.widget.value}')
#
# windows = Window(app, title="Cliente")
# menubar = MenuBar(app,
#                   toplevel=["Muebles", "Cliente"],
#
#                   options=[
#                       [["Listar", interfaz.registro_de_muebles.listar], ["agregar", interfaz.registro_de_muebles.agregar]],
#                       [["mostrar", windows.show], ["ocultar", windows.hide]]
#                   ])
# list_box = ListBox(windows, selected='jairo', items=[persona('jairo', 'ordonez'), persona('ale', 'ordonez'), persona('sami', 'ordonez')])
# list_box.when_double_clicked = mostrar_info


class clienteRow:
    def __init__(self, ventana, cliente):
        self.cliente = cliente
        # self.box =
class VentanaCliente:

    def __init__(self, app, registro_de_cliente):
        self.ventana = Window(app, title='Clientes de DonJulian', visible=False)
        self.title_box = TitleBox(self.ventana, 'Lista de clientes de DonJulian')
        self.registro_cliente = registro_de_cliente
        self.list_box = ListBox(self.ventana, items=self.registro_cliente.listar())

    def cerrar(self):
        self.ventana.hide()

    def abrir(self):
        self.ventana.show()

class VentanaMueble:

    def __init__(self, app, registro_mueble):
        self.ventana = Window(app, title='Muebles de DonJulian', visible=False)
        self.registro_mueble = registro_mueble

    def cerrar(self):
        self.ventana.hide()

    def abrir(self):
        self.ventana.show()

class VentanaDonJulian:

    def __init__(self):
        self.app = App(
            title="Don Julian",
            width=800,
            height=800,
            layout="auto"
        )
        self.interfaz = Interfaz()
        self.ventana_cliente = VentanaCliente(self.app, self.interfaz.registro_de_clientes)
        self.ventana_mueble = VentanaMueble(self.app, self.interfaz.registro_de_muebles)
        self.menu = MenuBar(self.app,
                  toplevel=["Muebles", "Cliente"],
                  options=[
                      [["Mostrar", self.ventana_mueble.abrir], ["ocultar", self.ventana_mueble.cerrar]],
                      [["mostrar", self.ventana_cliente.abrir], ["ocultar", self.ventana_cliente.cerrar]]
                  ])

        self.app.display()


if __name__ == '__main__':
    don_julian = VentanaDonJulian()

