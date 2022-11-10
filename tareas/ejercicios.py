from ModeladoDonJulian import Extra, Pieza, Mueble
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


class Num:

    def __init__(self,numero,lista_de_numeros):
        self.numero = numero
        self.lista_de_numeros = lista_de_numeros

    def sumatoria(self):

        sumatoria_de_numeros = 0

        for numero in lista_de_numeros: # Todo: que es lista_de_numero, a domnde esta declarada

            numero = numero

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

def editar_informacion(self):

# pedimos informacion
# preguntamos que dato informacion/dato quiere cambiar
# actualizamos la informacion
# preguntamos si desea hacer algun cambio mas
# retornamos la informacion actualizada
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

    while

        # print(f'Solicitando datos para registrarlo')
        # pasamos los datos basicos que pedimos, y pedimos el resto.
        parametros = self.pedir_informacion_completa_input(parametros)
    # instanciamos la clase con todo los datos que ya habiamos encontrados
    nueva_instancia = self.clase(**parametros)
    self.get_diccionario()[clave] = nueva_instancia
    self.guardar()
    self.cargar()
    return nueva_instancia


