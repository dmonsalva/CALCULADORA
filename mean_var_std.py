import numpy as np

<<<<<<< HEAD
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
=======
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("La lista debe contener nueve números")

    matrix = np.array(numbers).reshape(3, 3)

    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations
>>>>>>> 45d73d6 (Subiendo versión modificada del visualizador de series de tiempo)
