from ModeladoDonJulian import Mueble,Pieza, Extra, Cliente, Venta, RegistroDeVentas, RegistroDeClientes
from ejercicios import total_componentes
from unittest.mock import patch
from datetime import datetime
import unittest

class Test_total_de_componente(unittest.TestCase):
    def test_total_compónente(self):
        """
        tomar lista_de_pieza mas lista_extra y me retorna el total de elementos de ambas listas
        """

        lista_de_piezas = []
        estante = Pieza(50, 30, 2, 'estante')
        puerta = Pieza(58, 35, 2.3, 'puerta bajo')
        zocalo = Pieza(7, 200, 2, 'zocalo bajo')

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
        self.assertEqual(6,total_componentes(lista_de_piezas,lista_extra),'no corresponde')

    def test_agregar_pieza(self):
        cajonera = Mueble('cajonera','6 cajones',precio = 1)

        self.assertEqual(0,len(cajonera.lista_de_piezas))
        estante = Pieza(2,4,1,'estante cajonera')

        cajonera.agregar_pieza(estante)
        self.assertEqual(1,len(cajonera.lista_de_piezas), 'no se pudo agregar la pieza, de forma correcta')

    def test_agregar_extra(self):
        cajonera = Mueble('cajonera','6 cajones',1)

        bisagra = Extra('bisagra','codo 9')
        cajonera.agregar_extra(bisagra)

        self.assertEqual(1,len(cajonera.lista_extra),'no se agrego a la lista extra')

    def test_mueble(self):
        cajonera = Mueble('cajonera','6 cajones',2)
        costado = Pieza(11,22,1,'costado cajon')
        cajonera.agregar_pieza(costado)

        guias = Extra('guias', 'telescopicas 35cm')

        cajonera.agregar_extra(guias)

        self.assertEqual(2, len(cajonera.lista_de_piezas) + len(cajonera.lista_de_extras), 'no se agregaron las piezas a las listas')
        extra = cajonera.lista_de_extras[0]

        self.assertEqual(Extra, type(extra), 'la lista contiene elementos que no son del tipo extra')

    def test_agregar_cliente(self):
        nuevo_cliente = Cliente(nombre='prueba', apellido='ordonez')
        self.assertTrue(nuevo_cliente != None)
        self.assertEqual(nuevo_cliente.nombre, 'prueba', 'deberia ser el mismo nombre')
        self.assertEqual(nuevo_cliente.apellido, 'ordonez', 'deberia ser el mismo apellido')
        cliente2 = Cliente('Alejando', 'ordonez')
        cliente2.telefono = '484934304343'
        self.assertEqual(cliente2.telefono , '484934304343', 'deberia poder pasar el telefono' )
        # self.assertEqual(nuevo_c)
        # cliente2 = Cliente(nombre="segundo")
        #

    def test_venta(self):
        new_cliente = Cliente('alejandro', 'ordonez')
        cocina = Mueble('cocina', 'larga',9)
        nueva_venta = Venta()
        nueva_venta.poner_cliente(new_cliente) # setear
        nueva_venta.poner_mueble(cocina)
        nueva_venta.poner_motivo('renovacion')
        nueva_venta.poner_precio(4000.50)
        nueva_venta.adelanto = 2000.50
        self.assertEqual(nueva_venta.calcular_saldo(), 2000.00, 'no resto el adelanto de la venta')
        # self.assertEqual(nueva_venta.ingreso , datetime.today())

    def test_listar_ventas(self):
        jairo = Cliente('Jairo', 'Ordonez')
        ale = Cliente('alejandro', 'Ordonez')
        cocina = Mueble('cocina', 'cocina moderna',100)
        cama = Mueble('cama', 'Cama de dos plaza',200)

        registro_de_ventas = RegistroDeVentas()

        nueva_venta = Venta()
        nueva_venta.poner_cliente(jairo)
        nueva_venta.poner_mueble(cocina)
        registro_de_ventas.agregar_venta(nueva_venta)

        otra_venta = Venta()
        otra_venta.poner_cliente(ale)
        otra_venta.poner_mueble(cama)

        registro_de_ventas.agregar_venta(otra_venta)
        self.assertEqual(2, registro_de_ventas.devolver_cantidad_ventas())
        valor_esperado = '\n'.join(['Nombre completo: Jairo Ordonez, Mueble: Cocina',
                                   'Nombre completo: alejandro Ordonez, Mueble: cama'])
        from io import StringIO
        with patch('sys.stdout', new=StringIO()) as fake_out:
            registro_de_ventas.listar_ventas()
            self.assertEqual(fake_out.getvalue(), valor_esperado)

    # # crear un test, que se llama test_devolver_costo_de_mueble
    # # el test. debe instanciar un mueble, agregarle
    # # 2  piezas, 2 extra . con sus respectivo precio

    def test_devolver_costo_de_mueble(self):
        cocina = Mueble('cocina', '1.20, 4 cajones',1500)
        frente_cajon = Pieza(15, 45, 2, 'frente cajon',5)
        costado_cajon = Pieza(15, 45, 2, 'costado cajon',5)
        guia = Extra('guia_cajon','telescopica_45', 15)
        tornillo = Extra('tornillo','telescopica_45', 15)

        cocina.agregar_pieza(frente_cajon)
        cocina.agregar_pieza(costado_cajon)
        cocina.agregar_extra(guia)
        cocina.agregar_extra(tornillo)

        #e implementar un metodo en mueble que
        # calcule el precio del mueble, para eso
        # debe sumar el precio ,de todos sus piezas y
        # sus extras

        self.assertEqual(40,cocina.devolver_costo_de_mueble(),'no se calculo bien el costo')

    #@patch('builtins.input', side_efect=['ordonez', 'jairo', '35'])
    def test_guardar_cliente(self):
        registro_cliente = RegistroDeClientes()
        self.assertEqual(2, len(registro_cliente.lista_de_clientes))
        jairo = Cliente('jairo', 'ordonez' , 35)
        ale = Cliente('alejandro', 'ordonez',38)
        registro_cliente.agregar_cliente(jairo)
        registro_cliente.agregar_cliente(ale)
        registro_cliente.guardar_cliente()
        clientes = registro_cliente.cargar_cliente()
        self.assertEqual(len(clientes), 2, 'No esta cargando todos los datos')



