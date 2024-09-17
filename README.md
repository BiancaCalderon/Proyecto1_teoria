```markdown
# Proyecto de Conversión de Expresiones Regulares a Autómatas Finito Deterministas (AFD)

Este proyecto convierte expresiones regulares en autómatas finitos deterministas (AFD) utilizando algoritmos como la construcción de Thompson para NFA y el algoritmo de construcción de subconjuntos para convertir NFA a DFA. Además, el AFD se minimiza utilizando un algoritmo de minimización. El proyecto también incluye simulaciones del AFD con cadenas de entrada y exporta los resultados en archivos JSON.

## Estructura del Proyecto

El proyecto está compuesto por varios módulos:

- **`main.py`**: Archivo principal que coordina la conversión de la expresión regular a AFD, su minimización y la simulación del AFD.
- **`regex_conversion.py`**: Contiene funciones para convertir expresiones regulares a notación postfix, construir NFA utilizando el algoritmo de Thompson y generar e imprimir la matriz de adyacencia del NFA.
- **`Construccion_Subconjuntos.py`**: Implementa la conversión de NFA a DFA usando el algoritmo de construcción de subconjuntos.
- **`Minimization.py`**: Contiene funciones para minimizar el AFD.
- **`simulacion.py`**: Define la función para simular el AFD con una cadena de entrada.

## Uso

1. **Ejecutar el Archivo Principal**:
   Para ejecutar el archivo principal `main.py`, utiliza el siguiente comando: python main.py

2. **Ingresar Expresión Regular**:
   Se te pedirá que ingreses una expresión regular en notación estándar,.

3. **Resultados**:
   - La expresión regular se convierte a notación postfix y se guarda en `postfix_output.json`.
   - Se construye el NFA y se genera su matriz de adyacencia.
   - Se convierte el NFA a un AFD.
   - Se minimiza el AFD y el resultado se guarda en `minimized_dfa_complete.json`.
   - Se simula el AFD con una cadena de entrada y se muestra el resultado.

## Archivos de Salida

- **`postfix_output.json`**: Contiene la expresión regular en notación postfix.
- **`nfa_result.json`**: Contiene la matriz de adyacencia del NFA
- **`minimized_dfa_complete.json`**: Contiene el AFD minimizado en formato JSON, incluyendo estados, alfabeto, transiciones, estado inicial y estados de aceptación.

## Ejemplos

- **Entrada**: `a(b|c)*d`
- **Postfix**: `abc|*.d.`
- **Salida**: Se construye el NFA y su matriz de adyacencia, se convierte a AFD, se minimiza y se simula la cadena `abcbcd`.

## Dependencias

Este proyecto requiere Python y no tiene dependencias externas adicionales.

