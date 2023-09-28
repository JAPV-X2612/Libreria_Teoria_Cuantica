# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/28

# Pruebas de la Libreria de Teoría Cuántica

from Libreria_Teoria_Cuantica import *
import unittest as ut

class Test_Libreria_Nombre(ut.TestCase):
    
    def test_Prob_Sist_Linea(self):
        """Prueba del calculo de la probabilidad de que una partícula esté en el punto xi de un vector de estados ψ
        None -> OK or FAILED (failures=#)"""
        prob = Prob_Sist_Linea([2-3j, 1+2j],1)        
        self.assertAlmostEqual(prob,0.277777777)
        prob = Prob_Sist_Linea([-1j, 2.5-3j, 6+2j, 5-9j, -1+2j],3)
        self.assertAlmostEqual(prob,0.633781763)


    def test_Prob_Trans_Est(self):
        """Prueba del calculo de la probabilidad de transitar de un vector de estados ψ a otro vector de estdos φ
        None -> OK or FAILED (failures=#)"""
        pte = Prob_Trans_Est([sqrt(2)/2j, -sqrt(2)/2], [sqrt(2)/2, sqrt(2)/2j])        
        self.assertAlmostEqual(pte, -1j)
        pte = Prob_Trans_Est([-1j, -5-3j, 6+2j, 5-7j], [2+2j, 3-1j, -1-1j, 4+3j])
        self.assertAlmostEqual(pte,(-0.2808849-0.6716813j))


if __name__ == '__main__':
    ut.main()