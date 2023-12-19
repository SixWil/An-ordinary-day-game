# programmet är skrivet lite som en rysk docka i att det är funktioner i funktioner i funktioner,
# detta så att progrommet alltid ska ha någonting att falla tillbaka till om användaren ger ett oregistererat värde till en input.

#imports
import os

#Variabler
global ending
ending = []

#resett
def reset():
    os.system('cls')

    global intro
    intro = ""
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

    global läraren
    läraren = ""

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

    global galler
    galler = ""

    global antiklimax
    antiklimax = ""

    global gurg
    gurg = ""

    global romans
    romans = ""

    global agent
    agent = ""

    global gurg_the_groom
    gurg_the_groom = ""

    global nekad
    nekad = ""

    global sim
    sim = ""

    global respekt
    respekt = ""

#Start
försök = 0
def tutorial():
    global intro
    os.system('cls')
    while True:
        intro = input("""
        Hej! Välkommen till Sixten Wilde och Sigge Nilssons Spel:
         ______                          _ _             _             
        |  ____|                        | (_)           | |            
        | |__   _ __   __   ____ _ _ __ | |_  __ _    __| | __ _  __ _ 
        |  __| | '_ \  \ \ / / _` | '_ \| | |/ _` |  / _` |/ _` |/ _` |
        | |____| | | |  \ V / (_| | | | | | | (_| | | (_| | (_| | (_| |
        |______|_| |_|   \_/ \__,_|_| |_|_|_|\__, |  \__,_|\__,_|\__, |
                                              __/ |               __/ |
        (Körs i fullskärmsläge)              |___/               |___/ 
        Spelet är designat för att köras flera gånger och därför kan du alltid starta om genom att skriva: 0.
        För att välja en handling skriv dess siffra längst ned i konsollen (detta är i konsollen) och tryck på return (ny rad knappen), till exempel:

        Starta: 1
        """)
        if intro == "1":
            start()

#starta och starta om programmet
def start():
    "resettar programmet, initsierar sovrummet"
    while True:
        global ending
        global försök
        försök = försök + 1

        reset()
        global spelare
        spelare = ["din själ"]

        print(f"""
        EN VANLIG DAG
        försök: {försök}
        """)

    #   Endings kvar: {18-{len(ending)}}/18
    

        sovrum()

# Sovrum
def sovrum():
    "start rum, inget speciellt"
    while True:
        global vakenhet
        global tid

        vakenhet = input("""
        du vaknar, vad gör du?

        Somna om: 1.
        Gå upp: 2.
        """)
        os.system('cls')

        if vakenhet == "0":
            start()
        while vakenhet == "1":
            if tid < 9:
                tid = tid+1
                print(f"""
                du somnar om {tid} gången
                """)
                sovrum()

            while tid == 9:
                print("""
                på labbet sitter en överarbetad arbetare och jobbar med en server,
                han skulle egentligen fått åka hem för många timmar sedan.
                på en annan server börjar en lampa blinka vilket betyder att något importerats?
                han ställer sig upp för att se vad som hänt,
                han märker inte att en sladd har virat sig runt hans ben,
                när han går rycks den ur servern han jobbat på.
                Servern med namnet "vintergatan" slocknar.
                """)
                global val
                global ending
                if ending.count("Oopsy!") == 0:
                    ending = ending + ["Oopsy!"]
                val = input(f"""
                ({len(ending)}/18)
                Ending: Oopsy!
                
                börja om: 0
                """)
                if val == "0":
                    start()
            
        while vakenhet == "2":
            if tid > 3:
                print("du har snoozat så länge att världen omkring dig har förändrats")
            while 5 > tid > 2:
                print("""
                Du vaknar i nån slags pod, en alien märker att du vaknat.
                Det trycker på en knapp och metaliska klor kommer ut ur väggarna... och in i dig.
                """)
                if ending.count("skördad") == 0:
                    ending = ending + ["skördad"]
                val = input(f"""
                ({len(ending)}/18)
                Ending: skördad
            
                börja om: 0
                """)
                if val == "0":
                    start()

            while tid > 4 :
                print("""
                Du vaknar på en grå planet täck av damm... det finns inget kvar.
                """)
                if ending.count("Wasteland") == 0:
                    ending = ending + ["Wasteland"]
                val = input(f"""
                ({len(ending)}/18)
                Ending: Wasteland
            
                börja om: 0
                """)
                if val == "0":
                    start()
            
            if tid < 3:
                print("du går till köket för att äta frukost")
                köket()