if __name__ == '__main__':
    unittest.main()

#
# """ale = Cliente('alejandro', 'Ordonez','cajonera','12/1/2022',27/12/2022 )
# thiago = Cliente('thiago','ordonez','cama',1/3/2020,25/3/2022)
# juli = Cliente ('juli','ordonez','placard',5/8/2020,5/4/2022)"""

# crear un meteodo en la clase RegistroDeVenta
# llamado , devolver_las_ventas_de , y que tome
# como parametro , el nombre del cliente , y apellido,
# y devuelva , una lista con las ventas que coincidan
# con en el nombre y apellid

# Definir un metodo _eq_ en la clase cliente,
# que tome como parámetro , otro cliente,
# y devuelve True si  el nombre y apellido del cliente
# es igual al otro cliente

# definir metodo en la clase RegistroDeCliente
# llamada agregar_cliente_input

# Jairo ordoñez21:44
# esta funcion no toma parametro (solo el self),
# y pide al usuario un nombre(usar la funcion input),
# un apellido, edad, y crea una instancia de cliente,
# y luego usa la funcion agregar_cliente con la nueva
# instancia creada

# crear un metodo en la calse REgistro cliente,
# que se llame guardar_cliente, que no tome argumento,
# y  guarde el atributo, lista_cliente en un json ,
# crear un metodo en la clase registtro_cleite,
# que se lla,e cargar_Cleinte,
# y que lea el json y lo asigne a lista_cliete

# cocina = Mueble('cocina','1.20, 4 cajones',122)
# frente_cajon = Pieza(15,45,2)
# costado_cajon = Pieza(11,45,2)
# contra_frente = Pieza(7,45,2)

# cocina = Mueble('cocina','1.20, 4 cajones',122)
# frente_cajon = Pieza(15,45,2,'frente cajon')
# costado_cajon = Pieza(11,45,2,'costado cajon')
# contra_frente = Pieza(7,45,2,'contra frente')

# crear una funcion llamada sumatoria, que tome
# una lista de numeros, y sume su total
#
# ejemplo
# sumatoria([1,2,2,5])
# == 10
#
# sumatora([])
# ==0
#
#
# crear una funcion llamada productoria. que tome
# una lista de numeros enteros y devueva el producto
# de todos sus numeros
#
#
# ejemplos
# productoria([1,1,1,1])
#  == 1
# productoria([1,2,3,4])
# 24

# recorre la lista
# compara 2 elementos
#lo guarda en 1 lista
# vuelve a comparar
# si el elemento es menor al ya seleccionado termina

# toma una lista de elementos,
# devueleve 2 listas de elementos
# ina lista con elmentos pares
# la otra con los impares

# crear un test, que se llama test_precio_mueble
# el test. debe instanciar un mueble, agregarle
# 2  piezas, 2 extra . con sus respectivo precio