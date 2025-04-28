# Importamos el módulo math para usar el valor de pi
import math

# 1) Establecer el modelo matemático
# El sólido está compuesto por:
# a) Mitad de una esfera (una semiesfera).
# b) Un cono unido a esa semiesfera.
# Volumen total=Volumen semiesfera+Volumen del cono
# volumen de una esfera completa es: V_esfera = 4/3(pi)(r_1)^3
# El volumen de un cono es: V_cono = 1/3(pi)(r_2)^2(h)
# V_total = 4/3(pi)(r_1)^3 + 1/3(pi)(r_2)^2(h)
2# Defino la duncion de V_total
def v_total(r_1, r_2, h):
    """
    Parámetros:
    r_1 = radio de la esfera
    r_2 = radio de la base del cono
    h = altura del cono
    Retorna:
    Volumen total del sólido.
    """
    # Volumen de la esfera completa
    v_esfera = (4/3) * math.pi * (r_1**3)
    # Volumen del cono
    v_cono = (1/3) * math.pi * (r_2**2) * h
    # Volumen total
    v_total = v_esfera + v_cono
    return v_total
# 3) Planteo los valores dados por el porblema: 
# r_1 = 3 
# r_2 = 4
# h = 9/2  
# uso la funcion igresando los valores dados
r1 = 3
r2 = 4
h = 9/2 

# calcular el volumen
volumen = v_total(r1, r2, h)
# Imprimir el resultado
print("el Volumen total del la esfera y el cono es de ")
print(volumen)


# 1) Área Total del vagon y los dos ciruclos es: (b * a) + 2(pi * r^2)
# se define  la función para calcular el área total
def area_total_vagon(a, b, r):
    """
    Parámetros:
    a = altura del vagón
    b = largo del vagón
    r = radio de las rueda
    Retorna:
    Área total del vagón.
    """
    # Área del rectángulo
    a_rectangulo = b * a
    # Área de dos círculos
    a_circulos = 2 * math.pi * (r**2)
    # Área total
    a_total = a_rectangulo + a_circulos
    return a_total
# Ejemplo con valores arbitrarios
a = 2  # altura del vagón
b = 5  # largo del vagón
r = 1  # radio de las ruedas
# Calcular el área total
area = area_total_vagon(a, b, r)
# Imprimir el resultado
print("El area total del vagon y los ciruclos es de ")
print(area)

# 2) Área Total de los vagones y los dos ciruclos es: (b_1​ * a_1​) + (b_2​ * a_2​) + (pi * r_1^2​) + (pi * r_2^2​)

# Función para calcular el área de un círculo cualquiera
def area_circulo(r):
    return math.pi * (r ** 2)

# Función para calcular el área de un rectángulo cualquiera
def area_rectangulo(b, a):
    return b * a

# Función para sumar dos números
def suma(x, y):
    return x + y

# Función principal usando una composición de funciones
def area_total_carro(a_1, b_1, a_2, b_2, r_1, r_2):
    """
    Parámetros:
    a_1 = altura del primer rectángulo
    b_1 = base del primer rectángulo
    a_2 = altura del segundo rectángulo
    b_2 = base del segundo rectángulo
    r_1 = radio de la primera rueda
    r_2 = radio de la segunda rueda
    Retorna:
    Área lateral total del carro.
    """
    # Área de los rectángulos
    area_rect1 = area_rectangulo(b_1, a_1)
    area_rect2 = area_rectangulo(b_2, a_2)
    
    # Área de las ruedas
    area_cir1 = area_circulo(r_1)
    area_cir2 = area_circulo(r_2)
    
    # Sumar todas las áreas
    area_total = suma(suma(area_rect1, area_rect2), suma(area_cir1, area_cir2))
    
    return area_total
# Ejemplo con valores arbitrarioa
a_1 = 3  
b_1 = 6 
a_2 = 2 
b_2 = 5  
r_1 = 1  
r_2 = 1  

# Calcular el área total
area = area_total_carro(a_1, b_1, a_2, b_2, r_1, r_2)
# Imprimir resultado
print("El area total de los dos vagonoes y los circulos es de ")
print(area)

# 1) problema 1. 
# Funcion para calcular carne de aves en kilos  total_kilos= (N * 6 ) + (M * 7) + (K * 1)
def carne_aves(N, M, K):
    """
    Parámetros:
    N = número de gallinas
    M = número de gallos
    K = número de pollitos
    Retorna:
    Total de kilos de carne.
    """
    total_kilos = (N * 6) + (M * 7) + (K * 1)
    return total_kilos

# 2) Problema 2: Compra de pan, leche y huevos
# total_compra = (P * 300) + (M * 3300) + (H * 350)  
# Vueltas = 𝐵 − total_compra
def vueltas_compra(P, M, H, B):
    """
    Calcula las vueltas o la deuda después de una compra.
    Parámetros:
    P = número de panes
    M = número de bolsas de leche
    H = número de huevos
    B = valor del billete entregado
    Retorna:
    Cantidad de vueltas (positiva) o deuda (negativa).
    """
    total_compra = (P * 300) + (M * 3300) + (H * 350)
    vueltas = B - total_compra
    return vueltas
# 3) Problema 3: Interés compuesto préstamo. Me prestan P pesos con un interes del 3%
# Monto = P * ( 1 + 0.03)^2
def prestamo(P):
    """
    Parámetros:
    P = cantidad prestada
    Retorna:
    Monto a pagar al final del segundo mes.
    """
    monto = P * (1 + 0.03)**2
    return monto
# 4) Problema 4: Contagiados de Covid-19 
# Número de contagiados se duplica cada día. 
# # Número inicial de contagiados C.
# contagiados= C * 2^D

def contagios(C, D):
    """
    Parámetros:
    C = número inicial de contagiados
    D = número de días
    Retorna:
    Número de contagiados después de D días.
    """
    total_contagiados = C * (2 ** D)
    return total_contagiados


# Ejemplos de cada función

# 1. Carne de aves
print ("La catidad de carne de aves en kilos es de ")
print(carne_aves(2, 1, 5)) 

# 2. Vueltas de la compra
print ("las vueltas son de  ")
print(vueltas_compra(3, 1, 12, 50000))  

# 3. Préstamo
print ("lo que debo pagar el segundo mes si mi prestamo fueron 100000 es de  ")
print(prestamo(100000))  # 

# 4. Contagiados
print ("el Numero de contagios es de 5 días es ")
print(contagios(100, 5))  # 100 contagiados al día 0, calcular al día 5