#Köket
def köket():
    "köket, här kan du välja frukost, har liten effekt på spelets slut"
    global frukost
    frukost = input("""
    I köket står en svart tunna med en hazard symbol på,
    den osar en grön gas.
    bakom ugnen ligger en macka som varit där så länge du kan minnas.
    Ur skafferiet nästan lyser ett fantastiskt paket med smaskiga cornflakes från kellogs.
    vad gör du för frukost?

    sniffa på tunnan:   1
    Mackan:             2
    kellogs cornflakes™: 3
    """)
    os.system('cls')
    if frukost == "0":
        start()

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

            Quit while youre ahead:   1
            Drick gift (som en idiot) 2
            """)
            os.system('cls')

            if tunnan == "0":
                start()
            if tunnan == "1":
                köket()
            if tunnan == "2":
                global spelare
                spelare = spelare + ["cancer"]
                print(f"du har {spelare}")
                hallen()
#Hallen
def hallen():
    "vilken ordning vill du utforska världen, korrekt är först skolan sedan äventyr, stanna hemma ger en ending"
    global dagsplan
    dagsplan = input("""
        du funderar på vad du vill göra idag

        gå till skolan:   1
        gå ut på äventyr: 2
        stanna hemma:     3
        """)
    os.system('cls')

    if dagsplan == "0":
        start()
    while dagsplan == "3":
        print("Du stannar hemma och chillar hela dagen")
        global val
        global ending
        if ending.count("Gött!") == 0:
            ending = ending + ["Gött!"]
        val = input(f"""
            ({len(ending)}/18)
            Ending: Gött!
        
            börja om: 0
            """)
        if val == "0":
            start()

    while dagsplan == "1":
        global skolval
        skolval = input("""
        Det är söndag... skolan är stängd.
        Vill du försöka ta dig in ändå?

        inbrott:     1
        gå hem igen: 2
        """)
        os.system('cls')
        if skolval == "0":
            start()
        if skolval == "2":
            hallen()
        if skolval == "1":
            skolan()

    if dagsplan == "2":
        gatan()

#skolan
def skolan():
    "i skolan kan du uppnå inteligens, det kommer du behöva senare, går du för långt får du en ending"
    global val
    global koridor
    koridor = input("""
    du går runt i skolans koridorer, du kan fortsätta framåt, vika in till bilblioteket eller vända om.

    Vänd om:          1
    fortsätt frammåt: 2
    Biblioteket:      3
    """)
    os.system('cls')
    if koridor == "0":
        start()
    if koridor == "1":
        hallen()
    if koridor == "2":
        print("du stormar in ett kontor, en lärare har hört dig och kommer ut ur sitt näste.")
        global läraren
        läraren = input("""
        BOSS FIGHT: Magister V. Nordlund

        Ge upp:                1
        psychological warfare: 2
        """)
        os.system('cls')
        if läraren == "0":
            start()
        while läraren == "1":
            global val
            global ending
            if ending.count("Kvarsittning") == 0:
                ending = ending + ["Kvarsittning"]
            val = input(f"""
            ({len(ending)}/18)
            Ending: Kvarsittning
        
            börja om: 0
            """)
            if val == "0":
                start()
        while läraren == "2":
            global spelare
            for i in spelare:
                if i == "inteligens":
                    print("du är inte korkad nog att besegra läraren")
                    if ending.count("Kvarsittning") == 0:
                        ending = ending + ["Kvarsittning"]
                    val = input(f"""
                    ({len(ending)}/18)
                    Ending: Kvarsittning
                
                    börja om: 0
                    """)
                    if val == "0":
                        start()
                
            print("du säger något så dumt att lärarens huvud exploderar")
            if ending.count("Fängelse") == 0:
                ending = ending + ["Fängelse"]
            val = input(f"""
            ({len(ending)}/18)
            Ending: Fängelse
        
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

