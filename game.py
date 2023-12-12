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
    spelare = ["din själ"]

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

    global trafik
    trafik = 0

    global riktning
    riktning = 0

    global tunnel
    tunnel = ""

    global inspektion
    inspektion = ""

    global vampyren
    vampyren = ""

    global stash
    stash = ""

    global räkning
    räkning = 0

    global hittad
    hittad = 0
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
            global val
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
        global val
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
        gatan()

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
            global val
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
    

def gatan():
    global trafik
    trafik = input("""
    Du står framför ett övergångställe
    för:    skriv:
    Gå över: 1
    Vänta : 2
    """)
    while trafik == "1":
        global val
        val = input("""
            Ending: påkörd
            för:    skriv:
            börja om: 0
            """)
        if val == "0":
            start()
    while trafik == "2":
        print("Vilken tur att du väntade, den föraren var in lämpad för bilar")
        parken()

def parken():
    global riktning
    riktning = input("""
    du står nu i en park, mot skogen finns en grotta, mot staden finns en öppning till undermarken, vart vill du gå?
    för:   skriv:
    grottan: 1
    Staden: 2
    Stanna: 3
    """)
    
    while riktning == "3":
        global val
        val = input("""
        du sitter och njuter av solens värme och fåglarnas dova bakgrunds tvitter
        Ending: Mental health
        för:    skriv:
        börja om: 0
        """)
        if val == "0":
            start()

    while riktning == "1":
        print("du ramlar ner i grottan")
        grottan()

    while riktning == "2":
        kloaken()

def grottan():
    global tunnel
    tunnel = input("""
    efter ett tag delar grottan sig i två,
    vart vill du gå?
    för:    skriv:
    höger:    1
    vänster:  2
    """)
    if tunnel == "1":
        borgen()
    if tunnel == "2":
        mötesplattsen()

def borgen():
    global inspektion
    inspektion = input("""
    tillslut kommer du fram till en borg i grottan,
    utanför ligger en kristall, vad vill du?
    för: skriv:
    återvänd: 1
    inbrott: 2
    kolla på kristallen: 3
    """)
    if inspektion == "1":
        grottan()
    while inspektion == "3":
        global spelare
        global hittad
        hittad = spelare.count("inteligens")
        if hittad > 0:
            print("""
            du är smart nog att inse att kristallen är gjord av trä,
            detta är ju inte alls en kristall, det är en påle.
            """)
            spelare = spelare + ["träpåle"]
            print(f"du har {spelare}")
            inspektion = input("""
                tillslut kommer du fram till en borg i grottan,
                utanför ligger en kristall, vad vill du?
                för: skriv:
                återvänd: 1
                inbrott: 2
                """)
            global räkning
            räkning = räkning +1
        else:
            print("du är inte smart nog för att förstå kristallen")
            inspektion = input("""
                tillslut kommer du fram till en borg i grottan,
                utanför ligger en kristall, vad vill du?
                för: skriv:
                återvänd: 1
                inbrott: 2
                """)
    while inspektion == "2":
        print("""
        du forstätter frammåt in i mörkret,
        innan du hinner reagera flyger något från skuggorna mot dig,
        det bränner till i din hals vilket sprider sig genom dina blodådror till hela kroppen
        """)
        spelare = spelare + ["vampirism"]
        spelare.remove("din själ")
        print(f"du har {spelare}")
        global vampyren

        vampyren = input("""
        BOSS FIGHT: vampyren
        för:                  skriv:
        ge upp:                 1
        lökig andedräkt:        2
        träpåle i dess hjärta: 3
        """)
        if vampyren == "1":
            global val
            val = input("""
            Ending: upäten av vampyr
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()

        if vampyren == "2":
            val = input("""
            att vampyrer dör av lök är en myt.
            Ending: upäten av vampyr
            för:    skriv:
            börja om: 0
            """)
            if val == "0":
                start()
    

        while vampyren == "3":
            global tunnel
            for i in spelare:
                if i == "träpåle":
                    global stash
                    stash = input("""
                    vampyre, presis som alla andra, dör om man spettsar dem i hjärtat.
                    Bakom vapyren hittar du en klump med spagetti ett piller och en laddad pistol:
                    för:          skriv:
                    ta grejerna:    1
                    lämna grejerna: 2
                    """)
                if stash == "1":
                    droger = droger + ["piller"]
                    print(f"du har tagit drogerna {droger}")
                    spelare = spelare + ["spagetti"]
                    spelare = spelare + ["pistol"]
                    print(f"du har {spelare}")

                    tunnel = input("""
                    vill du kika på andra sidan grottan eller vill du gå hem?
                    för:        skriv:
                    gå hem:       1
                    andra sidan:  2
                    """)

                if stash == "2":
                    tunnel = input("""
                    vill du kika på andra sidan grottan eller vill du gå hem?
                    för:        skriv:
                    gå hem:       1
                    andra sidan:  2
                    """)
            else:
                val = input("""
                du har ingen träpåle
                Ending: upäten av vampyr
                för:    skriv:
                börja om: 0
                """)
                if val == "0":
                    start()

            
            if tunnel == "1":
                print("du har sätt något du inte borde ha sätt")
                for i in spelare:
                    if i == "vampirism":
                        print("""
                        dina nya vampyr krafter låter dig ducka undan från skotten något skutit mot dig,
                        bara en bra stund efter du flytt in i skogen inser du att din hud fräter,
                        """)
                        val = input("""
                            Ending: vampyr
                            för:    skriv:
                            börja om: 0
                            """)
                        if val == "0":
                            start()
                    else: val = input("""
                        Ending: skuten
                        för:    skriv:
                        börja om: 0
                        """)
                    if val == "0":
                        start()
            if tunnel == "2":
                mötesplattsen()





def mötesplattsen():
    g


def kloaken():
    f
#dra igång allt
start()