import csv


class electricity():
    def __init__(self):
        self.prices: float = []
        print("electricity.py init")
        with open('elpris.csv', mode = 'r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                try:
                    self.prices.append(float(lines[1])+0.761)
                except:
                    pass
