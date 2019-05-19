from random import randint
class cpf:
    def gerar(self):
        dig1 = 1
        while (dig1 != 0):
            dig1 = randint(0,9)
            dig2 = randint(0,9)
            dig3 = randint(0,9)
            dig4 = randint(0,9)
            dig5 = randint(0,9)
            dig6 = randint(0,9)
            dig7 = randint(0,9)
            dig8 = randint(0,9)
            dig9 = randint(0,9)

        total = (dig1 * 10) + (dig2 * 9) + (dig3 * 8 ) + (dig4 * 7) + (dig5 * 6) + (dig6 * 5 ) + (dig7 * 4) + (dig8 * 3) + (dig9 * 2 )
        divisao = total % 11

        if (divisao < 2):
            dig10 = 0
        else:
            dig10 = 11 - divisao

        total2 = (dig1 * 11) + (dig2 * 10) + (dig3 * 9 ) + (dig4 * 8) + (dig5 * 7) + (dig6 * 6 ) + (dig7 * 5) + (dig8 * 4) + (dig9 * 3 ) + (dig10 * 2 )
        divisao2 = total2 % 11
        if(divisao2 < 2):
            dig11 = 0
        else:
            dig11 = 11 - divisao2

        return str(dig1) + str(dig2) + str(dig3) + "." + str(dig4) + str(dig5) + str(dig6) + "." + str(dig7) + str(dig8) + str(dig9) + "-" + str(dig10) + str(dig11)