from src.evaluador import EvaluadorMateria

def main():
    # Creamos el evaluador para una materia
    matematicas = EvaluadorMateria("Matemáticas")
    
    print(f"--- Evaluando {matematicas.nombre_materia} ---")
    
    # Caso 1: Estudiante que gana con decimales
    resultado1 = matematicas.evaluar_estado(4.1, 3.5, 4.0)
    promedio1 = matematicas.calcular_promedio(4.1, 3.5, 4.0)
    print(f"Estudiante 1 - Promedio: {promedio1:.2f} -> Estado: {resultado1}")
    
    # Caso 2: Estudiante que reprueba
    resultado2 = matematicas.evaluar_estado(2.5, 3.1, 2.0)
    promedio2 = matematicas.calcular_promedio(2.5, 3.1, 2.0)
    print(f"Estudiante 2 - Promedio: {promedio2:.2f} -> Estado: {resultado2}")

if __name__ == "__main__":
    main()