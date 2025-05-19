from mean_var_std import calculate

<<<<<<< HEAD
# Prueba de la función con un conjunto de datos
try:
    print("Ejecutando prueba con datos de entrada...")
    print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
except Exception as e:
    print(f"Error en la ejecución: {e}")

# Ejecutar pruebas unitarias
print("Ejecutando pruebas unitarias...")
main(module='test_calculate', exit=False)
=======
# Prueba de la función
resultado = calculate([0,1,2,3,4,5,6,7,8])
print(resultado)
>>>>>>> 45d73d6 (Subiendo versión modificada del visualizador de series de tiempo)
