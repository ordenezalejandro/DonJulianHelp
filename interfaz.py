from ModeladoDonJulian import RegistroDeVentas,RegistroDeClientes,RegistroDeMuebles
from guizero import App, Window, ListBox, MenuBar, TitleBox, PushButton, Box, TextBox, info, question, PushButton
import os

"""
descripcion del programa:

Este programa esta pensado para ayudar al dueño de una fabrica de mueble
- cararcteristicas:
    - el Programa debe mostrarme los clientes que tengo cargados
        - El programa tiene que permitirme agregar cliente
        - El programa tiene que permitirme editar , borrar, y listar
    - El programa debe mostrame los muebles que produzco
        - El programa tiene que permitirme agregar, borrar, listar, editar, mueble,
    - El programa debe mostrame las ventas que he echo
        - El Programa tiene Que permitirme agregar, modificar, listar ventas,
        
        
    la interfaz consta de los siguiente ventanas:\
    Ventana Clientes:
        Cuando se llega aca mostrara una lusta de cliente, que esa lista titene una fila con lo siguiente
            - info basica, mas botones de agregar, editar ,borrar, ver muebles, ver ventas 
    Ventana Ventas:
        Cuando se llega aca deberia mostrar las ventas, que estan sin entregar
        y las filas deberia tener botones, ver, pasar a terminada , borrar, editar. 
    ventana Mueble:
        inicialmente cargaria lso muebles en RowMueble, donde cada row se mueswtar datos del mueble, 
        uy los botones borrar, editar
        
"""
class Interfaz:
    def __init__(self, prefix='registro'):
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

#interfaz = Interfaz()

# def listar_muebles():
#     print('asdfasdf')
#     return interfaz.registro_de_muebles.listar()
#
# def info_cliente(value):
#     result = []
#     for cliente in interfaz.registro_de_clientes.diccionario:
#         if cliente[1] == value:
#             result.append(f'name:{cliente[1]} last name:{cliente[0]}')
#
#     app.info('info', f'clientes que matchea {",".join(result)}\n')

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
#     app.info('info', f'La informacion de l a persona es{event.widget.value}')
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
#
class BoxAgregarCliente:

    def __init__(self, ventana):
        self.box = Box(ventana)
        nombre_cliente = TextBox(self.box, text="Ingrese el nombre:")
        apellido = TextBox(self.box, text="Ingrese el apellido")
        self.box.hide()

    def agregar_cliente(self):
        nombre = question(title='Cliente', question='Ingrese nombre del cliente', initial_value='jairo')
        apellido = question(title="Apelllido", question='ingrese el apellido del cliente')

#
# class clienteRow:
#     def __init__(self, ventana, cliente):
#         self.cliente = cliente
#         # self.box =

class VentanaCliente:

    def __init__(self, app, registro_de_cliente):
        self.ventana = Window(app, title='Clientes de DonJulian', visible=False, bg='white')
        self.title_box = TitleBox(self.ventana, 'Lista de clientes de DonJulian', layout='grid', border=2)
        self.registro_cliente = registro_de_cliente
        self.list_box = ListBox(self.ventana, items=self.registro_cliente.listar())
        self.list_box.text_size = 16
        self.list_box.font = 'Arial'
        self.list_box.bg = 'green'
        self.box_agregar = BoxAgregarCliente(self.ventana)
        self.button_agregar = PushButton(self.ventana, text='Agregar nueva cliente', command=self.agregar_cliente )

    def cerrar(self):
        self.ventana.hide()

    def abrir(self):
        self.ventana.show()

    def agregar_cliente(self):
        parametro= {}
        parametro['nombre'] = question(title='Agregar Cliente', question='Ingrese nombre del cliente', initial_value='jairo')
        parametro['apellido'] = question(title="Agregar", question='ingrese el apellido del cliente')
        clave = tuple(parametro.values())
        if clave in self.registro_cliente.diccionario:
            self.ventana.info('Warning', 'El usuario ya esta registrado')
            return
        else:
            parametro['domicilio'] = question(title='Agregar Cliente', question='Ingrese el domicilio del cliente', initial_value='jairo')
            parametro['telefono'] = question(title='Agregar Cliente', question='Ingrese el telefono', initial_value='jairo')
            parametro['edad'] = int(question(title='Agregar Cliente', question='Ingrese el edad', initial_value='jairo'))

            new_cliente = self.registro_cliente.agregar_nueva_instancia(clave, parametro)
            self.list_box.append(new_cliente)

class VentanaMueble:

    def __init__(self, app, registro_mueble):
        self.ventana = Window(app, title='Muebles de DonJulian', visible=False)
        self.ventana.button_agregar = PushButton(app, text="Agregar",  grid=[0,0])
        self.ventana.button_editar = PushButton(app, text="Editar",  grid=[1,0])
        self.ventana.button_borrar = PushButton(app, text="Borrar",  grid=[2,0])
        self.ventana.button_borrar.when_double_clicked = self.borrar
        self.ventana.lista = ListBox(app, items=registro_mueble.listar_interfaz(), grid=[1,1])
        self.registro_mueble = registro_mueble

    def borrar(self):
        value_selected = self.ventana.lista.value
        self.ventana.lista.remove(value_selected)
        self.registro_mueble.borrar_interfaz(value_selected)
        self.ventana.lista.show()

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
            layout="grid"
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

