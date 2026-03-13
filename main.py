import math
import matplotlib.pyplot as plt


# ==========================================
# CONSTANTES
# ==========================================

AIR_DENSITY = 1.155  # kg/m³

# Coeficientes de volume de cauda
HORIZONTAL_TAIL_VOLUME = 0.5
VERTICAL_TAIL_VOLUME = 0.04

TAIL_CHORD = 0.3  # corda da cauda (m)

# Braços de momento da cauda
LHT = 1.90
LVT = 1.90

# Intervalos de projeto
EH_PERCENT_MIN = 40
EH_PERCENT_MAX = 45

AILERON_CHORD_MIN = 0.15
AILERON_CHORD_MAX = 0.25

AILERON_SPAN_MIN = 0.5
AILERON_SPAN_MAX = 0.7

RUDDER_CHORD_MIN = 0.25
RUDDER_CHORD_MAX = 0.50

ELEVATOR_CHORD_MIN = 0.25
ELEVATOR_CHORD_MAX = 0.50

# Nomenclaturas
# Bw = Envergadura da asa
# Cw = Corda da asa
# Sw = Área da asa
# EH = ESTABILIZADOR HORIZONTAL
# EV = ESTABILIZADOR VERTICAL

def lst_media(lst):
    media = sum(lst) / len(lst)
    return media


def angulo_deflexao():
    lista = []
    for x in range(0, 1451, 25):
        if x != 1250:
            lista.append(x / 100)
    return lista


def graficos(Lmedcos, Cn, L, fmed):
    # Construindo o gráfico Cn x Sustentação
    plt.figure(1)                                 # Figura 1
    plt.plot(Cn, L, color='blue', linewidth=2)
    plt.title("Cn x Sustentação")                 # Título
    plt.xlabel("Cn")                              # Label x
    plt.ylabel("Sustentação")                     # Label y
    plt.show()

    # Construindo o gráfico Área x Sustentação
    plt.figure(2)                                 # Figura 2
    plt.plot(fmed, Lmedcos, color='green', linewidth=2)
    txt = "Área da superfície de controle / Área da superfície sustentadora"
    plt.title(txt)                                # Título
    plt.xlabel("Área defletida do leme")          # Label x
    plt.ylabel("Sustentação")                     # Label y
    plt.grid()
    plt.show()


def config_controle(B_EH, C_EH, CM_EV, Cm_EV, H_EV, B_Aileron,
                    C_Aileron, B_Leme, C_Leme, B_Profundor, C_Profundor):
    print("\n\nConfigurações do EH: (B x C)\n")
    for i in range(len(B_EH)):
        print("  Config.", i + 1, ":", B_EH[i], "x", C_EH[i], "m")

    print("\nConfigurações do EV: (CM x Cm x H)\n")
    for i in range(len(CM_EV)):
        print("  Config.", i + 1, ":",
              CM_EV[i], "x", Cm_EV[i], "x", H_EV[i], "m")

    print("\nConfigurações do Aileron: (B x C)\n")
    print("  (min)", B_Aileron[0], "x", C_Aileron[0], "m")
    print("  (max)", B_Aileron[1], "x", C_Aileron[1], "m")

    print("\nConfigurações do Leme: (B x C)")
    for i in range(len(B_Leme)):
        print("\n  Config.", i + 1, "do Leme:")
        print("    (min):", B_Leme[i], "x", C_Leme[0], "m")
        print("    (max):", B_Leme[i], "x", C_Leme[1], "m")

    print("\nConfigurações do Profundor: (B x C)")
    for i in range(len(B_Profundor)):
        print("\n  Config.", i + 1, "do Profundor:")
        print("    (min):", B_Profundor[i], "x", C_Profundor[0], "m")
        print("    (max):", B_Profundor[i], "x", C_Profundor[1], "m")


def volumes_cauda(Sht, Svt):
    print("\n\nÁreas de cauda:\n", "  Sht: ", Sht, "\n", "  Svt: ", Svt, "\n")


