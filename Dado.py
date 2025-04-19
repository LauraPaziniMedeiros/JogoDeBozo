from random import Random

class Dado:
    def __init__ (self, n = 6, seed = None):
        self.lados = n
        if seed == None:
            self.r = Random()
        else:
            self.r = Random()
            self.r.seed(seed)
        self.rolar()

    def rolar(self):
        self.atual = self.r.randint(1, self.lados)
        return self.atual
    
    def get_lado(self):
        return self.atual
    
    def __str__ (self):
        if self.lados != 6:
            print("Não há representação para este dado\n")
            return
        
        # Definição das strings
        s010 = "|  *  |\n"
        s100 = "|*    |\n"
        s001 = "|    *|\n"
        s000 = "|     |\n"
        s101 = "|*   *|\n"
        s111 = "|* * *|\n"

        res = "+-----+\n"
        if self.get_lado() == 1:
            res += s000 + s010 + s000
        elif self.get_lado() == 2:
            res += s100 + s000 + s001
        elif self.get_lado() == 3:
            res += s100 + s010 + s001
        elif self.get_lado() == 4:
            res += s101 + s000 + s101
        elif self.get_lado() == 5:
            res += s101 + s010 + s101
        else:
            res += s111 + s000 + s111
        res += "+-----+\n"

        return res