from fridge import fridge
import random
import matplotlib.pyplot as plt


def main():
    its = 1
    cost = 0
    time_under = 0
    time_over = 0
    print("working")
    for y in range(0, its):
        Fridge = fridge(5)
        for x in range(1, len(Fridge.El.prices)-1):
            closed = True
            if random.randrange(0, 9) == 0:
                closed = False
            Fridge._update_temp(x, closed, "Under3Expanded")
        cost += Fridge.price
        time_under += Fridge.time_under
        time_over += Fridge.time_over
        fig, ax = plt.subplots()
        ax.plot(range(len(Fridge.temp)), Fridge.temp, color='r')
        ax.plot(range(len(Fridge.El.prices)), Fridge.El.prices, color='g')
        ax.set_xlabel("Time (Index)")
        ax.set_ylabel("Temperature")
        ax.set_title("Fridge Temperature Over Time")
        plt.show()






    print(cost/its)
    print(time_over/its)
    print(time_under/its)
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












if __name__ == "__main__":
    main()
