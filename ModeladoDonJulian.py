import datetime
import json
import os.path
import pickle
from operator import attrgetter

class Mueble:
    def __init__(self,nombre, descripcion,precio,lista_de_piezas = None ,lista_de_extras = None):
        self.nombre = nombre
        self.descripcion = descripcion
        if lista_de_piezas == None :
            self.lista_de_piezas = []
        else:
            self.lista_de_pieza = lista_de_piezas
        if lista_de_extras == None :
            self.lista_de_extras = []
        else:
            self.lista_de_extras = lista_de_extras
        self.precio = precio
        print('mueble_nuevo')

    def __eq__(self, other):
        return self.nombre == other.nombre and self.descripcion == self.descripcion and self.precio == self.precio

    def agregar_pieza(self,pieza):
        assert type(pieza) == Pieza
        self.lista_de_piezas.append(pieza)

    def agregar_extra(self,extra):
        self.lista_de_extras.append(extra)

    def cantidad_de_piezas(self):
        return len (self.lista_de_piezas)

    """Crear un método en la clase mueble, que se llame  calcular_despiece,
    que no tome parámetro, y que devuelve la suma de los pie de cada pieza,
     (recordar que los piez están en la instancia, con el atributo 
     lista_de_pieza )"""

    def calcular_despiece(self):
        """
        recorrer la lista_de_pieza, calcular_el pie.
        guardar el valor y sumarlo a la pieza anterior, en una variable.
        retorne una variable

        """
        sumatoria_de_pie = 0

        for pieza in self.lista_de_piezas:

            pie = pieza.calcular_pie()

            sumatoria_de_pie = sumatoria_de_pie + pie

        return sumatoria_de_pie

    def calcular_precio_de_piezas(self):

        valor_de_piezas = 0

        for pieza in self.lista_de_piezas:

            precio_de_piezas = pieza.precio

            valor_de_piezas = valor_de_piezas +precio_de_piezas

        return valor_de_piezas

    def calcular_precio_de_extras(self):

        valor_de_extras = 0

        for extra in self.lista_de_extras:
            precio_extra = extra.precio

            valor_de_extras = valor_de_extras + precio_extra

        return valor_de_extras

    def devolver_costo_de_mueble(self):

        costo_de_mueble = self.calcular_precio_de_piezas() + self.calcular_precio_de_extras()

        return costo_de_mueble


        # TODO: pass


class Pieza:
    def __init__(self,alto,ancho,espesor,descripcion,precio=1):
        self.alto = alto
        self.ancho = ancho
        self.espesor = espesor
        self.descripcion = descripcion
        self.precio = precio

    def calcular_pie(self):
        return (self.alto * self.ancho * self.espesor)/900


