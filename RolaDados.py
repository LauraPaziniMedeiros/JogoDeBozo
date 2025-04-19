from random import Random
from Dado import Dado

class RolaDados:
    def __init__ (self, n, seed):
        self.n = n
        if seed != 0:
            rd = Random()
            rd.seed(seed)
        
        self.dados = []
        for _ in range(n):
            if seed == 0:
                d = Dado()
            else:
                d = Dado(6, rd.randint(1, 10000))

            self.dados.append(d)

    def rolar_dados(self, s = None):
        res = []
        i = 0
        if s == None:
            for i in range(self.n):
                res[i] = self.dados[i].rolar()

        s.split()
        quais = [False] * 6
        for c in s:
            quais[int(c)] = True
        j = 0
        for d in quais:
            if d:
                res[i] = self.dados[d].rolar()
                i += 1
            j += 1

        return res
    
    def __str__(self) -> str:
        if not self.dados:
            return ""
        
        # Get string representations of all dice
        dice_strings = [str(d).split('\n') for d in self.dados]
        
        # Build output line by line
        lines = []
        for line_parts in zip(*dice_strings):
            line = "    ".join(part.ljust(10) for part in line_parts)
            lines.append(line)
        return "\n".join(lines)
    
def main():
    d = RolaDados(5)
    d.rolar_dados()
    print(d)