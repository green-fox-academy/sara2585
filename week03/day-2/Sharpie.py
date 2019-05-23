class Sharpie():
    def __init__(self, color, width, ink_amount = 100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    def use(self):
        if self.ink_amount >= 2:
            self.ink_amount -= 2
            return self.ink_amount
        else:
            return "It's all used!"

# sharpie = Sharpie("white", 20)
# sharpie_use = sharpie.use()
# #print(f"{sharpie_use}")
        