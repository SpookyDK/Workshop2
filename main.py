from fridge import fridge
from electricity import electricity
import random


def main():
    print("working")
    Fridge = fridge(5)

    for x in range(1, len(Fridge.El.prices)):
        closed = True
        if random.randrange(0, 9) == 0:
           closed = False
        Fridge._update_temp(x, closed)
        print(Fridge.temp[x], Fridge.price)
    




















if __name__ == "__main__":
    main()
