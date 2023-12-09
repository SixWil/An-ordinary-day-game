# test

#imports
import os

#resett
def reset():
    global val
    val = ""

    global tid
    tid = 0

    global vakenhet
    vakenhet = ""

    global frukost
    frukost = ""

    global dagsplan
    dagsplan = ""

    global droger
    droger = []

    global tunnan
    tunnan = ""

    global spelare
    spelare = []

    global skolval
    skolval = ""

    global koridor
    koridor = ""

    global vapen
    vapen = ""

    global böcker
    böcker = ""

    global läst
    läst = 0
#Start
försök = 0

def start():
    while True:
        reset()
        os.system('cls')

        global försök
        försök = försök + 1
        print(f"""
        AN ORDINARY DAY
        försök {försök}
        """)

        sovrum()

# sovrum
def sovrum():
    global vakenhet
    global tid

    vakenhet = input("""
    du vaknar, vad gör du?
    för:    skriv:
    Somna om: 1.
    Gå upp: 2.
    """)

    while vakenhet == "1":
        if tid < 9:
            tid = tid+1
            print(f"du somnar om {tid} gången")
            sovrum()

        while tid == 9:
            print("""
            på labbet sitter en överarbetad arbetare,
            det är kväll och han skulle egentligen fått åka hem för många timmar sedan.
            Han ställer sig upp för att gå och hämta ännu en kopp kaffe,
            han märker inte att en sladd har virat sig runt hans ben och när han går rycker han den från servern.
            Servern med namnet "vintergatan" slocknar.
            """)
            val = input("""
            Ending: Oopsy!
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()
        
    while vakenhet == "2":
        while 5 > tid > 2:
            print("""
            Du vaknar i nån slags pod, en alien märker att du vaknat.
            Det trycker på en knapp och metaliska klor kommer ut ur väggarna... och in i dig.
            """)
            val = input("""
            Ending: skördad
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()

        while tid > 4 :
            print("""
            Du vaknar på en grå planet täck av damm... det finns inget kvar.
            """)
            val = input("""
            Ending: Wasteland
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()
        
        if tid < 3:
            print("du går till köket för att äta frukost")
            köket()

# köket
def köket():
    global frukost
    frukost = input("""
    I köket står en svart tunna med en toxic waste symbol på,
    den osar en grön gas.
    bakom ugnen ligger en macka som varit där så länge du kan minnas.
    Ur skafferiet nästan lyser ett fantastiskt paket med smaskiga cornflakes från kellogs.
    vad gör du för frukost?
    för:              skriv:
    sniffa på tunnan:   1
    Mackan:             2
    kellogs corflakes™: 3
    """)
    if frukost == "2":
        print("Mycket dåligt val")
        hallen()

    if frukost == "3":
        print("Mycket bra val")
        hallen()

    if frukost == "1":
        global droger
        for i in droger:
            if i == "gas":
                droger.remove("gas")
        droger = droger + ["gas"]
        print(f"du har tagit drogerna {droger}")

        while frukost == "1":
            global tunnan
            tunnan = input("""
            Hela världen snurrar och du kan inte skilja upp och ned, det känns ganska bra.
            för:                    skriv:
            Quit while youre ahead:   1
            Drick gift (som en idiot) 2
            """)

            if tunnan == "1":
                köket()
            if tunnan == "2":
                global spelare
                spelare = spelare + ["cancer"]
                print(f"du har {spelare}")
                hallen()

# hallen
def hallen():
    global dagsplan
    dagsplan = input("""
        du funderar på vad du vill göra idag
        för:            skriv:
        gå till skolan:   1
        gå ut på äventyr: 2
        stanna hemma:     3
        """)

    while dagsplan == "3":
        print("Du stannar hemma och chillar hela dagen")
        val = input("""
            Ending: Gött!
            för:    skriv:
            börja om: 0
            """)
        if val == "0":
            start()

    while dagsplan == "1":
        global skolval
        skolval = input("""
        Det är söndag... skolan är stängd.
        Vill du försöka ta dig in ändå?
        för:       skriv:
        inbrott:     1
        gå hem igen: 2
        """)
        if skolval == "2":
            hallen()
        if skolval == "1":
            skolan()

    if dagsplan == "2":
        parken()

def skolan():
    global val
    global koridor
    koridor = input("""
    du går runt i skolans koridorer, du kan fortsätta framåt, vika in till bilblioteket eller vända om.
    för:            skriv:
    Vänd om:          1
    fortsätt frammåt: 2
    Biblioteket:      3
    """)
    if koridor == "1":
        hallen()
    if koridor == "2":
        print("du stormar in ett kontor, en lärare har hört dig och kommer ut ur sitt näste.")
        global vapen
        vapen = input("""
        BOSS FIGHT: Magister V. Nordlund
        för:                 skriv:
        Ge upp:                1
        psychological warfare: 2
        """)
        while vapen == "1":
            val = input("""
            Ending: Kvarsittning
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()
        while vapen == "2":
            global spelare
            for i in spelare:
                if i == "inteligens":
                    print("du är inte korkad nog att besegra läraren")
                    val = input("""
                    Ending: Kvarsittning
                    för:    skriv:
                    börja om: 0
                    """)
                    if val == "0":
                        start()
                
            print("du säger något så dumt att lärarens huvud exploderar")
            val = input("""
            Ending: Fängelse
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()
    if koridor == "3":
        for i in spelare:
            if i == "inteligens":
                print("det finns inget mer att lära sig i biblioteket")
                skolan()
        else: biblioteket()

def biblioteket():
    global böcker
    böcker = input("""
    Du sätter dig i bibloteket
    för:              skriv:
    läs böcker en stund: 1
    lämna biblioteket:   2
    """)
    if böcker == "2":
        skolan()
    if böcker == "1":
        global läst
        läst = läst +1
        print(f"""
        du har läst böcker i {läst} stund(er)
        """)
        if läst == 10:
            print("du har läst alla böckerna")
            global spelare
            spelare = spelare + ["inteligens"]
            print(f"du har {spelare}")
            skolan()
        if läst != 10:
            biblioteket()
    

def parken():
    p

#dra igång allt
start()