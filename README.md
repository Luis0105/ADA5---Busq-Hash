# ADA5---Busq-Hash
- En qué consiste cada ejercicio
1. Hash por Plegamiento: Este método divide la clave en partes de igual tamaño (en este caso, dos dígitos por parte). Luego suma estas partes y calcula el índice aplicando un módulo con el tamaño de la tabla hash. Este método distribuye los datos uniformemente al considerar las distintas partes de la clave, lo cual es útil para claves largas y complejas.
2. Hash por Cuadrado: Este método eleva la clave al cuadrado, extrae los dígitos centrales del resultado, y calcula el índice aplicando un módulo con el tamaño de la tabla hash. Los dígitos centrales suelen tener menos patrones repetitivos que los extremos de una clave, lo cual mejora la distribución.

- Por qué usan ese método de búsqueda
1. Hash por Plegamiento: Se utiliza porque es sencillo y efectivo para claves numéricas largas. Permite aprovechar todas las partes de la clave y distribuye los datos de manera uniforme en la tabla.
2. Hash por Cuadrado: Es útil porque los dígitos centrales de un número al cuadrado tienen menos correlación con la clave original, lo que ayuda a evitar colisiones en la tabla hash.

- Si sé pudiera mejorar con otro método de búsqueda
1. Hash por Plegamiento: Puede mejorarse si se combina con una función de dispersión adicional o se usa un tamaño de tabla óptimo (como un número primo) para reducir las colisiones. Otro método, como hash por módulo (división), podría ser más simple y rápido si las claves son cortas.
2. Hash por Cuadrado: Para claves largas, podría usarse hash por plegamiento para considerar múltiples secciones de la clave. Si las claves son cadenas o de naturaleza textual, un método como hashing basado en caracteres ASCII o hashing de suma ponderada podría ser más efectivo.

- Conclusiones
Ambos métodos son útiles para convertir claves complejas en índices hash que permitan acceder eficientemente a una tabla hash. Hash por Plegamiento es ideal para claves largas y distribuye bien los valores al procesar todas las partes de la clave, mientras que el hash por cuadrado es más adecuado para claves cortas, ya que aprovecha los dígitos centrales del cuadrado de la clave para obtener índices con menos patrones repetitivos. La elección del método depende de las características de las claves y de la necesidad de minimizar colisiones. En la práctica, combinar estos métodos con técnicas como encadenamiento o direccionamiento abierto mejora aún más su rendimiento.
