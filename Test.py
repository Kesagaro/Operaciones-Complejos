import unittest
import Cplx
from math import pi
class CplxTest(unittest.TestCase):
    def test_sumcplx(self):
        a, b = (3, 2), (1, 4)
        result = Cplx.sumcplx(a, b)
        print ('Test suma =', result)

        a, b = (4, 6) , (-2, 5)
        result = Cplx.sumcplx(a, b)
        print('Test suma =', result)

    def test_prodcplx(self):
        a, b = (5, 5), (1, 4)
        result = Cplx.prodcplx(a, b)
        print ('Test producto =', result)

        a, b = (5, 2) , (-2, 5)
        result = Cplx.prodcplx(a, b)
        print('Test producto =', result)


    def test_rescplx(self):
        a, b = (7, -3), (5, 2)
        result = Cplx.rescplx(a, b)
        print ('Test resta =', result)

        a, b = (1, 2), (3, 4)
        result = Cplx.rescplx(a, b)
        print('Test resta =', result)


    def test_divcplx(self):
        a, b = (5, 4), (1, 3)
        result = Cplx.divcplx(a, b)
        print ('Test division =', result)

        a, b = (4, 3), (2, 5)
        result = Cplx.divcplx(a, b)
        print('Test division =', result)

    def test_modcplx(self):
        a = (2.4, 4)
        result = Cplx.modcplx(a)
        print ('Test modulo =', result)

        a = (3.1 , 5)
        result = Cplx.modcplx(a)
        print ('Test modulo =', result)


    def test_conjcplx(self):
        a = (2, 5)
        result = Cplx.conjcplx(a)
        print ('Test conjugado =', result)

        a = (1, 3)
        result = Cplx.conjcplx(a)
        print('Test conjugado =', result)



    def test_polcplx(self):
        a = (1.8, 4)
        result = Cplx.polcplx(a)
        print ('Test cartesiano a polar =', result)

        a = (2.4, 6)
        result = Cplx.polcplx(a)
        print('Test cartesiano a polar =', result)

    def test_carcplx(self):
        a = (6.15, pi/3)
        result = Cplx.carcplx(a)
        print ('Test cartesiano a polar =', result)

        a = (7.11, pi/4)
        result = Cplx.carcplx(a)
        print('Test cartesiano a polar =', result)

    def test_fasecplx(self):
        a = (2.8, 7)
        result = Cplx.fasecplx(a)
        print ('Test retornar fase =', result)

        a = (3.1, 5)
        result = Cplx.fasecplx(a)
        print('Test retornar fase =', result)
