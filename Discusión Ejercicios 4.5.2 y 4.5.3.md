# Discusión Ejercicios 4.5.2 y 4.5.3

**ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO**  
**Carrera / Semestre:** Ingeniería de Sistemas / 4to Semestre  
**Asignatura:** Ciencias Naturales y Tecnología (CNYT)  
**Nombre:** Jesús Alfonso Pinzón Vega  
**Fecha:** 2023/09/28  

### 1. Solución del Ejercicio 4.5.2
**Enunciado:** Escriba el vector de estados genérico para un sistema de dos partículas con giro. Generalícelo a un sistema con n partículas (esto es importante: ¡será la realización física de los registros cuánticos!).

Para solucionar este ejercicio, primeramente se muestra a continuación el vector de estados genérico para un sistema de dos partículas:

|ψ⟩ₓ = b₀|x₀⟩ + b₁|x₁⟩ + ... + bₙ₋₁|xₙ₋₁⟩  
|ψ⟩ᵧ = c₀|y₀⟩ + c₁|y₁⟩ + ... + cₙ₋₁|yₙ₋₁⟩  

|ψ⟩ = |ψ⟩ₓ⊗|ψ⟩ᵧ = (b₀|x₀⟩ + b₁|x₁⟩ + ... + bₙ₋₁|xₙ₋₁⟩)⊗(c₀|y₀⟩ + c₁|y₁⟩ + ... + cₙ₋₁|yₙ₋₁⟩)  
**|ψ⟩ = b₀c₀|x₀⟩⊗|y₀⟩ + ... + bᵢcⱼ|xᵢ⟩⊗|yⱼ⟩ + ... + cₙ₋₁bₘ₋₁|xcₙ₋₁⟩⊗|yₘ₋₁⟩**  

Y ahora para n partículas, el vector de estados genéerico es el siguiente:

|ψ⟩ₚ₀ = a₀,₀|x₀,₀⟩ + ... + a₀,ᵢ|x₀,ᵢ⟩ + ... + a₀,ₘ₋₁|x₀,ₘ₋₁⟩  
|ψ⟩ₚ₁ = a₁,₀|x₁,₀⟩ + ... + a₁,ᵢ|x₁,ᵢ⟩ + ... + a₁,ₘ₋₁|x₁,ₘ₋₁⟩  
  ፧   =     ፧      + ... +     ፧      + ... +       ፧          
|ψ⟩ₚₙ₋₁ = aₙ₋₁,₀|xₙ₋₁,₀⟩ + ... + aₙ₋₁,ᵢ|xₙ₋₁,ᵢ⟩ + ... + aₙ₋₁,ₘ₋₁|xₙ₋₁,ₘ₋₁⟩  

|ψ⟩ = |ψ⟩ₚ₀⊗|ψ⟩ₚ₁⊗...⊗|ψ⟩ₚₙ = (a₀,₀|x₀,₀⟩ + ... + a₀,ᵢ|x₀,ᵢ⟩ + ... + a₀,ₘ₋₁|x₀,ₘ₋₁⟩)⊗(a₁,₀|x₁,₀⟩ + ... + a₁,ᵢ|x₁,ᵢ⟩ + ... + a₁,ₘ₋₁|x₁,ₘ₋₁⟩)⊗...⊗(aₙ₋₁,₀|xₙ₋₁,₀⟩ + ... + aₙ₋₁,ᵢ|xₙ₋₁,ᵢ⟩ + ... + aₙ₋₁,ₘ₋₁|xₙ₋₁,ₘ₋₁⟩)  
**|ψ⟩ = a₀,₀a₁,₀...aₙ₋₁,₀|x₀,₀⟩⊗|x₁,₀⟩⊗...⊗|xₙ₋₁,₀⟩ + ... + a₀,ᵢa₁,ᵢ...aₙ₋₁,ᵢ|x₀,ᵢ⟩⊗|x₁,ᵢ⟩⊗...⊗|xₙ₋₁,ᵢ⟩ + ... + a₀,ₘ₋₁a₁,ₘ₋₁...aₙ₋₁,ₘ₋₁|x₀,ₘ₋₁⟩⊗|x₁,ₘ₋₁⟩⊗...⊗|xₙ₋₁,ₘ₋₁⟩**  


### 2. Solución del Ejercicio 4.5.3
**Enunciado:** Asumir el mismo escenario del ejemplo 4.5.2 con |φ⟩ = |x₀⟩⊗|y₁⟩ + |x₁⟩⊗|y₁⟩.

Para dar solución a este ejercicio, se procede a seguir las mismas instrucciones de ejemplo 4.5.2, el cual trata de averiguar si se puede expresar un vector de estados de dos partículas como el producto tensor de los vectores de estados de cada una.

Para ello, se construyen las siguientes ecuaciones: 

1) |φ⟩ = |x₀⟩⊗|y₁⟩ + |x₁⟩⊗|y₁⟩ = **0**|x₀⟩⊗|y₀⟩ + **1**|x₀⟩⊗|y₁⟩ **0**|x₁⟩⊗|y₀⟩ + **1**|x₁⟩⊗|y₁⟩  
2) |ψ⟩ₓ = b₀|x₀⟩ + b₁|x₁⟩  
3) |ψ⟩ᵧ = c₀|y₀⟩ + c₁|y₁⟩  
4) |ψ⟩ₓ⊗|ψ⟩ᵧ = (b₀|x₀⟩ + b₁|x₁⟩)⊗(c₀|y₀⟩ + c₁|y₁⟩) = **b₀c₀**|x₀⟩⊗|y₀⟩ + **b₀c₁**|x₀⟩⊗|y₁⟩ **b₁c₀**|x₁⟩⊗|y₀⟩ + **b₁c₁**|x₁⟩⊗|y₁⟩  

Luego, se crea el siguiente sistema de ecuaciones:

* b₀c₀ = 0  
* b₀c₁ = 1  
* b₁c₀ = 0  
* b₁c₁ = 1  

Y cómo el sistema NO tiene solución, se concluye que ***el vector de estados NO puede ser escrito como el producto tensor de los vectores de estado de cada partícula por separado***; en otras palabras, esto quiere decir que las partículas están entralazadas cuánticamente.