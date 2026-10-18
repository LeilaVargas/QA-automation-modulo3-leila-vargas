# TP Integrador - QA Automation (Módulo 3)

## Contenido

- `ejercicios/numero_primo.py`: Punto 1. Indica si un número ingresado es primo.
- `ejercicios/ecuacion_cuadratica.py`: Punto 2. Calcula las raíces de ax² + bx + c = 0.
- `pruebas/ui/test_saucedemo.py`: Punto 3, casos 1 a 3 sobre https://www.saucedemo.com/ (Selenium).
- `pruebas/api/test_pokeapi.py`: Punto 3, casos 1 a 3 sobre https://pokeapi.co/api/v2 (requests).
- `paginas/`: Page Objects usados por las pruebas de UI.
- `resultados/reporte_ejecucion.html`: reporte HTML de la última ejecución.

## Preparar el entorno (Windows)

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

## Ejecutar

    pytest                          # Chrome
    pytest --navegador firefox      # Firefox
    pytest --navegador edge         # Edge
    pytest --sin-ventana            # sin abrir el navegador

    python ejercicios\numero_primo.py
    python ejercicios\ecuacion_cuadratica.py
