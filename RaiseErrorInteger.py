try:
    number = int(input("inserisci un numero maggiore di 10"))
    if number <= 10:
        raise Exception("Number must be bigger than 10")
except ValueError as err:
    print("Pls insert an integer")
except Exception as ex:
    print(ex)
