# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/28

# Libreria de Teoría Cuántica

from numpy import *
from copy import *
from math import *

def Normal_Vect(v):
    """Calcula y devuelve la normalización de un vector dado
    (1D array) -> 1D array"""
    v = array(v)
    vn = (1/linalg.norm(v))*v
    return vn


def Prob_Sist_Linea(ψ,xi):
    """Calcula y devuelve la probabilidad de que una partícula esté en el punto xi de un vector de estados ψ
    (1D array, ) -> 1D array"""
    ψ = array(ψ)
    prob = (linalg.norm(ψ[xi]))**2/(linalg.norm(ψ))**2
    return prob


def Prob_Trans_Est(ψ,φ):
    """Calcula y devuelve la probabilidad de transitar de un vector de estados ψ a otro vector de estdos φ
    (1D array) -> 1D array"""
    ψ,φ = array(ψ),array(φ)
    ψ,φ = Normal_Vect(ψ),Normal_Vect(φ)
    braφ = transpose(conjugate(φ))
    pte = dot(braφ,ψ)
    return pte