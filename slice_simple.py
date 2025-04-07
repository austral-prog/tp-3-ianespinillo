def slice_simple():
    texto = "Awesome"
    texto = texto.lower() 
    print(texto[0:3])  # Se espera que imprima "Awe"
    print(texto[2:5])  # Se espera que imprima "eso"
    print(texto)  # Se espera que imprima "weso"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.

slice_simple()  # Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
