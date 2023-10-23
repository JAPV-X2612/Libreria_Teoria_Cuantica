# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/28

# Pruebas de la Libreria de Teoría Cuántica

from Libreria_Teoria_Cuantica import *
import unittest as ut

class Test_Libreria_Teoria_Cuantica(ut.TestCase):
    
    def test_Prob_Sist_Linea(self):
        """Prueba del calculo de la probabilidad de que una partícula esté en el punto xi de un vector de estados |ψ⟩
        None -> OK or FAILED (failures=#)"""
        prob = Prob_Sist_Linea([2-3j, 1+2j], 1)        
        self.assertAlmostEqual(prob, 0.277777777)
        prob = Prob_Sist_Linea([-1j, 2.5-3j, 6+2j, 5-9j, -1+2j], 3)
        self.assertAlmostEqual(prob, 0.633781763)
        prob = Prob_Sist_Linea([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], 7)
        self.assertAlmostEqual(prob, 0.108695652)
        

    def test_Prob_Trans_Est(self):
        """Prueba del calculo de la probabilidad de transitar de un vector de estados |ψ⟩ a otro vector de estdos |φ⟩
        None -> OK or FAILED (failures=#)"""
        pte = Prob_Trans_Est([sqrt(2)*1j/2, -sqrt(2)/2], [sqrt(2)/2, sqrt(2)*1j/2])        
        self.assertAlmostEqual(pte, 1)
        pte = Prob_Trans_Est([-1j, -5-3j, 6+2j, 5-7j], [2+2j, 3-1j, -1-1j, 4+3j])
        self.assertAlmostEqual(pte, 0.530052199)
        pte = Prob_Trans_Est([1,0,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0,0])
        self.assertAlmostEqual(pte, 0)


    def test_Ampli_Trans(self):
        """Prueba del calculo de la amplitud de transición de un vector de estados |ψ⟩ a otro vector de estdos |φ⟩
        None -> OK or FAILED (failures=#)"""
        at = Ampli_Trans([1,-1j],[1j,1])
        self.assertAlmostEqual(at, -1j)
        at = Ampli_Trans([2+5j,-2,-1+5j],[3j,4+1j,6])
        self.assertAlmostEqual(at, 0.0165340082+0.4298842139j)


    def test_Val_Var(self):
        """Prueba del calculo del valor esperado y la varianza de un experimento después de aplicar una matriz Ω que describe un observable sobre un vector de estados |ψ⟩
        None -> OK or FAILED (failures=#)"""
        val,var = Val_Var([[1,-1j],[1j,2]],[sqrt(2)/2,sqrt(2)*1j/2])
        val,var = round(val.real,3),round(var.real,3)
        self.assertAlmostEqual(val, 2.5)
        self.assertAlmostEqual(var, 0.25)
        val,var = Val_Var([[1,1j,-2j],[-1j,2,1+1j],[2j,1-1j,3]],[2j,-3,1j])
        val,var = round(val.real,3),round(var.real,3)
        self.assertAlmostEqual(val, 1.357)
        self.assertAlmostEqual(var, 6.444)
        
    
    def test_Colap_Sist(self):
        """Prueba del calculo de la probabilidad de que un sistema colapse de un vector de estados |ψ⟩ a cada uno de los vectores propios |e⟩ de un observable Ω si el resultado de la medición fue su correspondiente valor propio λ
        None -> OK or FAILED (failures=#)"""
        prob = Colap_Sist([[-1,-1j],[1j,1]],[1/2,1/2])
        self.assertAlmostEqual(prob[0], 0.5)
        self.assertAlmostEqual(prob[1], 0.5)
        prob = Colap_Sist([[2,1+1j],[1-1j,0]],[1j,1])
        self.assertAlmostEqual(prob[0], 0.788675135)
        self.assertAlmostEqual(prob[1], 0.211324865)
        
    
    def test_Dina_Sist(self):
        """Prueba del calculo del estado final |φ⟩ que resulta del producto de n matrices unitarias y de un estado inicial |ψ⟩
        None -> OK or FAILED (failures=#)"""
        φ = Dina_Sist([[[1,0],[0,1]],[[0,1],[1,0]],[[0,-1j],[1j,0]]],[1,0])
        self.assertEqual(list(φ),[-1j,0])
        φ = Dina_Sist([[[1,0],[0,-1]],[[0,1j],[-1j,0]],[[0,-1j],[1j,0]]],[1,1])
        self.assertEqual(list(φ),[-1,1])
    
    
    def test_Exercise_4_3_1(self):
        """Prueba de los resultados del ejercicio 4.3.1 del texto guía
        None -> OK or FAILED (failures=#)"""
        h_bar = 1.054571817e-34
        hx = [[0,1],[1,0]]
        hx = (h_bar/2)*array(hx)
        val,vect = cplx_mtx_val_vect(hx)
        vect = [list(x) for x in vect]
        self.assertEqual(vect[0],[0.7071067811865475, -0.7071067811865475])
        self.assertEqual(vect[1],[0.7071067811865475, 0.7071067811865475])
        
        
    def test_Exercise_4_3_2(self):
        """Prueba de los resultados del ejercicio 4.3.2 del texto guía
        None -> OK or FAILED (failures=#)"""
        h_bar = 1.054571817e-34
        ψ = [1/2,1/2]
        hx = [[0,1],[1,0]]
        hx = (h_bar/2)*array(hx)
        val,vect = cplx_mtx_val_vect(hx)
        vect = [list(x) for x in vect]
        prob = Colap_Sist(hx,ψ)
        vpd = 0
        for n in range(len(prob)):
            vpd += prob[n]*val[n]
        self.assertAlmostEqual(vpd,0)
        
    
    def test_Exercise_4_4_1(self):
        """Prueba de los resultados del ejercicio 4.4.1 del texto guía
        None -> OK or FAILED (failures=#)"""
        U1 = [[0,1],[1,0]]
        U2 = [[sqrt(2)/2,sqrt(2)/2],[sqrt(2)/2,-sqrt(2)/2]]
        U3 = dot(array(U1),array(U2))
        v1,v2,v3 = cplx_unt_mtx(U1),cplx_unt_mtx(U2),cplx_unt_mtx(U3)
        self.assertEqual(v1,True)
        self.assertEqual(v2,True)
        self.assertEqual(v3,True)
        
        
    def test_Exercise_4_4_2(self):
        """Prueba de los resultados del ejercicio 4.4.2 del texto guía
        None -> OK or FAILED (failures=#)"""
        ψ = [1,0,0,0]
        Ω = [[0,1/sqrt(2),1/sqrt(2),0],[1j/sqrt(2),0,0,1/sqrt(2)],[1/sqrt(2),0,0,1j/sqrt(2)],[0,1/sqrt(2),-1/sqrt(2),0]]
        Ω3 = Mult_Clics(Ω,3)
        φ = dot(Ω3,array(ψ))
        prob = Prob_Sist_Linea(φ,3)
        self.assertAlmostEqual(prob,0)
            

if __name__ == '__main__':
    ut.main()