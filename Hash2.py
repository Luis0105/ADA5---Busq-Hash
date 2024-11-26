def hash_plegamiento(key, table_size):
    print(f"Calculando hash de la clave {key} usando el método de plegamiento.")
    key_str = str(key)
    parts = [int(key_str[i:i+2]) for i in range(0, len(key_str), 2)]  # Dividir en partes de 2 dígitos
    print(f"1. Dividir la clave en partes de 2 dígitos: {parts}")
    sum_parts = sum(parts)
    print(f"2. Sumar las partes: {sum(parts)} = {sum_parts}")
    hash_value = sum_parts % table_size
    print(f"3. Resultado de aplicar el módulo: {sum_parts} % {table_size} = {hash_value}")
    return hash_value

# Ejemplo de uso
print("Hash por Plegamiento:")
print("-----------")
key = 123456
table_size = 10
hash_plegamiento(key, table_size)
print()
key = 789012
hash_plegamiento(key, table_size)
print()
