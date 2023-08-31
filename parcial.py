import math

# función para calcular la distancia entre dos puntos en el plano
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# decorador para ordenar los puntos por coordenadas
def ordenar_puntos_decorator(func):
    def wrapper(*args, **kwargs):
        puntos_ordenados_por_x = sorted(args[0], key=lambda p: p[0])
        return func(puntos_ordenados_por_x, **kwargs)
    return wrapper

# función para encontrar los pares más cercanos en un conjunto de puntos
@ordenar_puntos_decorator
def encontrar_pares_cercanos(puntos, **kwargs):
    if len(puntos) < 2:
        return None
    
    min_distancia = float('inf')  # Valor inicial muy grande para comparar distancias
    par_mas_cercano = None
    
    # Recorremos todas las combinaciones de pares posibles
    for i in range(len(puntos)):
        for j in range(i+1, len(puntos)):
            dist = distancia(puntos[i], puntos[j])  # Calculamos la distancia
            if dist < min_distancia:  # Si encontramos una distancia más corta
                min_distancia = dist
                par_mas_cercano = (puntos[i], puntos[j], min_distancia)
    
    return par_mas_cercano

puntos = [(1, 2), (4, 6), (3, 8), (9, 12), (10, 5)]
resultado = encontrar_pares_cercanos(puntos)
    

print("Pares más cercanos:", resultado[:2]) 
print("Distancia:", resultado[2])  