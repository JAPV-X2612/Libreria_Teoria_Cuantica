# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/28

# Libreria de Teoría Cuántica

from numpy import *
from math import *

def Normal_Vect(v):
    """Calcula y devuelve la normalización de un vector dado
    (1D array) -> 1D array"""
    v = array(v)
    vn = (1/linalg.norm(v))*v
    return vn


def cplx_vct_mtx_adj(vm):
    """Calcula y devuelve la adjunta (daga) de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vm = array(vm)
    vma = transpose(conjugate(vm))
    return vma


def cplx_vct_mtx_inter_prod(vm1,vm2):
    """Calcula y devuelve el producto interno de dos vectores o matrices complejos
    (1D array, 1D array or 2D array, 2D array) -> 1D array or 2D array or int or float"""
    try:
        vm1,vm2 = array(vm1),array(vm2)
        d1 = vm1.ndim
        d2 = vm2.ndim
        if d1 == 1 == d2:
            vip = dot(cplx_vct_mtx_adj(vm1),vm2)
            return vip
        elif vm1.shape[0] == vm2.shape[0]:
            mip = trace(dot(cplx_vct_mtx_adj(vm1),vm2))
            return mip
        else:
            return "Los vectores o matrices NO son compatibles"
    except:
        return "Los vectores o matrices NO son compatibles"


def Prob_Sist_Linea(ψ,xi):
    """Calcula y devuelve la probabilidad de que una partícula esté en el punto xi de un vector de estados |ψ⟩
    (1D array, ) -> float"""
    ψ = array(ψ)
    prob = (linalg.norm(ψ[xi]))**2/(linalg.norm(ψ))**2
    return prob


def Prob_Trans_Est(ψ,φ):
    """Calcula y devuelve la probabilidad de transitar de un vector de estados |ψ⟩ a otro vector de estdos |φ⟩
    (1D array, 1D array) -> float"""
    ψ,φ = array(ψ),array(φ)
    ψ,φ = Normal_Vect(ψ),Normal_Vect(φ)
    braφ = transpose(conjugate(φ))
    at = dot(braφ,ψ)
    pte = linalg.norm(at)**2
    return pte


def Ampli_Trans_(ψ,φ):
    """Calcula y devuelve la amplitud de transición de un vector de estados |ψ⟩ a otro vector de estdos |φ⟩
    (1D array, 1D array) -> complex"""
    ψ,φ = array(ψ),array(φ)
    ψ,φ = Normal_Vect(ψ),Normal_Vect(φ)
    braφ = transpose(conjugate(φ))
    at = dot(braφ,ψ)
    return at


def Val_Esp_Var(Ω,ψ):
    """Calcula y devuelve el valor esperado y la varianza de un experimento después de aplicar una matriz Ω que describe un observable sobre un vector de estados |ψ⟩
    (2D array, 1D array) -> float, float"""
    Ω,ψ = array(Ω),array(ψ)
    ψ = Normal_Vect(ψ)
    
    if cplx_herm_mtx(Ω) == False:
        return "El observable NO es una matriz hermitiana"
    else:
        I = identy(len(Ω))
        veΩψ = cplx_vct_mtx_inter_prod(dot(Ω,ψ),ψ)
        ΔψΩ = Ω-dot(veΩψ,I)
        varψΩ = cplx_vct_mtx_inter_prod(dot(ΔψΩ,ψ),ψ)
        
    return veΩψ,varψΩ


def cplx_herm_mtx(m):
    """Indica si una matriz compleja es hermitiana
    (2D array) -> True or False"""
    m = array(m)
    a,b = m.shape
    if a == b:
        hm = [list(x) for x in m]
        hmt = [list(x) for x in cplx_vct_mtx_adj(m)]
        if  hm == hmt:
            return True
        else:
            return False
    else:
        return "La matriz NO es cuadrada"