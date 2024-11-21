from electricity import electricity
import math


class fridge:
    def __init__(self, starting_temp: float):
        self.temp: float = [starting_temp]
        self.C1 = 5*(10**-7)
        self.C2 = 3*(10**-5)
        self.CC1 = 0*(300**-1)
        self.CC2 = 8*(10**-6)
        self.El = electricity()
        self.price = 0
        self.time_under = 0 
        self.time_over = 0

    def _should_cool(self, itteration: int, closed: bool = True, thermostat: str = "") -> bool:
        match thermostat:
            case "Under3":
                return self.thermostat_under_3(itteration-1)
            case "Under3Expanded":
                return self.thermostat_under_3_expanded(itteration-1, closed)
            case _:
                return (self.temp[itteration] > 5)

    def _update_temp(self, itteration: int, closed: bool, thermostat: str = ""):
        if self._should_cool(itteration - 1, closed, thermostat):
            if closed:
                self.temp.append(self.temp[itteration - 1] + (self.C1 * (20 - self.temp[itteration - 1]) + self.CC2 * (-5 - self.temp[itteration - 1]))*300)
            else:
                self.temp.append(self.temp[itteration - 1] + (self.C2 * (20 - self.temp[itteration - 1]) + self.CC2* (-5 - self.temp[itteration - 1]))*300)
            self._calculate_price(True, itteration)
        else:
            if closed:
                self.temp.append(self.temp[itteration - 1] + (self.C1 * (20 - self.temp[itteration - 1]) + self.CC1 * (-5 - self.temp[itteration - 1]))*300)
            else:
                self.temp.append(self.temp[itteration - 1] + (self.C2 * (20 - self.temp[itteration - 1]) + self.CC1 * (-5 - self.temp[itteration - 1]))*300)
            self._calculate_price(False, itteration)

    def _calculate_price(self, running: bool, itteration: int):
        if running:
            self.price += self.El.prices[itteration]*1  # electricity cost added

        if self.temp[itteration] < 3.5:
            self.price += 4.39*math.exp(-0.49*self.temp[itteration])
            self.time_over += 1
        elif self.temp[itteration] >= 6.5:
            self.price += 0.11*math.exp(0.31*self.temp[itteration])
            self.time_over += 1

    def thermostat_under_3(self, itteration: int) -> bool:
        if self.temp[itteration] >= 6.5:
            return True
        elif self.temp[itteration] > 3.5 and self.El.prices[itteration] < 3:
            return True
        else:
            return False

    def thermostat_under_3_expanded(self, itteration: int, closed: bool) -> bool:
        if self.temp[itteration] >= 6.2:
            return True
        elif self.temp[itteration] > 3.5 and self.El.prices[itteration] <2:
            return True
        elif self.temp[itteration] > 5 and self.El.prices[itteration] < 3:
            return True
        elif self.temp[itteration] > 6.2 and not closed:
            return True
        else:
            return False
