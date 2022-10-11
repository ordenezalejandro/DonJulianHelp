import datetime
import json


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

    def cantidad_extra(self):
        self.cantidad_extra = lista_extra
        return len(lista_de_piezas)

def total_componentes(lista_de_piezas,lista_extra):
    return len(lista_de_piezas) +len(lista_extra)


# todo: sacar la definicion de estas instancias a otro archivo
lista_de_piezas = []
estante = Pieza(50,30,2,'estante')
puerta = Pieza(58,35,2.3,'puerta bajo')
zocalo = Pieza(7,200,2,'zocalo bajo')

lista_de_piezas.append(estante)
lista_de_piezas.append(puerta)
lista_de_piezas.append(zocalo)

lista_extra = []
bisagra = Extra('bisagra','2 bisagras x puerta')
tornillos = Extra('tornillos', '8 tornillos x puerta')
guias = Extra('guias','telescopicas de 45')

lista_extra.append(bisagra)
lista_extra.append(tornillos)
lista_extra.append(guias)

cajonera = Mueble('cajonera', '6 cajones',100,lista_de_piezas,lista_extra)

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

class Venta:
    def __init__(self):
        self.cliente = None
        self.mueble = None
        self.fecha_de_venta = datetime.datetime.now()
        self.fecha_de_entrega = None
        self.total = None
        self.seña = None
        self.motivo = None
        self.saldo = None

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




class RegistroDeVentas:
    def __init__(self):
        self.lista_de_ventas = []
        self.registro_de_clientes = RegistroDeClientes()

    def agregar_venta(self,venta):
        assert type(venta) == Venta
        self.lista_de_ventas.append(venta)

    def devolver_cantidad_ventas(self):
        return len (self.lista_de_ventas)



    def devolver_las_ventas_de(self,cliente):
        coincidencia = []

        for venta in self.lista_de_ventas:
            if self.venta.cliente.__eq__(cliente):
                coincidencia.append(venta)
        return coincidencia




    # recorra la lista de venta-->for
    # compare q los nombres sean iguales--> ==
    #si son iguales agregarlos a la lista devolver_ventas_de--> append.devolver_las_ventas_de
    # retornar esa lista de coincidencias



    def listar_ventas(self):
        """definir el methodo listar_ventas, de la clase registro_ventas,
        que no toma parametro, y que recorre la lista de ventas, e imprime,
         el nombre y apellido del cleinte, el nombre del mueble,
         y la fecha_de inicio, la fecha de salida"""

        for venta in self.lista_de_ventas:
            print('nombre{},apelllido{},mueble{},fecha de venta{},fecha de entrega{}'.format(venta.cliente.nombre,venta.cliente.apellido,venta.mueble,venta.fecha_de_venta,venta.fecha_de_entrega))

    def registrar_venta_input(self):
        cliente = self.registro_de_clientes.agregar_cliente_input()
        new_venta = Venta()
        new_venta.poner_cliente(cliente)
        mueble = self.registro_de_mueble.agregar_mueble_input()
        new_venta.poner_mueble(mueble)
        self.agregar_venta(new_venta)

    def guardar_ventas(self):

        with open('registro_de_ventas.json', 'w') as archivo:
            json.dump(self.listas_de_ventas, archivo)


"""agregar el methodo agregar_venta,  a la clase RegistroVenta, 
que toma como una parametro una instancia de venta, 
y la agrega a la lista."""


class RegistroDeClientes:
    def __init__(self):
        self.listas_de_clientes = []
        self.cargar_cliente()

    def agregar_cliente(self,cliente):
        assert type(cliente) == Cliente
        self.listas_de_clientes.append(cliente)

    def agregar_cliente_input (self):
        apellido = input ('apellido del cliente')
        nombre = input ('nombre del cliente')
        edad = input ('ingrese la edad del cliente')
        if self.existe_cliente(nombre,apellido):
            cliente = self.obtener_cliente(nombre,apellido)

        else :

            cliente = Cliente (apellido =apellido,nombre = nombre,edad =edad)

            self.agregar_cliente(cliente)

        return cliente

    def existe_cliente(self,nombre,apellido):
        for cliente in self.lista_de_clientes:
            if cliente.nombre == nombre and cliente.apellido == apellido:
                return True
        return False


    def guardar_cliente(self):

        with open ('registro_de_clientes.json', 'w') as archivo:
            json.dump(self.listas_de_clientes, archivo)

    def cargar_cliente(self):

        with open ('registro_de_clientes.json','r') as archivo:

            self.lista_de_clientes = json.load(archivo)

class Num:

    def __init__(self,numero,lista_de_numeros):
        self.numero = numero
        self.lista_de_numeros = lista_de_numeros
    def sumatoria(self):

        sumatoria_de_numeros = 0

        for numeros in lista_de_numeros:

            numero = num.numero

            sumatoria_de_numeros = sumatoria_de_numeros + numero

        return sumatoria_de_numeros

def sumar_lista_de_numeros(lista_de_numeros):

    sumar = 0

    for numero in lista_de_numeros:

        sumar += numero

    return sumar

def productoria_lista_de_numeros(lista_de_numeros):

    multiplicar = 1

    for numero in lista_de_numeros:

        multiplicar *= numero

    return multiplicar


"""ponele si yo te digo, hace una funcion que tome , una lista de 
lista de numeros, y devuelva una sola lista con todos los numero,
es decir. aplanar_lista([[1,2,3], [3,4,5], [2,0]])  
deberia devolver [1,2,3,4,5,2,0]"""

"""
lista de, lista de numeros,
agruparlos en una sola lista, con la funcion append 
"""
def aplanar_listas(lista_de_lista_de_numeros):

    lista_aplanada = []

    for lista_de_numeros in lista_de_lista_de_numeros:

        lista_aplanada.append(lista_de_numeros)

    return lista_aplanada

"""def dame_mayor, que tome una lista y me devuelva el de mayor valor"""

def dame_mayor(lista):

    mayor = lista[0]

    for numero in lista:


        if mayor < numero:

            mayor = numero

    return mayor

"""
recorrer la lista
evaluar si es par o impar
asignarlos a una nueva lista
devuelva las 2 listas
"""

def par_o_impar(lista):

    par = []
    impar = []

    for numero in lista:
        if numero%2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    return par , impar

def separar_sub_20(lista_de_personas):

    menor_de_20 = []
    mayor_20 = []

    for persona in lista_de_personas:

        if persona.edad>20:
            mayor_20.append(persona)
        else:
            menor_de_20.append(persona)

    return menor_de_20, mayor_20




class Menu:
    def __init__(self):
        #todo: definir el metodo init

    def choose_menu(self): # elegir menu
        # todo: definir una funcion que llame a un menu
