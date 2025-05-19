import numpy as np
import unittest
import sys

# Función para calcular estadísticas de una lista de nueve números
def calculate(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números")

    matriz = np.array(lista).reshape(3, 3)

    estadisticas = {
        'mean': [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.mean().tolist()],
        'variance': [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.var().tolist()],
        'standard deviation': [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.std().tolist()],
        'max': [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.max().tolist()],
        'min': [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.min().tolist()],
        'sum': [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.sum().tolist()]
    }

    return estadisticas

# Prueba de la función con un conjunto de datos
if __name__ == "__main__":
    try:
        print("Ejecutando prueba con datos de entrada...")
        print(calculate([0,1,2,3,4,5,6,7,8]))
    except Exception as e:
        print(f"Error en la ejecución: {e}")

    # Ejecutar pruebas unitarias sin conflictos de argumentos en entornos interactivos
    print("Ejecutando pruebas unitarias...")
    sys.argv = ['']
    unittest.main(exit=False)

# Clase de pruebas unitarias
class TestCalculate(unittest.TestCase):
    def test_correct_output(self):
        """Prueba con una lista válida de 9 números."""
        resultado = calculate([0,1,2,3,4,5,6,7,8])
        esperado = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(resultado, esperado)

    def test_invalid_input(self):
        """Prueba que se genere una excepción cuando la lista tiene menos de 9 elementos."""
        with self.assertRaises(ValueError):
            calculate([1,2,3])

    def test_numeric_values(self):
        """Prueba con una lista de valores negativos y positivos."""
        resultado = calculate([-1,0,1,-2,3,-3,2,-4,4])
        self.assertIsInstance(resultado, dict)

if __name__ == "__main__":
    unittest.main()
    