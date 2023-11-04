def calcolatrice():
    while True:
        print(''' 
        1 -- addizione
        2 -- sottrazione
        3 -- moltiplicazione
        4 -- divisione
        lascia vuoto per uscire
        ''')
        user_input = input(": ")
        if user_input == "":
            break
        if user_input in ("1", "2", "3", "4"):
            num1 = float(input("primo numero "))
            num2 = float(input("secondo numero: "))

            if user_input == "1":
                result = num1 + num2
            elif user_input == "2":
                result = num1 - num2
            elif user_input == "3":
                result = num1 * num2
            elif user_input == "4":
                if num2 == 0:
                    print("no divisioni per 0")
                    continue
                result = num1 / num2

            print('Risultato: ', result)
        else:
            print('non valido riprova.')

calcolatrice()
