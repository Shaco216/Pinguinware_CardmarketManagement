
# https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python
class Card:
    # enumeration für tcg statt genauem string: https://www.youtube.com/watch?v=-MZiQaNI0QA
    # tcg_list = ["MTG","YuGiOh"]
    def __init__(self, tcg, *args):
        self.tcg = tcg
        self.name = args[0]
        self.expansionpack = args[1]
        self.grading = args[2]
        self.price = args[3]
        self.language = args[4]
        self.signed = args[5]
        if tcg == 0:
            self.mtgrarity = args[6]
            self.colors = args[7]
            self.type = args[8]  # kartentyp: creature,
            self.foil = args[9]
        if tcg == 1:
            self.yugiohrarity = [6]
