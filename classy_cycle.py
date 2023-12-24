class Cycle:
    def __init__(self, company, model, year):  # Corrected '__init_()' to '__init__()'
        self.company = company
        self.model = model
        self.year = year

    def descriptive_name(self):
        descriptive = f"{self.model} {self.company} {self.year}"
        print(descriptive.title())  # Corrected 'descriptive_name.title()' to 'descriptive.title()'

h = Cycle(1, 2, 3)
h.descriptive_name()
