class EvaluadorMateria:
    def __init__(self, nombre_materia: str):
        self.nombre_materia = nombre_materia

    def _validar_nota(self, nota: float):
        """Valida que la nota esté en el rango permitido (0.0 a 5.0)."""
        if not (0.0 <= nota <= 5.0):
            raise ValueError(f"La nota {nota} es inválida. Debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self, nota1: float, nota2: float, nota3: float) -> float:
        """Calcula y retorna el promedio exacto de las tres notas."""
        notas = [nota1, nota2, nota3]
        for nota in notas:
            self._validar_nota(nota)
        
        return sum(notas) / len(notas)

    def evaluar_estado(self, nota1: float, nota2: float, nota3: float) -> str:
        """
        Evalúa las tres notas y determina si el estudiante gana o reprueba.
        Retorna 'gana' si el promedio es >= 3.0, de lo contrario 'reprueba'.
        """
        promedio = self.calcular_promedio(nota1, nota2, nota3)
        
        if promedio >= 3.0:
            return "gana"
        else:
            return "reprueba"