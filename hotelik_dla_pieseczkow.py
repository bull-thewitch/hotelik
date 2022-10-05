from hotel_obj import *

h = Hotel()

for i in range(5):
    h.add_box(Box(i + 1))

while True:
    print(h)
    print("1: zamelduj\n2: wymelduj\n3: zamien\nk: koniec")
    cmd = input()
    if cmd == "1":
        name = input("Podaj imię pieska: ") 
        try:
            h.check_in(name)
        except Exception as e:
            print("Problem z zameldowaniem", str(e)) 
    elif cmd == "2":
        number = input("Podaj numer boxa")
        try:
            h.check_out(int(number))
        except Exception as e:
            print("Problem z wymeldowaniem", str(e))
    elif cmd == "3":
        n1 = input("Podaj numer boxa, który chcesz zmienić: ")
        n2 = input("Podaj numer boxa, na który chcesz zmienić: ")
        try:
            h.exchange_box(int(n1), int(n2))
        except Exception as e:
            print("Zjebałeś", str(e))
    elif cmd == "k":
        print("Do zobaczenia")
        break
    else:
        print("Nieznane polecenie")
print(h)