class Extra:
    def __init__(self,nombre, descripcion, precio = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    # def cantidad_extra(self):
    #     self.cantidad_extra = lista_extra # todo: corregir esto, que es lista_extra, donde se declara
    #     return len(lista_de_piezas)

class Cliente:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __eq__(self, other):
       return self.nombre == other.nombre and self.apellido == other.apellido

    def __lt__(self, otro_cliente):
        return self.edad < otro_cliente.edad

    def __gt__(self,otro_cliente):
        return self.edad> otro_cliente.edad

    def __repr__(self):
        return f'Cliente(**{self.__dict__})'

    def __str__(self):
        return f'fullname: {self.nombre}  {self.apellido}'

class Venta:
    def __init__(self, cliente=None, mueble=None,fecha_de_entrega=None,total=None,adelanto=0,motivo=None):
        self.cliente =cliente
        self.mueble = mueble
        self.fecha_de_venta = datetime.datetime.now()
        self.fecha_de_entrega = fecha_de_entrega
        self.total = total
        self.adelanto = adelanto
        self.motivo = motivo
        self.saldo = self.total - self.adelanto

    def poner_cliente(self, cliente):
        assert isinstance(cliente, Cliente)
        self.cliente = cliente

    def poner_mueble(self,mueble):
        assert isinstance(mueble,Mueble)
        self.mueble = mueble

    def poner_motivo(self,motivo):
        assert isinstance(motivo,str)
        self.motivo = motivo

    def poner_precio(self,precio):
        assert isinstance(precio,float)
        self.precio = precio

    def adelanto(self,adelanto):
        assert isinstance(adelanto, float)
        self.adelanto = adelanto

    def calcular_saldo(self):
        return self.precio - self.adelanto

    def guardar_venta(self):
        with open('registro_de_ventas.json', 'w') as archivo:
            json.dump(self.listas_de_ventas, archivo)

    def guardar_cargar(self):
        with open('registro_de_ventas.json', 'r') as archivo:
            self.lista_de_ventas = json.load(archivo)


class Serializable:
    def __init__(self, clase):
        self.class_name = clase.__name__
        self.clase = clase
        directory = os.path.split(__file__)[0]
        self.lista = [] # este seria en que antes usamos, lista_de_clientes, lista_de_muebgles etc
        # setattr(self, f'lista_de{self.class_name}s', None)
        self.data_path = os.path.join(directory, 'data', f'registro_de_{self.class_name}.json')
        self.cargar()

    def get_lista(self):
        return self.lista

    def cargar(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'rb') as archivo:
                # setattr(self.get_lista(), list(map(lambda x: Cliente(**x), json.load(archivo))))
                self.lista = pickle.load(archivo)
        else:
            with open(self.data_path, 'wb') as archivo:
                pickle.dump([], archivo)
                self.lista = []
        return self.get_lista()

    def guardar(self):
        with open(self.data_path, 'wb') as archivo:
            # todo: aqui me di cuenta que json.dump solo puede guardar objectos que contengan elementos basicos del lenguage, como clientes,
            #  es un ojbeto que nosotros creamos , es decir no es basico.  no serializable, accedi a cada cliente, el atributo __Dict__ que devuelve la representacion de eso.
            # eso seria lo mismo que hacer un for en la lista de cliente, y acceder al attributo __dict_):

            # for instance in self.get_lista():
            #     instances.append(instance.__dict__)  # todo objeto en python tiene el atributo __dict__. que representa la instancia
            pickle.dump(self.lista, archivo)
            # json.dump(list(map(attrgetter('__dict__'), self.listas_de_clientes)), archivo)

    def agregar(self, instance):
        assert type(instance) == self.clase
        if instance in self.get_lista():
            print(f'el {self.class_name} ya ha sido cargado')
        else:
            self.get_lista().append(instance)

    def agregar_input(self):
        parametros = self.pedir_informacion_input()
        nueva_instancia = self.clase(**parametros)
        if nueva_instancia in self.get_lista():
            print(f'La instancia de {self.class_name} con valores {self.__dict__} ya existe')
        else:
            self.get_lista().append(nueva_instancia)
        return nueva_instancia

    def pedir_informacion_input(self):
        """
        esto una interfaz, que deberia los datos necesario para crear una instancia nueva
        debe devolver una dictionario con los parametros para instancianr una nueva instancia de la clase.
        :return:
        """
        raise Exception('Este methodo deberia ser implementado')

    def listar(self):
        for element in self.lista:
            print(element)
    #
    # def obtener_instance(self, **kargs):
    #     claves = self.ingrese_claves()



class RegistroDeClientes(Serializable):
    def __init__(self):
       super(RegistroDeClientes, self).__init__(Cliente)

    def agregar_cliente_input (self):
        parametro = {} #dict()
        parametro['apellido'] = input ('apellido del cliente')
        parametro['nombre'] = input ('nombre del cliente')
        parametro['edad'] = input ('ingrese la edad del cliente')

        return parametro



class RegistroDeMuebles(Serializable):
    def __init__(self):
        super(RegistroDeMuebles, self).__init__(Mueble)

    def pedir_informacion_input(self):
        parametros = {}
        parametros['nombre'] = input('Ingrese el nombre del mueble\n')
        parametros['descripcion'] = input('Ingrese el descripcion del mueble\n')
        parametros['precio'] = input('Ingrese el precio del mueble\n')
        return parametros

class RegistroDeExtra(Serializable):
    def __init__(self):
        super(RegistroDeExtra, self).__init__(Pieza)

    def pedir_informacion_input(self):
        parametros = {}
        parametros['nombre'] = input('Ingrese el nombre del mueble\n')
        parametros['descripcion'] = input('Ingrese el descripcion del mueble\n')
        parametros['precio'] = input('Ingrese el precio del mueble\n')
        return parametros

class RegistroDeVenta(Serializable):

    def __init__(self):
        super(RegistroDeVenta).__init__(Venta)
        self.registro_de_clientes = RegistroDeClientes()
        self.registro_de_muebles = RegistroDeMuebles()

    def pedir_informacion_input(self):
        parametros = {}
        parametros['cliente'] = self.registro_de_clientes.agregar_input()
        parametros['mueble'] = self.registro_de_muebles.agregar_input()
        parametros['fecha_de_venta'] = datetime.datetime.now()
        parametros['fecha_de_entrega'] = input('Ingrese la fecha de entrega en formato dd-mm-yyyy\n')
        parametros['total'] = int(input("Ingrese el precio total de la venta"))
        parametros['adelanto'] = int(input("Ingrese cuanto deposito el clente como entrega"))
        parametros['motivo'] = input("Ingrese el motivo de la venta (o deje en blanco si no tiene motivo)")
        parametros['saldo'] = parametros['total'] - parametros['adelanto']
        return parametros


class Menu:
    def __init__(self):
        #todo: definir el metodo init
        pass

    def choose_menu(self): # elegir menu
        # todo: definir una funcion que llame a un menu
        pass
