from Placar import Placar

NRODADAS = 10
# PARA ALTERAR A FORMA COMO A CLASSE É MOSTRADA NO COMANDO PRINT()
# VOCÊ TEM QUE DAR OVERRIDE NA PROPRIEDADE __repr__ DA SUA CLASSE. EX.:
# class oi:
#   def __repr__(self):
#       return "eba"
# teste = oi()
# print(teste) -> eba


def main():
    seed = int(input("Digite a semente (zero para aleatório): "))
    # rd = RolaDados(5, seed)
    pl = Placar()
    print(pl)
    for rodada in range(0, NRODADAS):
        print("****** Rodada ", (rodada + 1), sep="")
        input("Pressione ENTER para lançar os dados")
        # primeira tentativa
        # rd.rolar()
        print("1          2          3          4          5")
        # print(rd)

        # segunda tentativa
        muda = input(
            "Digite os números dos dados que quiser TROCAR. Separados por espaços."
        )
        # rd.rolar(muda)
        print("1          2          3          4          5")
        # print(rd)

        # terceira tentativa
        muda = input(
            "Digite os números dos dados que quiser TROCAR. Separados por espaços."
        )
        # values = rd.rolar(muda)
        print("1          2          3          4          5")
        # print(rd)

        print("\n\n")
        print(pl)

        pos = 0
        while pos <= 0:
            try:
                pos = int(
                    input("Escolha a posição que quer ocupar com essa jogada ===> ")
                )
                if pos > NRODADAS or pos <= 0:
                    pos = 0
                # pl.add(pos, values)
            except:
                pos = 0
            if pos == 0:
                print("Valor inválido. Posição ocupada ou inexistente.")

        print("\n\n")
        print(pl)

    print("***********************************")
    print("***")
    print("*** Seu escore final foi: ", pl.getScore(), sep="")
    print("***")
    print("***********************************")


if __name__ == "__main__":
    main()
