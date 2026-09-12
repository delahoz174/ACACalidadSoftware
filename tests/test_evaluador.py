import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.evaluador import EvaluadorMateria

class TestEvaluadorMateria(unittest.TestCase):
    
    def setUp(self):
        self.evaluador = EvaluadorMateria("Matemáticas")

    def test_cp01_gana_con_decimales(self):
        """CP01 Estudiante aprueba con notas decimales altas"""
        resultado = self.evaluador.evaluar_estado(4.1, 3.5, 4.0)
        self.assertEqual(resultado, "gana", "El CP01 falló: debió ganar.")

    def test_cp02_reprueba_por_promedio(self):
        """CP02 Estudiante reprueba por promedio bajo"""
        resultado = self.evaluador.evaluar_estado(2.5, 3.1, 1.8)
        self.assertEqual(resultado, "reprueba", "El CP02 falló: debió reprobar.")

    def test_cp03_gana_limite_exacto(self):
        """CP03 Aprobación en el límite exacto (Caso borde)"""
        resultado = self.evaluador.evaluar_estado(3.0, 3.0, 3.0)
        self.assertEqual(resultado, "gana", "El CP03 falló: debió ganar.")

    def test_cp04_error_nota_fuera_de_rango(self):
        """CP04 Validación de seguridad: Nota fuera del rango"""
        try:
            self.evaluador.evaluar_estado(5.5, 4.0, 3.0)
            self.fail("El CP04 falló: Se esperaba un error por nota mayor a 5.0")
        except ValueError:
            pass

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvaluadorMateria)
    
  
    descripciones = [prueba.shortDescription() for prueba in suite]
    
    runner = unittest.TextTestRunner(verbosity=0)
    resultado = runner.run(suite)

    print("\n" + "="*60)
    if resultado.wasSuccessful():
        print(f"✅ Se ejecutaron {resultado.testsRun} casos de prueba exitosamente.")
        print("Test ejecutados:")
        for desc in descripciones:
            print(f"  - {desc}")
    else:
        print(f"❌ Fallaron {len(resultado.failures) + len(resultado.errors)} pruebas.")
        print("Revisa los mensajes de error arriba para más detalles.")
    print("="*60 + "\n")