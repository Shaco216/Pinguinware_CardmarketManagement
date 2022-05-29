
#https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python
class card:
    #enumeration für tcg statt genauem string: https://www.youtube.com/watch?v=-MZiQaNI0QA
    def __init__(self,tcg, *args):# name, edition, grading, price, colors, type):
        self.tcg = tcg
        if tcg == "YuGiOh"
        self.name = name
        self.edition = edition
        self.grading = grading
        self.price = price
        self.colors = colors
        self.type = type #kartentyp: creature,