#biblioteket
def biblioteket():
    "läs 3 böcker för att bli smart, läser du 10 kommer bibliotikaren"
    global läst
    global böcker
    while True:
        böcker = input(f"""
        Du sätter dig i bibloteket

        läs:               1
        lämna biblioteket: 2
        """)
        os.system('cls')

        if böcker == "0":
            start()

        if böcker == "2":
            skolan()

        if böcker == "1":
            läst = läst + 1
            print(f"""
            du har läst i {läst} stund(er)
            """)
            
            while läst == 3:
                global spelare
                if spelare.count("inteligens") == 0:
                    spelare = spelare + ["inteligens"]

                print(f"""
                du har läst klart boken.
                du har: {spelare}
                """)

                global nörd
                nörd = input("""
                Vill du läsa mer eller lämna biblioteket?
                Lämna: 2
                Fortsätt: 3
                """)
                os.system('cls')

                if nörd == "2":
                    skolan()
                if nörd == "3":
                    läst = läst + 1
                    print(f"""
                    du har läst böcker i {läst} stund(er)
                    """)
                
            if läst != 10:
                biblioteket()
            if läst == 10:
                global respekt
                respekt = input("""
                Ur en hög böcker vaknar en biblotikarie, du får inte vara här idag
                BOSS FIGHT: biblotikarien

                var tyst i bilbioteket: 2
                skrik och slamra:       3
                """)
                os.system('cls')
                if respekt == "0":
                    start()
                if respekt == "2":
                    print("""
                    "eh, du läser ju faktiskt riktiga böcker"
                    hon låter dig slippa undan
                    """)
                    skolan()
                if respekt == "3":
                    global ending
                    if ending.count("karma") == 0:
                        ending = ending + ["karma"]
                    val = input(f"""
                    din ligism gör att biblioteket reagerar våldamt,
                    en hylla tippar över och krossar dig
                    ({len(ending)}/18)
                    Ending: karma
                
                    börja om: 0
                    """)
                    if val == "0":
                        start()  

#övergångstället
def gatan():
    "detta är bara för att retas, fyller ingen funktion alls."
    global trafik
    trafik = input("""
    Du står framför ett övergångställe

    Gå över: 1
    Vänta : 2
    """)
    os.system('cls')
    if trafik == "0":
        start()
    while trafik == "1":
        global val
        global ending
        if ending.count("påkörd") == 0:
            ending = ending + ["påkörd"]
        val = input(f"""
            ({len(ending)}/18)
            Ending: påkörd
        
            börja om: 0
            """)
        if val == "0":
            start()
    while trafik == "2":
        print("Vilken tur att du väntade, den föraren var inte lämpad för bilar")
        parken()

#vägvalet
def parken():
    "här får du välja riktning igen, korrekt är grottan först sedan staden, stanna ger en ending"
    global riktning
    riktning = input("""
    du står nu i en park, mot skogen finns en grotta, mot andra sidan finns en öppning till tunnlarna under staden, vart vill du gå?

    grottan: 1
    Staden: 2
    Stanna: 3
    """)
    os.system('cls')
    if riktning == "0":
        start()
    while riktning == "3":
        global val
        global ending
        if ending.count("Mental health") == 0:
            ending = ending + ["Mental health"]
        val = input(f"""
        du sitter och njuter av solens värme och fåglarnas dova bakgrunds tvitter
        ({len(ending)}/18)
        Ending: Mental health
    
        börja om: 0
        """)
        if val == "0":
            start()

    while riktning == "1":
        print("du ramlar ner i grottan")
        grottan()

    while riktning == "2":
        kloaken()

#grottan
def grottan():
    "här kan du gå vänster till staden ändå, du ska gå till höger"
    global tunnel
    tunnel = input("""
    efter ett tag delar grottan sig i två,
    vart vill du gå?

    höger:    2
    vänster:  1
    """)
    os.system('cls')
    if tunnel == "0":
        start()
    if tunnel == "2":
        borgen()
    if tunnel == "1":
        mötesplattsen()

