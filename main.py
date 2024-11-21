from fridge import fridge
import random
import matplotlib.pyplot as plt


def main():
    print("working")
    Fridge = fridge(5)
    print(Fridge.El.prices)
    for x in range(1, len(Fridge.El.prices)-1):
        closed = True
        if random.randrange(0, 9) == 0:
            closed = False
        Fridge._update_temp(x, closed)
    print(Fridge.temp)





    fig, ax = plt.subplots()
    x_values = range(len(Fridge.temp))  # X-akse værdier fra 0 til længden af Fridge_temp
    ax.plot(x_values, Fridge.temp)  # Tegn plottet

    # Tilføj akse-labels og titel
    ax.set_xlabel("Time (Index)")
    ax.set_ylabel("Temperature")
    ax.set_title("Fridge Temperature Over Time")

    # Vis plottet
    plt.show()













if __name__ == "__main__":
    main()
