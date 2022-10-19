"""
este archivo contiene interfaz, con las siguientes funcionalidades
- iniciar programa
- imprimir menu
- leer comando
- ejecutar comando
- salir
"""
from copy import copy

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
    #     todo: implementar la funcion guardar muebles
    def ejecutar_comando(self,comando):

        if comando not in (1,2,3,4,5,6,7):

            self.comando_invalido()

        else:
            if comando == 1 :
                self.registro_de_clientes.agregar_input()

            if comando == 2:
                self.registro_de_muebles.agregar_input()
            #     falta metodo
            if comando == 3:
                self.registro_de_ventas.agregar_input()
            if comando == 4:
                self.registro_de_clientes.listar()
            if comando == 5:
                self.registro_de_muebles.listar()
            if comando == 6:
                self.registro_de_ventas.listar()
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
    comando = input("ingrese el comando:\n")
    if not comando.isdigit():
        return -1
    comando = int(comando) if comando else -1
    return comando

    pass

def flippingBits(n):
    # Write your code here
    bytes = []
    resto = n%2
    partial = n
    while partial > 0:
        bytes.append(resto)
        partial = partial//2
        resto = partial%2
    bytes.reverse()
    bytes = (32-len(bytes))*[0] + bytes
    result = 0
    bytes = list(map(lambda x: int(not(x)), bytes))
    for index, byte in enumerate(reversed(bytes)):
        result +=byte*(2**index)
    return result
import math
def primality(n):

    for num in range(1, int(math.isqrt(n)+1)):
        if n % int(num) == 0:
            return False
    return True


from functools import partial
from itertools import combinations, combinations_with_replacement
from collections import defaultdict


class Solution:
    def canPartitionKSubsets(self, nums, k):
        generate_subset = partial(combinations, nums)
        supersets = map(generate_subset, range(len(nums)))
        result = defaultdict(list)
        for subsets in supersets:
            for set_ in subsets:
                sum_ = sum(set_)

                result[sum_].append(set_)

        posibles = filter(lambda x: len(x) >= k, result.values())
        from collections import Counter
        for supersets in posibles:
            nums_ = Counter(copy(nums))
            acumulado = []
            for set_ in supersets:
                if set(set_).issubset(nums_.elements()):
                    nums_ -= Counter(set_)
                    acumulado.append(set_)

                if not nums_:
                    print(acumulado)
                    if len(acumulado) >= k:
                        # print(acumulado)
                        return True

        # print(acumulado)
        return False


class Solution2:
    def canPartitionKSubsets(self, nums, k) :

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum / k

        ks = [0] * k
        nums.sort(reverse=True)
        visited = [False] * len(nums)

        def can_partition(rest_k, cur_sum=0, next_index=0):
            if rest_k == 1:
                return True

            if cur_sum == subset_sum:
                return can_partition(rest_k - 1)

            for i in range(next_index, len(nums)):
                if not visited[i] and cur_sum + nums[i] <= subset_sum:
                    visited[i] = True
                    if can_partition(rest_k, cur_sum=cur_sum + nums[i], next_index=i + 1):
                        return True
                    visited[i] = False
            return False

        return can_partition(k)





import unittest
class test_fli(unittest.TestCase):

    def test_2(self):
        result = flippingBits(4)
        self.assertEqual(result, 4294967291)

    def test_prim(self):
        result = primality(1)
        self.assertEqual(True, result)

    def test_solucion(self):
        solucion = Solution()
        self.assertEqual(True, solucion.canPartitionKSubsets([1,1,1,1,2,2,2,2], 2))
        self.assertEqual(True, solucion.canPartitionKSubsets([1,1,1,1,2,2,2,2], 4))
        self.assertEqual(True, solucion.canPartitionKSubsets([2,6,16,13,3,4,1,1,2,12], 3))
        self.assertEqual(False, solucion.canPartitionKSubsets([1,1,1,1,9], 2))
        self.assertEqual(False, solucion.canPartitionKSubsets([1,2,3,4], 3))
        self.assertEqual(True, solucion.canPartitionKSubsets([1,1 ], 2))