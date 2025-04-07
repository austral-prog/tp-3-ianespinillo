def slice_advanced():
    # Código a implementar utilizando input.
    texto = input()
    texto = texto.lower()
    print(texto[4:len(texto):2])  # Se espera que imprima "Awe"
slice_advanced()
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
