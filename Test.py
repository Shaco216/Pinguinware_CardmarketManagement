
#https://www.youtube.com/watch?v=jMQfA1cmFw8
class Test:
    def __init__(self,tcg, *args):
        if tcg == 'YuGiOh':
            for x in args:
                print(x)
            self.wort = args[0]#https://stackoverflow.com/questions/3136059/getting-one-value-from-a-tuple
            self.zahl = args[1]
        if tcg == 'MTG':
            print(f"my parameters are: {args}")

a = Test('YuGiOh', "hello", 2)
b = Test('MTG', "hellow", 3)

print(a.wort)
print(a.zahl)