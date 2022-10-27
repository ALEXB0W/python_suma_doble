# ========================================
# Solución forzada.
# ========================================

'''
nums = [2, 7, 11, 15]
numero = 9

def sumar_numero_lista(vector, target):
    for i in range(len(vector)):
        for j in range(len(vector)):
            if i != j and vector[i] + vector[j] == target:
                return {i,j}

print(sumar_numero_lista(nums, numero))
'''

# ========================================
# Solución en tiempo "n" y memoria "n".
# nums = [2, 7, 11, 15]
# mapa = [7:0, 2:1, -2:2, -6:3]
# ========================================

nums = [2, 7, 11, 15]
mapa = dict()
numero = 9

def sumar_numero_lista(vector, target):
    # Se crea el mapa de las parejas.
    for i in range(len(vector)):
        valor = vector[i]
        complemento = target - valor
        mapa[complemento] = i

    # Busca las parejas.
    for i in range(len(vector)):
        valor = vector[i]
        # Se verifica que los índices no sean iguales.
        if valor in mapa != mapa.values():
            if valor in mapa != i:
                return {i, mapa[valor]}

print(sumar_numero_lista(nums, numero))