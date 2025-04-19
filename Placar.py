class Placar:
    POSICOES = 10
    PLACAR = [0] * 10
    TAKEN = [False] * 10

    def add(self, posicao: int, dados: list):
        if self.TAKEN[posicao - 1]:
            raise ValueError("Posição ocupada")
        k = 0
        if posicao == 1:
            k = self.conta(1, dados)
        elif posicao == 2:
            k = 2 * self.conta(2, dados)
        elif posicao == 3:
            k = 3 * self.conta(3, dados)
        elif posicao == 4:
            k = 4 * self.conta(4, dados)
        elif posicao == 5:
            k = 5 * self.conta(5, dados)
        elif posicao == 6:
            k = 6 * self.conta(6, dados)
        elif posicao == 7:  # full hand
            if self.checkFull(dados):
                k = 15
        elif posicao == 8:  # sequencia
            if self.checkSeqMaior(dados):
                k = 20
        elif posicao == 9:
            if self.checkQuadra(dados):
                k = 30
        elif posicao == 10:
            if self.checkQuina(dados):
                k = 40
        else:
            raise ValueError("Valor da posição ilegal")

        self.PLACAR[posicao - 1] = k
        self.TAKEN[posicao - 1] = True

    def getScore(self) -> int:
        t = 0
        for i in range(0, self.POSICOES):
            if self.TAKEN[i]:
                t += self.PLACAR[i]
        return t

    def conta(self, n: int, vet: list) -> int:
        cont = 0
        for i in vet:
            if i == n:
                cont += 1
        return cont

    def checkFull(self, dados: list) -> bool:
        v = dados.copy()
        v.sort()
        return (v[0] == v[1] and v[1] == v[2] and v[3] == v[4]) or (
            v[0] == v[1] and v[2] == v[3] and v[3] == v[4]
        )

    def checkQuadra(self, dados: list) -> bool:
        v = dados.copy()
        v.sort()
        return (v[0] == v[1] and v[1] == v[2] and v[2] == v[3]) or (
            v[1] == v[2] and v[2] == v[3] and v[3] == v[4]
        )

    def checkQuina(self, dados: list) -> bool:
        v = dados.copy()
        return v[0] == v[1] and v[1] == v[2] and v[2] == v[3] and v[3] == v[4]

    def checkSeqMaior(self, dados: list) -> bool:
        v = dados.copy()
        v.sort()
        return (
            v[0] == v[1] - 1
            and v[1] == v[2] - 1
            and v[2] == v[3] - 1
            and v[3] == v[4] - 1
        )

    def __repr__(self) -> str:
        s = ""
        for i in range(0, 3):
            num = (
                " {:<4}".format(self.PLACAR[i])
                if self.TAKEN[i]
                else "({}) ".format(i + 1)
            )
            s += num + "   |   "
            num = (
                " {:<4}".format(self.PLACAR[i + 6])
                if self.TAKEN[i + 6]
                else "({}) ".format(i + 7)
            )
            s += num + "   |  "
            num = (
                " {:<4}".format(self.PLACAR[i + 3])
                if self.TAKEN[i + 3]
                else "({}) ".format(i + 4)
            )
            s += num + "\n-------|----------|-------\n"
        num = " {:<4}".format(self.PLACAR[9]) if self.TAKEN[9] else "({})".format(10)
        s += "       |   " + num + "   |"
        s += "\n       +----------+\n"
        return s
