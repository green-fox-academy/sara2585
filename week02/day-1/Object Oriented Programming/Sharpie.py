class Sharpie():
    def __init__(self, color, width, ink_amount = 100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    def use(self):
        self.ink_amount -= 2
        return self.ink_amount

sharpie = Sharpie("white", 50.0)
sharpie_use = sharpie.use()
print(f"{sharpie_use}")
        