# coding: UTF8
import datetime
import json
import os.path
import pickle
import shelve
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

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"


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

    def __hash__(self):
        return hash((self.nombre, self.descripcion))
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

    def __init__(self, nombre, apellido, edad, domicilio=None, telefono=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def es_igual(self, basica):
        result = []
        for attributo, valor in basica:
            result.append(getattr(self, attributo) == valor)
        return all(result)

    def __eq__(self, other):
       return self.nombre == other.nombre and self.apellido == other.apellido

    def __lt__(self, otro_cliente):
        return self.edad < otro_cliente.edad

    def __gt__(self,otro_cliente):
        return self.edad> otro_cliente.edad

    def __repr__(self):
        return f'Cliente(**{str(self.__dict__)})'

    def __str__(self):
        return f'fullname: {self.nombre}  {self.apellido}'

    def __hash__(self):
        return hash((self.apellido, self.nombre))

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

    def __str__(self):
        return f'Cliente:{self.cliente} , mueble: {self.mueble.nombre} , fecha_entrega:{self.fecha_de_entrega}'

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
        self.diccionario = {} # este seria en que antes usamos, lista_de_clientes, lista_de_muebgles etc
        # setattr(self, f'lista_de{self.class_name}s', None)
        self.data_path = os.path.join(directory, 'data', f'registro_de_{self.class_name}.json')
        self.cargar()

    def get_diccionario(self):
        return self.diccionario

    def get_to_dump(self):
        return [(key, value.__dict__) for key, value in self.diccionario.items()]

    def cargar(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'rb') as archivo:
                # setattr(self.get_lista(), list(map(lambda x: Cliente(**x), json.load(archivo))))
                self.diccionario = pickle.load(archivo)
        else:
            with open(self.data_path, 'wb') as archivo:
                pickle.dump({}, archivo)
                self.diccionario = {}
        return self.get_diccionario()

    def guardar(self):
        # self.diccionario.close()
        with open(self.data_path, 'wb') as archivo:
            # todo: aqui me di cuenta que json.dump solo puede guardar objectos que contengan elementos basicos del lenguage, como clientes,
            #  es un ojbeto que nosotros creamos , es decir no es basico.  no serializable, accedi a cada cliente, el atributo __Dict__ que devuelve la representacion de eso.
            # eso seria lo mismo que hacer un for en la lista de cliente, y acceder al attributo __dict_):

            # for instance in self.get_lista():
            #     instances.append(instance.__dict__)  # todo objeto en python tiene el atributo __dict__. que representa la instancia
            # lista = list(self.get_diccionario().items())
            pickle.dump(self.diccionario, archivo, protocol=pickle.HIGHEST_PROTOCOL)
            # json.dump(list(map(attrgetter('__dict__'), self.listas_de_clientes)), archivo)

    def agregar(self, instance):
        assert type(instance) == self.clase
        if instance in self.get_diccionario():
            print(f'el {self.class_name} ya ha sido cargado')
        else:
            self.get_diccionario().append(instance)


    def agregar_input(self):
        # aqui pedimos la informacion basica
        parametros = self.pedir_informacion_basica_input()
        clave = tuple(parametros.values())
        # nos preguntamos si la clave (es decir la informacion basica que pedimos ya esta)
        if clave in self.get_diccionario():
            # obtenemos el objeto que estaba asociado
            instancia = self.get_diccionario()[clave]
            print(f'Objecto {self.class_name} encontrada: {instancia}\n')
            return instancia
        else:
            print(f'No hemos encontrado el objeto {self.class_name} \n')
            print(f'Solicitando datos para registrarlo')
            # pasamos los datos basicos que pedimos, y pedimos el resto.
            parametros = self.pedir_informacion_completa_input(parametros)
        # instanciamos la clase con todo los datos que ya habiamos encontrados
        nueva_instancia = self.clase(**parametros)
        self.get_diccionario()[tuple(clave)] = nueva_instancia
        self.guardar()
        self.cargar()
        return nueva_instancia

    def borrar(self):
        parametros = self.pedir_informacion_basica_input()
        clave = tuple(parametros.values())
        if clave in self.get_diccionario():
            self.get_diccionario().pop(clave)
            print(f"El objecto {self.class_name} con valores {clave} se borro exitosamente")
        else:
            print(f'No se encotro instancia de {self.class_name} con estos valores {clave}')
        self.guardar()
        self.cargar()
    def pedir_informacion_basica_input(self):
        """"
        Recordar que estas deben ser guardadas en el orden en el qeu se generan las claves primarias
        ejemplo: si la informacion es apellido y nombre, es decir en el dicionario se va almacenar asi, deberian pedirse de la
        siguiente forma
        parametros['clave1'] = 'valor_clave_1'
        parametros['clave2'] = 'valor_clave_2'
        """
        raise Exception("Esto metodo no se implemento")

    def pedir_informacion_completa_input(self, parametros):
        """
        esto una interfaz, que deberia los datos necesario para crear una instancia nueva
        debe devolver una dictionario con los parametros para instanciar una nueva instancia de la clase.
        :return:
        """
        raise Exception('Este methodo deberia ser implementado')

    def listar(self):
        if not self.diccionario:
            print(f'No hay ninguna instancia de {self.class_name} para mostrar')
        for element in self.diccionario.values():
            print(element)


class RegistroDeClientes(Serializable):
    def __init__(self):
       super(RegistroDeClientes, self).__init__(Cliente)

    def pedir_informacion_completa_input(self, parametros):
        parametros['edad'] = input ('ingrese la edad del cliente\n')
        parametros['domicilio'] = input('ingrese el domicilio\n')

        return parametros

    def pedir_informacion_basica_input(self):
        parametro = {} #dict()
        parametro['apellido'] = input('apellido del cliente\n')
        parametro['nombre'] = input('nombre del cliente\n')
        return parametro





class RegistroDeMuebles(Serializable):
    def __init__(self):
        super(RegistroDeMuebles, self).__init__(Mueble)

    def pedir_informacion_basica_input(self):
        parametros = {}
        parametros['nombre'] = input('Ingrese el nombre del mueble\n')
        parametros['descripcion'] = input('Ingrese el descripcion del mueble\n')

        return parametros

    def pedir_informacion_completa_input(self, parametros):
        parametros['precio'] = input('Ingrese el precio del mueble\n')
        return parametros

class RegistroDeExtra(Serializable):
    def __init__(self):
        super(RegistroDeExtra, self).__init__(Pieza)

    def pedir_informacion_completa_input(self, parametros):
        parametros['precio'] = input('Ingrese el precio del mueble\n')

    def pedir_informacion_basica_input(self):
        parametros = {}
        parametros['nombre'] = input('Ingrese el nombre del mueble\n')
        parametros['descripcion'] = input('Ingrese el descripcion del mueble\n')

        return parametros

class RegistroDeVentas(Serializable):

    def __init__(self):
        super(RegistroDeVentas, self).__init__(Venta)
        self.registro_de_clientes = RegistroDeClientes()
        self.registro_de_muebles = RegistroDeMuebles()

    def pedir_informacion_basica_input(self):
        parametros = {}
        parametros['cliente'] = self.registro_de_clientes.agregar_input()
        parametros['mueble'] = self.registro_de_muebles.agregar_input()
        parametros['fecha_de_entrega'] = input('Ingrese la fecha de entrega en formato dd-mm-yyyy\n')

        return parametros

    def pedir_informacion_completa_input(self, parametros):
        parametros['total'] = int(input("Ingrese el precio total de la venta"))
        parametros['adelanto'] = int(input("Ingrese cuanto deposito el clente como entrega"))
        parametros['motivo'] = input("Ingrese el motivo de la venta (o deje en blanco si no tiene motivo)")

        return parametros

    def listar_por_cliente(self, cliente):
        # recorrer las ventas
        result = []
        for claves, venta in self.diccionario.items():
            if claves and cliente == claves[0]:
                result.append(venta)

        return result

    def listar_venta_por_mueble(self, mueble):
        result = []
        for claves, venta in self.diccionario.items():
            if claves and mueble == claves[1]:
                result.append(venta)

        return result

    def imprimir_ventas_de_mueble(self):
        claves = tuple(self.registro_de_muebles.pedir_informacion_basica_input().values())
        if claves not in self.registro_de_muebles.diccionario:
            print(f'el mueble {claves [0]} {claves [1]} no existe')
            return False
        mueble = self.registro_de_muebles.diccionario[claves]
        ventas = self.listar_venta_por_mueble(mueble)
        for mueble in ventas:
            print(mueble)

    def imprimir_ventas_de_cliente(self):
        claves = tuple(self.registro_de_clientes.pedir_informacion_basica_input().values())
        if claves not in self.registro_de_clientes.diccionario:
            print(f'El cliente {claves[0]} {claves[1]} no existe')
            return False
        cliente = self.registro_de_clientes.diccionario[claves]
        ventas = self.listar_por_cliente(cliente)
        for venta in ventas:
            print(venta)
        # fijarnos que pertenezca al cliente

        # pertenece los guardamos en un lugar
        # develvor la lista

    def total_de_ventas(self):

        """una nueva funcionalidad , para que el usuario puedo consultar todos las ventas,
           y la funcionalidad debe sumar toodas las ventas realizadas
        """
        result = []

        for venta in self.diccionario.values():
            result.append(venta.total)
        print(f' El total de las ventas es:/n $', sum(result))

    def gasto_por_cliente(self):

        """("gasto por cliente"), el sistema deberia pedir, que cliente,..etc, luego antes de
        escribir el codigo escribilo como lo harias, agregar  la nueva funcion, agregar el comando,
         definir el comando, el comando debe pedir al usuario la informacio basica del cliente, obter el cliente,
        y buscar despus las ventas de ese cliente, y sumar el mono de esas especicficas venas.
        """
        claves = tuple(self.registro_de_clientes.pedir_informacion_basica_input().values())
        if claves not in self.registro_de_clientes.diccionario:
            print(f'El cliente {claves[0]} {claves[1]} no existe')
            return False
        cliente = self.registro_de_clientes.diccionario[claves]
        ventas = self.listar_por_cliente(cliente)
            # metodo 1 for
        total = 0
        for venta in ventas:
            total += venta.total

        print(f' El monto de ventas del cliente es:/n $', total)

        #metodo 2 sum+compresion
        print(f' El monto de ventas del cliente es:/n $', sum([venta.total for venta in ventas]))

        # metodo 3 sum+lamda+map
        print(f' El monto de ventas del cliente es:/n $', sum(map(lambda venta:venta.total,ventas )))



class Menu:
    def __init__(self):
        #todo: definir el metodo init
        pass

    def choose_menu(self): # elegir menu
        # todo: definir una funcion que llame a un menu
        pass
