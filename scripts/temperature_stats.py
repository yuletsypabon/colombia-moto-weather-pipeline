# Objetivo: escribir una función que reciba una lista de temperaturas y retorne el promedio, el máximo y el mínimo. Si la lista está vacía, debe lanzar un ValueError con un mensaje claro.


list_of_temperatures = (23, 25, 19, 30, 22)

def temperature_stats(temperatures):
    if not temperatures:
        raise ValueError("La lista de temperaturas no puede estar vacía.")
    
    average = sum(temperatures) / len(temperatures)
    maximum = max(temperatures)
    minimum = min(temperatures)
        
    return {"promedio": average, "máximo": maximum, "mínimo": minimum}

print(temperature_stats(list_of_temperatures))    
