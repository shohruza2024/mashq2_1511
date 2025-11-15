class Universitet:
    def ish_kuni_boshlash(self):
        raise NotImplementedError

    def maosh_hisoblash(self, soat):
        raise NotImplementedError

    def dars_otish(self, fan):
        pass


class Talaba(Universitet):
    def ish_kuni_boshlash(self):
        return "Talaba darsga keldi."

    def maosh_hisoblash(self, soat):
        return 0 


class Oqituvchi(Universitet):
    def __init__(self, tarif):
        self.tarif = tarif

    def ish_kuni_boshlash(self):
        return "O'qituvchi ish kunini boshladi."

    def maosh_hisoblash(self, soat):
        return self.tarif * soat

    def dars_otish(self, fan):
        print(f"{fan} fanidan dars o'tilmoqda.")


class Xodim(Universitet):
    def __init__(self, tarif):
        self.tarif = tarif

    def ish_kuni_boshlash(self):
        return "Xodim ishga keldi."

    def maosh_hisoblash(self, soat):
        return self.tarif * soat

jamoa = [
    Talaba(),
    Oqituvchi(50000),
    Xodim(20000)
]

umumiy_maosh = sum(x.maosh_hisoblash(160) for x in jamoa)

print("Oylik umumiy maosh:", umumiy_maosh)

jamoa[1].dars_otish("Matematika")