#vampyrens lya
def borgen():
    "här sloss du med vampyren, och får grejerna för att besegra gurg i staden, pålen krävs för att besegra vampyren, inteligens krävs för pålen."
    global inspektion
    inspektion = input("""
    tillslut kommer du fram till en borg i grottan,
    utanför ligger en kristall, vad vill du?

    återvänd: 1
    inbrott: 2
    kolla på kristallen: 3
    """)
    os.system('cls')
    if inspektion == "0":
        start()
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

                återvänd: 1
                inbrott: 2
                """)
            os.system('cls')
            if inspektion == "0":
                start()
            global räkning
            räkning = räkning +1
        else:
            print("du är inte smart nog för att förstå kristallen")
            inspektion = input("""
                tillslut kommer du fram till en borg i grottan,
                utanför ligger en kristall, vad vill du?

                återvänd: 1
                inbrott: 2
                """)
            os.system('cls')
            if inspektion == "0":
                start()
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

        ge upp:                 1
        lökig andedräkt:        2
        träpåle i dess hjärta: 3
        """)
        os.system('cls')
        if vampyren == "0":
            start()
        if vampyren == "1":
            global val
            global ending
            if ending.count("upäten av vampyr") == 0:
                ending = ending + ["upäten av vampyr"]
            val = input(f"""
            ({len(ending)}/18)
            Ending: upäten av vampyr
        
            börja om: 0
            """)
            if val == "0":
                start()

        if vampyren == "2":
            if ending.count("upäten av vampyr") == 0:
                ending = ending + ["upäten av vampyr"]
            val = input(f"""
            att vampyrer dör av lök är en myt.
            ({len(ending)}/18)
            Ending: upäten av vampyr
        
            börja om: 0
            """)
            if val == "0":
                start()
    

        while vampyren == "3":
            global tunnel
            if spelare.count("träpåle") > 0:
                global stash
                stash = input("""
                vampyrer, presis som alla andra, dör om man spettsar dem i hjärtat.
                Bakom vapyren hittar du en klump med spagetti ett piller och en laddad pistol:

                ta grejerna:    1
                lämna grejerna: 2
                """)
                os.system('cls')
                if stash == "0":
                    start()
                if stash == "1":
                    global droger
                    droger = droger + ["piller"]
                    print(f"du har tagit drogerna {droger}")
                    spelare = spelare + ["spagetti"]
                    spelare = spelare + ["pistol"]
                    print(f"du har {spelare}")

                    global tunnel
                    tunnel = input("""
                    vill du kika på andra sidan grottan eller vill du gå hem?

                    gå hem:       1
                    andra sidan:  2
                    """)
                    if tunnel == "0":
                        start()

                    if stash == "2":
                        tunnel = input("""
                        vill du kika på andra sidan grottan eller vill du gå hem?

                        gå hem:       1
                        andra sidan:  2
                        """)
                        os.system('cls')
            else:
                if ending.count("upäten av vampyr") == 0:
                    ending = ending + ["upäten av vampyr"]
                val = input(f"""
                du har ingen träpåle
                ({len(ending)}/18)
                Ending: upäten av vampyr
            
                börja om: 0
                """)
                if val == "0":
                    start()
            
            while tunnel == "1":
                print("du har sätt något du inte borde ha sätt")
                if spelare.count("vampirism") > 0: 
                    print("""
                    dina nya vampyr krafter låter dig ducka undan från skotten något skutit mot dig,
                    bara en bra stund efter du flytt in i skogen inser du att din hud fräter,
                    """)
                    if ending.count("vampyr") == 0:
                        ending = ending + ["vampyr"]
                    val = input(f"""
                        ({len(ending)}/18)
                        Ending: vampyr
                    
                        börja om: 0
                        """)
                    if val == "0":
                        start() 
                else:
                    if ending.count("skuten") == 0:
                        ending = ending + ["skuten"]
                    val = input(f"""
                    ({len(ending)}/18)
                    Ending: skuten
                
                    börja om: 0
                    """)
                if val == "0":
                    start()
            if tunnel == "2":
                mötesplattsen()
