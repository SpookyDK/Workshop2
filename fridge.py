"""
A python file containing the fridge class
"""
from electricity import Electricity
import math
import doctest
import random


class fridge:
    """
    fridge class to hold and control a theoritical fridge
    """
    def __init__(self, starting_temp: float, EL: Electricity):
        """
        Init the fridge class, requires a starting_temp
        """
        self.temp: float = [starting_temp]
        self.C1 = 5*(10**-7)
        self.C2 = 3*(10**-5)
        self.CC1 = 0*(300**-1)
        self.CC2 = 8*(10**-6)
        self.El = EL
        self.price = 0
        self.time_under = 0 
        self.time_over = 0

    def _should_cool(self, itteration: int, closed: bool = True, thermostat: str = "") -> bool:
        """
        Function using a switch case(Not fucking match case you little piece of shit using python terms), 
        to determen if cooling is needed
        Takes a string describing the thermostat to use, and a the itteration and state of the door
        >>> test_fridge._should_cool(1,False, "Under3Expanded")
        False

        >>> test_fridge._should_cool(1,False, "Under3")
        False
        """
        match thermostat:
            case "Under3":
                return self.thermostat_under_3(itteration-1)
            case "Under3Expanded":
                return self.thermostat_under_3_expanded(itteration-1, closed)
            case "thermostat_bogo":
                return self.thermostat_bogo()
            case _:
                return (self.temp[itteration] > 5)

    def _update_temp(self, itteration: int, closed: bool, thermostat: str = ""):
        """
        Uses the formula to update the fridge temp, calls _should_cool
        """
        if self._should_cool(itteration - 1, closed, thermostat):
            if closed:
                self.temp.append(self.temp[itteration - 1] + (self.C1 * (20 - self.temp[itteration - 1]) + self.CC2 * (-5 - self.temp[itteration - 1]))*300)
            else:
                self.temp.append(self.temp[itteration - 1] + (self.C2 * (20 - self.temp[itteration - 1]) + self.CC2 * (-5 - self.temp[itteration - 1]))*300)
            self._calculate_price(True, itteration)
        else:
            if closed:
                self.temp.append(self.temp[itteration - 1] + (self.C1 * (20 - self.temp[itteration - 1]) + self.CC1 * (-5 - self.temp[itteration - 1]))*300)
            else:
                self.temp.append(self.temp[itteration - 1] + (self.C2 * (20 - self.temp[itteration - 1]) + self.CC1 * (-5 - self.temp[itteration - 1]))*300)
            self._calculate_price(False, itteration)

    def _calculate_price(self, running: bool, itteration: int):
        """
        Calculates the price, electricity, and food loss
        """
        if running:
            self.price += self.El.prices[itteration]*1  # electricity cost added

        if self.temp[itteration] < 3.5:
            self.price += 4.39*math.exp(-0.49*self.temp[itteration])
            self.time_over += 1
        elif self.temp[itteration] >= 6.5:
            self.price += 0.11*math.exp(0.31*self.temp[itteration])
            self.time_over += 1

    def thermostat_under_3(self, itteration: int) -> bool:
        """
        Thermostat which cools if over 6.5, or if over 3.5, and electricity under 3
        """
        if self.temp[itteration] >= 6.5:
            return True
        elif self.temp[itteration] > 3.5 and self.El.prices[itteration] < 2.5:
            return True
        else:
            return False

    def thermostat_under_3_expanded(self, itteration: int, closed: bool) -> bool:
        """
        Thermostat which cools if over 6.5, or if over 3.5, and electricity under 3.
        And tries to minimize food loss
        """
        if self.temp[itteration] >= 6.2:
            return True
        elif self.temp[itteration] > 3.5 and self.El.prices[itteration] <1.3:
            return True
        elif self.temp[itteration] > 5 and self.El.prices[itteration] < 2.8:
            return True
        elif self.temp[itteration] > 6.2 and not closed:
            return True
        else:
            return False

    def thermostat_bogo(self) -> bool:
        return random.randrange(0,1) == 1


if __name__ == "__main__":
    doctest.testmod(extraglobs={"test_fridge": fridge(5, Electricity())})
