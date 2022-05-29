

class Sammlung:
    def __init__(self, kartensammlung):
        self.Kartensammlung = kartensammlung

    def get_wert(self):
        gesamtwert = 0
        for item in self.Kartensammlung:
            gesamtwert = gesamtwert + item.price
        return gesamtwert
