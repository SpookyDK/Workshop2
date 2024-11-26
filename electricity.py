"""
A python file used to load and contain elpriser
"""
import csv


class electricity():
    """
    A class used to load and contain elpriser
    """

    def __init__(self):
        """
        This inits the electricity class and loads the file into memory as self.prices: float []
        """
        self.prices: float = []
        with open('elpris.csv', mode = 'r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                try:
                    self.prices.append(float(lines[1]))
                except:
                    pass
