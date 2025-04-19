from random import Random

class Dado:
    def __init__ (self, n = 6, seed = None):
        self.lados = n
        if seed == None:
            self.r = Random()
        else:
            self.r = Random(seed)
        self.rolar()

    def rolar(self):
        self.atual = self.r.randint(1, self.lados)
        return self.atual
    
    def get_lado(self):
        return self.atual

    def imprime_dado (self):
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
        s = "+-----+\n"

        if self.get_lado() == 1:
            print(s000 + s010 + s000 + s)
            return;
        if self.get_lado() == 2:
            print(s100 + s000 + s001 + s)
            return;
        if self.get_lado() == 3:
            print(s100 + s010 + s001 + s)
            return;
        if self.get_lado() == 4:
            print(s101 + s000 + s101 + s)
            return;
        if self.get_lado() == 5:
            print(s101 + s010 + s101 + s)
            return;
        if self.get_lado() == 6:
            print(s111 + s000 + s111 + s)
            return;

if __name__ == "__main__":
    d = Dado()
    d.rolar()
    d.imprime_dado()