def main():
    print("Bem-vindo ao código Enterprise.")

    # Definindo angulos do leme
    ang = angulo_deflexao()

    # Recebendo medidas
    Cw = float(input("Digite o valor da Corda da asa: "))                 # m
    Bw = float(input("Digite o valor da Envergadura da asa: "))           # m
    V = float(input("Digite a velocidade da aeronave: "))                 # m/s

    Sw = Bw * Cw
    Sht = round(((HORIZONTAL_TAIL_VOLUME * Cw * Sw) / LHT), 5)
    Svt = round(((VERTICAL_TAIL_VOLUME * Bw * Sw) / LVT), 5)

    # Declarando listas de envergadura e corda
    cordaEH = []
    envergaduraEH = []
    cordaMaiorEV = []
    cordaMenorEV = []
    alturaEV = []

    cordaAileron = []          #
    envergaduraAileron = []    #
    cordaLeme = []             # Não sabíamos os nomes corretos das medidas
    envergaduraLeme = []       # do Aileron, Leme e Profundor, então optamos
    cordaProfundor = []        # por colocar corda e envergadura
    envergaduraProfundor = []  # 

    areaLeme = []

    Lmin = []     #
    Lmed = []     # sustentação mínima, média e máxima
    Lmax = []     #

    Lmincos = []  # 
    Lmedcos = []  # sustentação projetada no plano lateral (sin)
    Lmaxcos = []  # 

    # Calculando medidas dos estabilizadores
    for i in range(EH_PERCENT_MIN, EH_PERCENT_MAX + 1):
        # Estabilizador Horizontal
        CEH = round(math.sqrt(Sht * i / 100), 4)  # Corda do EH
        BEH = round(Sht / CEH, 4)  # Envergadura do EH
        cordaEH.append(CEH)
        envergaduraEH.append(BEH)
        # Envergadura do Profundor = Envergadura do EH
        envergaduraProfundor.append(BEH)

        # Estabilizador Vertical
        CMEV = CEH  # Corda Maior EV = Corda EH
        cordaMaiorEV.append(CMEV)
        CmEV = round(CMEV * 0.65, 4)  # Corda menor EV
        h = round((2 * Svt / (CMEV + CmEV)), 4)  # h = Altura do EV
        cordaMenorEV.append(CmEV)
        alturaEV.append(h)
        # Envergadura do Leme = 90% da Altura do EV
        bLeme = round(0.90 * h, 4)  # Envergadura do Leme
        envergaduraLeme.append(bLeme)

    # Calculando medidas dos Ailerons
    cAmin = AILERON_CHORD_MIN * Cw  # Corda do Aileron mínima = 15%
    cAmax = AILERON_CHORD_MAX * Cw  # Corda do Aileron máxima = 25%
    cordaAileron.append(cAmin)
    cordaAileron.append(cAmax)
    bAmin = AILERON_SPAN_MIN * Bw / 2  # Envergadura do Aileron mínima = 50%
    bAmax = AILERON_SPAN_MAX * Bw / 2  # Envergadura do Aileron máxima = 70%
    envergaduraAileron.append(bAmin)
    envergaduraAileron.append(bAmax)

    # Calculando medidas do Leme e do Profundor
    cLmin = RUDDER_CHORD_MIN * TAIL_CHORD  # Corda do Leme mínima
    cLmax = RUDDER_CHORD_MAX * TAIL_CHORD  # Corda do Leme máxima
    cordaLeme.append(cLmin)
    cordaLeme.append(cLmax)
    cPmin = ELEVATOR_CHORD_MIN * TAIL_CHORD  # Corda do Profundor mínima
    cPmax = ELEVATOR_CHORD_MAX * TAIL_CHORD  # Corda do Profundor máxima
    cordaProfundor.append(cPmin)
    cordaProfundor.append(cPmax)

    # Calculando área do Leme
    aLmin = round(cordaLeme[0] * envergaduraLeme[0], 4)
    aLmed = round(lst_media(cordaLeme) * lst_media(envergaduraLeme), 4)
    aLmax = round(cordaLeme[1] * envergaduraLeme[0], 4)
    areaLeme.append(aLmin)
    areaLeme.append(aLmed)
    areaLeme.append(aLmax)

    # Calculando Area do Leme * cos(w)
    fmin = []
    fmed = []
    fmax = []
    for x in ang:
        fmin.append(areaLeme[0] * math.sin(math.radians(x)))
        fmed.append(areaLeme[1] * math.sin(math.radians(x)))
        fmax.append(areaLeme[2] * math.sin(math.radians(x)))

    # Calculando sustentação
    with open("Cl (A x L).txt") as Cl:
        listaCl = []
        for linha in Cl:
            listaCl.append(float(linha.replace("\n", "")))

        for x in range(len(listaCl)):
            L = (AIR_DENSITY * V * V * areaLeme[0] * listaCl[x]) / 2
            Lmin.append(L)
            L = (AIR_DENSITY * V * V * areaLeme[1] * listaCl[x]) / 2
            Lmed.append(L)
            L = (AIR_DENSITY * V * V * areaLeme[2] * listaCl[x]) / 2
            Lmax.append(L)

        for i in range(min(len(Lmin), len(ang))):
            Lmincos.append(Lmin[x] * math.sin(math.radians(ang[x])))
            Lmedcos.append(Lmed[x] * math.sin(math.radians(ang[x])))
            Lmaxcos.append(Lmax[x] * math.sin(math.radians(ang[x])))

    # Calculando segunda lista de sustentação
    with open("Cl (Cn x L).txt") as Cl:
        listaSus = []
        listaCl = []
        for linha in Cl:
            listaCl.append(float(linha.replace("\n", "")))

        for x in listaCl:
            L = (AIR_DENSITY * V * V * 0.045 * x) / 2
            listaSus.append(L)

    # Importanto dados do arquivo Cn.txt
    with open("Cn.txt") as Cn:
        listaCn = []
        for linha in Cn:
            listaCn.append(float(linha.replace("\n", "")))

    while True:
        print("\nSelecione uma opção (digite o número correspondente):")
        print("    [0] - Áreas de cauda (Sht, Svt)")
        print("    [1] - Dimensões das superfícies de controle")
        print("    [2] - Gráfico das superfícies")
        print("    [3] - Sair")
        option = input("Sua escolha: ")

        if option == "0":
            volumes_cauda(Sht, Svt)
        elif option == "1":
            config_controle(envergaduraEH, cordaEH, cordaMaiorEV, cordaMenorEV,
                            alturaEV, envergaduraAileron, cordaAileron,
                            envergaduraLeme, cordaLeme, envergaduraProfundor,
                            cordaProfundor)
        elif option == "2":
            graficos(Lmedcos, listaCn, listaSus, fmed)
        elif option == "3":
            print("\nObrigado por usar o software de controle Enterprise 2021")
            print("Eliaquim e Giovanni 2021")
            break
        elif option == "4":
            print(cordaLeme)
            print(envergaduraLeme)
            print(areaLeme)


main()
