from electricity import electricity
class fridge:
    def __init__(self, starting_temp: float):
        self.temp: float = [starting_temp]
        self.C1 = 5*(10**-7)*(300**-1)
        self.C2 = 3*(10**-5)*(300**-1)
        self.CC1 = 0*(300**-1)
        self.CC2 = 8*(10**-6)*(300**-1)
        self.El = electricity()
        self.price = 0
        print(self.C1)
        print(self.C2)
        print(self.CC1)
        print(self.CC2)

    def _should_cool(self, itteration: int) -> bool:
        return (self.temp[itteration] > 5)

    def _update_temp(self, itteration: int, closed: bool):
        if self._should_cool(itteration - 1):
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

    def _calculate_price(self, running: bool, itteration: int):
        self.price += self.El.prices[itteration]*1
