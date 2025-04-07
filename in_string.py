def check_vowels():
    # Código a implementar utilizando input.
    name = input()
    name = name.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        print(f"Contiene {vowel}: {vowel in name}")
    
    #name2= input("Ingrese el segundo nombre: ")
    

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

check_vowels()
