

def calcolatrice():
    while True:
        print(''' 
        1 -- addizione
        2 -- sottrazione
        3 -- moltiplicazione
        4 -- divisione
        5 -- elevazione a potenza
        6 -- radice quadrata
        7 -- radice personalizzabile
        lascia vuoto per uscire
        ''')
        user_input = input(': ')
        if user_input == '':
            break
        if user_input in ('1', '2', '3', '4','5','6','7'):
            try:
                num1 = float(input("primo: "))
                num2 = float(input("secondo: "))
                if user_input == "1":
                    result = num1 + num2
                elif user_input == "2":
                    result = num1 - num2
                elif user_input == "3":
                    result = num1 * num2
                elif user_input == "4":
                    if num2 == 0:
                        print("Cannot divide by zero")
                        continue
                    result = num1 / num2
                
                elif user_input == "5":
                    result = num1 ** num2

                elif user_input == "6":
                    if num1 < 0:
                        print('Impossibile calcolare la radice quadrata di un numero negativo')
                        continue
                    else:
                        result = num1 **(1/2)

                elif user_input == "7":
                    if num1 < 0 and num2 % 2 == 0:
                        print( "Impossibile calcolare radici pari di numeri negativi")
                        continue
                    else:
                        result = num1 ** (1/num2)
                    
                print("Result:", result)
                
            except ValueError:
                    print('input invalido')
            
        else:
            print('input invalido')

calcolatrice()
