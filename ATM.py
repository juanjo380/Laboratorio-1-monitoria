#Libreria random
import random

#Cajero automatico

#Funciones
#Credenciales aleatorias de tarjetas
def cards():
    global balance, amount_of_moneys, information, iteration
    likely = True
    while likely:
        try:
            amount_of_moneys = int(input("Enter the number of cards to create: "))
            likely = False
        except Exception as m:
            print ("Ops, unexpected error with {} ".format(m))
    for j in range(1,amount_of_moneys+1):
            card_number = random.randint(111111111,999999999)
            clue = random.randint(1111,9999)
            balance = random.randint(0,3000000)
            database = {f"Card_{j}":card_number,
                                f"Password_{j}":clue,
                                f"Money_{j}":balance
                                }
            information |= database
    print("Credentials: {}".format(information))


#Entrada de datos
def entrance():
    global debit_card,iteration
    while True:
        try:
            debit_card = int(input("Please enter the card number: "))
            while debit_card  not in information.values():
                #Ciclo while que verifica si el numero de tarjeta de debito se encuentra dentro de valores de {}
                debit_card = int(input("Card not found, try again: "))
            break
        except ValueError: #Excepcion de solo valores numericos
            print("You can only enter numerical values")


#Clave de tarjetas
def pin():
    global iteration
    for iteration in range(1,amount_of_moneys):
        while debit_card == information[f"Card_{iteration}"]:
            try:
                pook = int(input("Enter the password with which you withdraw money.: "))
                while pook != information[f"Password_{iteration}"]:
                    pook = int(input("Error, Enter the password with which you withdraw money again: "))
                break
            except ValueError:
                print("Only integer numbers will be accepted.")
    print(f"You have: $", information[f"Money_{iteration}"])


#Funcion para retirar dinero
def mony():
    limit = 10000 # Cantidad limite para retirar
    if information[f"Money_{iteration}"] >= limit:
        while True:
            try:
                withdraw = int(input("Enter the money you want to withdraw: "))
                if withdraw%limit != 0 or withdraw > information[f"Money_{iteration}"]:
                    withdraw = int(input("Invalid amount, try again please: "))
                print(f"""
                        You have successfully withdrawn: $ {withdraw}
                        You now have it available to withdraw: $""",
                        information[f"Money_{iteration}"] - withdraw
                      )
                break
            except ValueError:
                print("Remember, we only accept numerical values.")
    else:
        print("You don't have enough money.")


#Enterpoint
if __name__ == '_main_':
    information = {}
    cards()
    entrance()
    pin()
    mony()