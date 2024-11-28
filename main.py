from fridge import fridge
from electricity import Electricity
import random
import matplotlib.pyplot as plt 
import doctest


def main():
    """
    Run Main
    """
    ai_enhanced_mode = True
    its = 10
    cost = 0





    el = Electricity()

    if ai_enhanced_mode:
        cost = run_ai(its, el)
    else:
        cost = run_normal(its, el)
        

    print(cost/its)
    plot_data(el)
    


def run_normal(its: int, El: Electricity)-> float:
    """
    Run run_normal
    >>> 11000 < run_normal(1,Electricity()) < 13000
    True
    """
    cost = 0
    for y in range(0, its):
        Fridge = fridge(5, El)
        for x in range(1, len(El.prices)-1):
            closed = True
            if random.randrange(0, 9) == 0:
                closed = False
            Fridge._update_temp(x, closed, "Under3")
        cost += Fridge.price
    return cost


def run_ai(its: int, El: Electricity)-> float:
    """
    Run run_ai
    >>> 11000 < run_normal(1,Electricity()) < 13000
    True
    """
    cost = 0 
    for y in range(0, its):
        Fridge = fridge(5, El) 
        for x in range(1, len(El.prices)-1):
            closed = True
            if random.randrange(0, 9) == 0:
                closed = False
            Fridge._update_temp(x, closed, "Under3")
        cost += Fridge.price
    print("Algoritm has been AI enhanced")
    return cost


def plot_data(El: Electricity):
    """
    plots the data to charts
    >>> plot_data(Electricity())
    True
    """
    Fridge = fridge(5, El) 
    for x in range(1, len(El.prices)-1):
        closed = True
        if random.randrange(0, 9) == 0:
            closed = False
        Fridge._update_temp(x, closed, "Under3")

    fig, ax = plt.subplots()
    ax.plot(range(len(Fridge.temp)), Fridge.temp, color='r')
    ax.plot(range(len(Fridge.El.prices)), Fridge.El.prices, color='g')
    ax.set_xlabel("Time (Index)")
    ax.set_ylabel("Temperature, Electricity prices")
    ax.set_title("Fridge Temperature Over Time")
    plt.show()
    return True





if __name__ == "__main__":
    doctest.testmod()
    main()
