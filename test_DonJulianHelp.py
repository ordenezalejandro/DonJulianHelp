import os
import unittest
from interfaz import Interfaz
from unittest.mock import Mock, patch


class MyTestCase(unittest.TestCase):
    def tearDown(self) -> None:
        directory = os.path.split(__file__)[0]
        path_mueble = os.path.join(directory, 'data', 'test_1_de_Mueble.json')
        path_cliente = os.path.join(directory, 'data', 'test_1_de_Cliente.json')
        path_venta = os.path.join(directory, 'data', 'test_1_de_Venta.json')
        if os.path.exists(path_mueble):
            os.remove(path_mueble)
        if os.path.exists(path_cliente):
            os.remove(path_cliente)
        if os.path.exists(path_venta):
            os.remove(path_venta)

    def test_agregar_cliente(self):
        side_effect = [
            '1',
            'ordonez',
            'jairo',
            '31',
            'roberto sironi',
            '12'
        ]
        with patch('builtins.input', side_effect=side_effect):
            with Interfaz('test_1') as interfaz:
                interfaz.iniciar_programa()

        self.assertEqual(len(interfaz.registro_de_clientes), 1)

    def test_agregar_venta(self):
        side_effect = [
            '1',
            'ordonez',
            'jairo',
            '31',
            'roberto sironi',
            '3',
            'ordonez',
            'jairo',
            'cocina',
            'romana',
            '14000',
            '12-12-2023',
            '14000',
            '10000',
            'refaccion',
            '12'
        ]
        with patch('builtins.input', side_effect=side_effect):
            with Interfaz('test_1') as interfaz:
                interfaz.iniciar_programa()

        self.assertEqual(len(interfaz.registro_de_ventas), 1, 'La venta no fue agregada')
        self.assertEqual(len(interfaz.registro_de_muebles), 1, 'el mueble no fue agregado')
        self.assertEqual(len(interfaz.registro_de_clientes), 1, 'el cliente no fue agregado')


    def test_total_venta(self):
        side_effect = [
            '1',
            'ordonez', 'jairo', '31', 'roberto sironi',
            '3',
            'ordonez', 'jairo', 'cocina', 'romana', '10000'  '12-12-2023', '14000', '10000', 'refaccion',
            '3',
            'ordonez', 'jairo', 'mesa', 'romana', '10000', '12-12-2023', '16000', '10000', 'refaccion',
            '10',
            '12'
        ]
        with patch('builtins.input', side_effect=side_effect):
            with Interfaz('test_1') as interfaz:
                interfaz.iniciar_programa()
        self.assertEqual(interfaz.registro_de_ventas.total_de_ventas() == 30000, 'la suma no esta correcta')

    def test_agregar_venta_con_multiples_mubles(self):
        side_effect = datos_basicos() + [
            '3',
            'ordonez', 'jairo', 'cocina', 'romana', '1', 'no',
            '3',
            'ordonez', 'jairo', 'mesa', 'victoriana', '1', 'si', 'silla', 'victoriana', '6', 'no'
            '12',
        ]
        with patch('builtins.input', side_effect=side_effect):
            with Interfaz('test_1') as interfaz:
                interfaz.iniciar_programa()
        self.assertEqual(interfaz.registro_de_ventas.total_de_ventas() == 30000, 'la suma no esta correcta')


def datos_basicos():
    """ return una lista con muebles y cleintes cargados"""
    side_effect = [
        '1',
        'ordonez', 'jairo', '31', 'roberto sironi',
        '2',
        'cocina', 'romana', '1000',
        '2', 'mesa', 'victoriana', '20000',
        '2', 'silla', 'victoriana', '500'
    ]


if __name__ == '__main__':
    unittest.main()