# där tunnlarna och grottorna möts
def mötesplattsen():
    "där grottan och kloaken möts, är du vampyr kan du gå igenom gallret och få en ending"
    print("""
    du ser att kloakerna leder ned i grottorna,
    det kan inte vara bra.
    """)
    global galler
    galler = spelare.count("vampirism")
    if galler > 0:
        global antiklimax
        antiklimax = input("""
        du kan använda dina vampyr krafter för att ta din igenom gallren, eller så kan du förtsätta frammåt

        genom gallret:    1
        fortsätt frammåt: 2
        """)
        os.system('cls')
        if antiklimax == "0":
            start()
        while antiklimax == "1":
            global ending
            if ending.count("MEH!") == 0:
                ending = ending + ["MEH!"]
            val = input(f"""
            du förvandlar dig till fladdermöss och flyger igenom gallret,
            på andra sidan ser du en skyllt där det står:
            "DEVELOPER NOTE: här finns det inget"
            du dog av antiklimax
            ({len(ending)}/18)
            Ending: MEH!
        
            börja om: 0
            """)
            if val == "0":
                start()
    
    kloaken()

#Stadens tunnlar
def kloaken():
    "under staden, du möter gurg, detta är sista scenen i spelet (om du gjort rätt)"
    global val
    print("""
    du fortsätter frammåt till du plöttsligt ser en siluett av vad du tror är en man, men något är off,
    det ser ut som att han smälter. Du snubblar och ljudet du gör för att återfå balansen ekar genom tunneln,
    figuren tittar på dig.
    """)
    global gurg
    while droger.count("piller") > 0:
        gurg = input("""
        BOSS FIGHT: gurg the ...guy?

        fly: 1
        blockera: 2
        dodge'a: 3
        spaghetti: 4
        pistol: 5
        vampyr kraft: 6
        """)
        os.system('cls')
        if gurg == "0":
            start()
        while gurg == "1":
            global ending
            if ending.count("upäten av gurg") == 0:
                ending = ending + ["upäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter up dig,
            ({len(ending)}/18)
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "2":
            if ending.count("upäten av gurg") == 0:
                ending = ending + ["upäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter up dig,
            ({len(ending)}/18)
            Ending: upäten av gurg

            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "3":
            if ending.count("upäten av gurg") == 0:
                ending = ending + ["upäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter up dig,
            ({len(ending)}/18)
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "5":
            if ending.count("upäten av gurg") == 0:
                ending = ending + ["upäten av gurg"]
            val = input(f"""
            Du plockar fram pistolen och skuter villt mot varelsen,
            du har avlossat alla skott i pistolen, några kulor träffar och gör skada... inte många nog.
            Motstånd är meningslöst,
            Gurg äter up dig,
            ({len(ending)}/18)
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()

        while gurg == "6":
            if ending.count("upäten av gurg") == 0:
                ending = ending + ["upäten av gurg"]
            val = input(f"""
            du flyger fram och biter gurg i halsen och ger honom vampirism,
            han biter dig i halsen tillbaka och ger dig död,
            ({len(ending)}/18)
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "4":
            global romans
            romans = input("""
            du gräppar frenetiskt efter något att och får fram spaghettin,
            du håller fram den som en sköld framför dig.
            Efter en liten stund öpnar du ögonen igen och ser att figuren rodnar,
            den har tagit spaghettin som en romantisk gest, och vänder sig om för att ge dig något i retur.

            vänta: 1
            SKUT:  2
            """)
            os.system('cls')

            if romans == "0":
                start()  

            while romans == "2":
                global agent
                agent =input("""
                du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skuter...
                PANG! *det piiiper i dina öron* omgivningen byter färg och varalsen faller ihop på golvet.
                Bakom dig för du att en person klappar händerna "imponerande",
                när du vänder dig om ser du en person i kostym,
                de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.
            
                acceptera: 1
                neka:      2
                """)
                os.system('cls')
                if agent == "0":
                    start()
                while agent == "1":
                    if ending.count("Bödeln") == 0:
                        ending = ending + ["Bödeln"]
                    val = input(f"""
                    "mycket bra val"
                    ({len(ending)}/18)
                    Ending: Bödeln
                
                    börja om: 0
                    """)
                    if val == "0":
                        start()
                while agent == "2":
                    print("""
                    "dåligt val"
                    Boss fight: agent K

                    """)
                    if ending.count("avrättad") == 0:
                        ending = ending + ["avrättad"]
                    input(f"""
                    PANG! *det isar i bröstet* innan du hinner reagera har agenten skutit dig...
                    "mycket dåligt val"
                    ({len(ending)}/18)
                    Ending: avrättad
                
                    börja om: 0
                    """)
                    if val == "0":
                        start()     

            while romans == "1":
                global gurg_the_groom
                gurg_the_groom = input("""
                gurg erbjuder dig en (självlysande) svamp som sin gåva til dig, vill du bli ihop med gurg?

                acceptera:     1
                neka:          2
                """)
                os.system('cls')
                if gurg_the_groom == "0":
                    start()
                while gurg_the_groom == "1":
                    while droger.count("gas") > 0:
                        global sim
                        sim = input("""
                        du har tagit alla tre droger och har därför blivigt uplyst,
                        du inser att du lever i en simulation... och att det finns andra serverar.

                        utforska: 1
                        återvänd: 2
                        """)
                        os.system('cls')
                        if sim == "0":
                            start()
                        if sim == "1":
                            if ending.count("destroyer of worlds") == 0:
                                ending = ending + ["destroyer of worlds"]
                            input(f"""
                            Det tar en stund att åka genom sladdarna,
                            när du väl anländer har den förra servern slocknat.
                            ({len(ending)}/18)
                            Ending: destroyer of worlds
                        
                            börja om: 0
                            """)
                            if val == "0":
                                start()
                        if sim=="2":
                            print("du återvänder till jorden")
                            break
                    if ending.count("gurg jn") == 0:
                        ending = ending + ["gurg jn"]
                    val = input(f"""
                    du och gurg lever lyckliga i alla era dagar.
                    ({len(ending)}/18)
                    Ending: Ordinary day 2?.. gurg jn the swamp monster vampire?
                
                    börja om: 0
                    """)
                    
                    if val == "0":
                        start()  

                while gurg_the_groom == "2":
                    global nekad
                    nekad = input("""
                    gurg ser förvirrad ut

                    vänta: 1
                    SKUT: 2
                    """)
                    os.system('cls')
                    if nekad == "0":
                        start()
                    while nekad == "1":
                        print("""
                        när han inser vad du gjort blir han förargad
                        """)
                        if ending.count("upäten av gurg") == 0:
                            ending = ending + ["upäten av gurg"]
                        val = input(f"""
                        Motstånd är meningslöst,
                        Gurg äter up dig,
                        ({len(ending)}/18)
                        Ending: upäten av gurg
                    
                        börja om: 0
                        """)
                        if val == "0":
                            start()
                    while nekad == "2":
                        agent =input("""
                        du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skuter...
                        PANG! *det piiiper i dina öron* omgivningen byter färg och varalsen faller ihop på golvet.
                        Bakom dig för du att en person klappar händerna "imponerande",
                        när du vänder dig om ser du en person i kostym,
                        de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.
                    
                        acceptera: 1
                        neka:      2
                        """)
                        os.system('cls')
                        while agent == "1":
                            if ending.count("Bödeln") == 0:
                                ending = ending + ["Bödeln"]
                            val = input(f"""
                            "mycket bra val"
                            ({len(ending)}/18)
                            Ending: Bödeln
                        
                            börja om: 0
                            """)
                            if val == "0":
                                start()
                        while agent == "2":
                            print("""
                            "dåligt val"
                            Boss fight: agent K

                            """)
                            input(f"""
                            PANG! *det isar i bröstet* innan du hinner reagera har agenten skutit dig...
                            "mycket dåligt val"
                            ({len(ending)}/18)
                            Ending: avrättad
                        
                            börja om: 0
                            """)
                            if val == "0":
                                start()   

                        


    else:
        gurg = input("""
        BOSS FIGHT: gurg the ...guy?

        fly:       1
        blockera:  2
        dodge'a:   3
        """)
        os.system('cls')
        if ending.count("upäten av gurg") == 0:
            ending = ending + ["upäten av gurg"]
        val = input(f"""
        Motstånd är meningslöst,
        Gurg äter up dig,
        ({len(ending)}/18)
        Ending: upäten av gurg

        börja om: 0
        """)
        if val == "0":
            start()

#dra igång allt
tutorial()