class Klasa(object):
    tab = [1,2,3]

    def __init__(self, tab, zmienna1, zmienna2):
        self.tab = tab
        self._zmienna1 = zmienna1
        self.__zmienna2 = zmienna2
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def metodaInstancyjna(self):
        print("Wywołano metodę 'metodaInstancyjna()'")
        print("Instancyjne tab: " + self.tab)
        print("Statycne tab: " + Klasa.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")

obiekt = Klasa([4, 5, 6], 10, 20)
print(obiekt._Klasa__zmienna2)
####################################################
# Zmiennej 'tab' jest przypisywana tablica [4, 5, 6]
# Zmiennej '_zmienna1' jest przypisywana wartość 10
# Zmiennej '__zmienna2' jest przypisywana wartość 20
####################################################