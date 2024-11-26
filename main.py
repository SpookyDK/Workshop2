from fridge import fridge
import random
import matplotlib.pyplot as plt


def main():
    """
    Run Main
    """
    ai_enhanced_mode = True
    its = 50
    cost = 0
    if ai_enhanced_mode:
        cost = run_ai(its)
    else:
        cost = run_normal(its)
        


    print(cost/its)
    # fig, ax = plt.subplots()
    # ax.plot(range(len(Fridge.temp)),  Fridge.temp)
    # ax.set_xlabel("Time (Index)")
    # ax.set_ylabel("Temperature")
    # ax.set_title("Fridge Temperature Over Time")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.plot(range(len(Fridge.El.prices)),  Fridge.El.prices)
    # ax.set_xlabel("Itteration (Index)")
    # ax.set_ylabel("price")
    # ax.set_title("Electricty prices over time")
    # plt.show()


def run_normal(its: int)-> float:
    """
    Run run_normal
    """
    cost = 0
    for y in range(0, its):
        Fridge = fridge(5)
        for x in range(1, len(Fridge.El.prices)-1):
            closed = True
            if random.randrange(0, 9) == 0:
                closed = False
            Fridge._update_temp(x, closed, "Under3Expanded")
        cost += Fridge.price
    return cost


def run_ai(its: int)-> float:
    """
    Run run_ai
    """
    cost = 0 
    for y in range(0, its):
        Fridge = fridge(5) 
        for x in range(1, len(Fridge.El.prices)-1):
            closed = True
            if random.randrange(0, 9) == 0:
                closed = False
            Fridge._update_temp(x, closed, "Under3Expanded")
        cost += Fridge.price
    print("Algoritm has been AI enhanced")
    return cost






if __name__ == "__main__":
    main()
