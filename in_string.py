def check_vowels():
    # Código a implementar utilizando input.
    name = input("Ingrese su nombre: ")
    name = name.lower()
    print(f"Contiene a: {'a' in name}")
    print(f"Contiene e: {'e' in name}")
    print(f"Contiene i: {'i' in name}")
    print(f"Contiene o: {'o' in name}")
    print(f"Contiene u: {'u' in name}")
    
    #name2= input("Ingrese el segundo nombre: ")
    

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

check_vowels()
