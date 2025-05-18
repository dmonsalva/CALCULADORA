# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

# Prueba de la función con un conjunto de datos
try:
    print("Ejecutando prueba con datos de entrada...")
    print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
except Exception as e:
    print(f"Error en la ejecución: {e}")

# Ejecutar pruebas unitarias
print("Ejecutando pruebas unitarias...")
main(module='test_calculate', exit=False)