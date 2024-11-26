def hash_cuadrado(key, table_size):
    print(f"Calculando hash de la clave {key} usando el método de cuadrado.")
    squared = key ** 2
    print(f"1. Elevar la clave al cuadrado: {key}^2 = {squared}")
    squared_str = str(squared)
    mid = len(squared_str) // 2
    middle_digits = squared_str[mid-1:mid+1]  # Extraemos dos dígitos centrales
    print(f"2. Extraemos los dígitos centrales: {middle_digits}")
    hash_value = int(middle_digits) % table_size
    print(f"3. Resultado de aplicar el módulo: {int(middle_digits)} % {table_size} = {hash_value}")
    return hash_value

# Ejemplo de uso
print("Hash por Cuadrado:")
print("-----------")
key = 123
table_size = 10
hash_cuadrado(key, table_size)
print()
key = 456
hash_cuadrado(key, table_size)
print()
