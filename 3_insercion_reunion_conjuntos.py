import random

conjunto1 = {random.randint(1,10) for _ in range(5)}
conjunto2 = {random.randint(1,10) for _ in range(5)}

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

interseccion = conjunto1.intersection(conjunto2)
union = conjunto1.union(conjunto2)
diferencia = conjunto1.difference(conjunto2)

print("Números interseccionados ", interseccion)
print("Números comunes", union)
print("Números diferentes", diferencia)