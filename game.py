# test

#imports
import os


#resett
def reset():
    global kvar
    kvar = []

    global klar
    klar = []

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

global intro
os.system('cls')
intro = input("""
Hej! Välkommen till Sixten Wilde och Sigge Nilssons Spel:
  ______                          _ _             _             
 |  ____|                        | (_)           | |            
 | |__   _ __   __   ____ _ _ __ | |_  __ _    __| | __ _  __ _ 
 |  __| | '_ \  \ \ / / _` | '_ \| | |/ _` |  / _` |/ _` |/ _` |
 | |____| | | |  \ V / (_| | | | | | | (_| | | (_| | (_| | (_| |
 |______|_| |_|   \_/ \__,_|_| |_|_|_|\__, |  \__,_|\__,_|\__, |
                                       __/ |               __/ |
                                      |___/               |___/ 
Varje val assosieras med en siffra, för att välja det valet skriv dess siffra längst ner i konsollen (denna texten är i konsollen).
Detta spelet är designat för att spelas flera gånger, för att starta om skriv 0
""")

#starta och starta om programmet
def start():
    "resettar programmet, initsierar sovrummet"

    while True:
        reset()
        os.system('cls')
        global spelare
        spelare = ["din själ"]

        global försök
        försök = försök + 1
        print(f"""
        EN VANLIG DAG
        försök {försök}
        """)

        print(f"du har {spelare}")

        sovrum()

# Sovrum
def sovrum():
    "start rum, inget speciellt"
    global vakenhet
    global tid

    vakenhet = input("""
    du vaknar, vad gör du?

    Somna om: 1.
    Gå upp: 2.
    """)
    if vakenhet == "0":
        start()
    while vakenhet == "1":
        if tid < 9:
            tid = tid+1
            print(f"du somnar om {tid} gången")
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
            val = input("""
            Ending: Oopsy!
        
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

    if dagsplan == "0":
        start()
    while dagsplan == "3":
        print("Du stannar hemma och chillar hela dagen")
        global val
        val = input("""
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
    "i skolan kan du upnå inteligens, det kommer du behöva senare, går du för långt får du en ending"
    global val
    global koridor
    koridor = input("""
    du går runt i skolans koridorer, du kan fortsätta framåt, vika in till bilblioteket eller vända om.

    Vänd om:          1
    fortsätt frammåt: 2
    Biblioteket:      3
    """)
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
        if läraren == "0":
            start()
        while läraren == "1":
            global val
            val = input("""
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
                    val = input("""
                    Ending: Kvarsittning
                
                    börja om: 0
                    """)
                    if val == "0":
                        start()
                
            print("du säger något så dumt att lärarens huvud exploderar")
            val = input("""
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
    global böcker
    böcker = input("""
    Du sätter dig i bibloteket

    läs böcker en stund: 1
    lämna biblioteket:   2
    """)
    if böcker == "0":
        start()
    if böcker == "2":
        skolan()
    if böcker == "1":
        global läst
        läst = läst +1
        print(f"""
        du har läst böcker i {läst} stund(er)
        """)
        if läst == 3:
            global spelare
            spelare = spelare + ["inteligens"]
            print(f"du har {spelare}")
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
            if respekt == "0":
                start()
            if respekt == "2":
                print("""
                "eh, du läser ju faktiskt riktiga böcker"
                hon låter dig slippa undan
                """)
                skolan()
            if respekt == "3":
                val = input("""
                din ligism gör att biblioteket reagerar våldamt,
                en hylla tippar över och krossar dig
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
    if trafik == "0":
        start()
    while trafik == "1":
        global val
        val = input("""
            Ending: påkörd
        
            börja om: 0
            """)
        if val == "0":
            start()
    while trafik == "2":
        print("Vilken tur att du väntade, den föraren var in lämpad för bilar")
        parken()

#vägvalet
def parken():
    "här får du välja riktning igen, korrekt är grottan först sedan staden, stanna ger en ending"
    global riktning
    riktning = input("""
    du står nu i en park, mot skogen finns en grotta, mot staden finns en öppning till undermarken, vart vill du gå?

    grottan: 1
    Staden: 2
    Stanna: 3
    """)
    if riktning == "0":
        start()
    while riktning == "3":
        global val
        val = input("""
        du sitter och njuter av solens värme och fåglarnas dova bakgrunds tvitter
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
        if vampyren == "0":
            start()
        if vampyren == "1":
            global val
            val = input("""
            Ending: upäten av vampyr
        
            börja om: 0
            """)
            if val == "0":
                start()

        if vampyren == "2":
            val = input("""
            att vampyrer dör av lök är en myt.
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
            else:
                val = input("""
                du har ingen träpåle
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
                    val = input("""
                        Ending: vampyr
                    
                        börja om: 0
                        """)
                    if val == "0":
                        start() 
                else: val = input("""
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
        if antiklimax == "0":
            start()
        while antiklimax == "1":
            val = input("""
            du förvandlar dig till fladdermöss och flyger igenom gallret,
            på andra sidan ser du en skyllt där det står:
            "DEVELOPER NOTE: här finns det inget"
            du dog av antiklimax
            Ending: MEH!
        
            börja om: 0
            """)
            if val == "0":
                start()
    
    kloaken()

#Stadens tunnlar
def kloaken():
    "under staden, du möter gurg, detta är sista scenen i spelet (om du gjort rätt)"
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
        if gurg == "0":
            start()
        while gurg == "1":
            val = input("""
            Motstånd är meningslöst,
            Gurg äter up dig,
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "2":
            val = input("""
            Motstånd är meningslöst,
            Gurg äter up dig,
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "3":
            val = input("""
            Motstånd är meningslöst,
            Gurg äter up dig,
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()
        while gurg == "5":
            val = input("""
            Du plockar fram pistolen och skuter villt mot varelsen,
            du har avlossat alla skott i pistolen, några kulor träffar och gör skada... inte många nog.
            Motstånd är meningslöst,
            Gurg äter up dig,
            Ending: upäten av gurg
        
            börja om: 0
            """)
            if val == "0":
                start()

        while gurg == "6":
            val = input("""
            du flyger fram och biter gurg i halsen och ger honom vampirism,
            han biter dig i halsen tillbaka och ger dig död,
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
                if agent == "0":
                    start()
                while agent == "1":
                    val = input("""
                    "mycket bra val"
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
                    input("""
                    PANG! *det isar i bröstet* innan du hinner reagera har agenten skutit dig...
                    "mycket dåligt val"
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
                        if sim == "0":
                            start()
                        if sim == "1":
                            input("""
                            Det tar en stund att åka genom sladdarna,
                            när du väl anländer har den förra servern slocknat.
                            Ending: destroyer of worlds
                        
                            börja om: 0
                            """)
                            if val == "0":
                                start()
                        if sim=="2":
                            print("du återvänder till jorden")
                            break
                    input("""
                    du och gurg lever lyckliga i alla era dagar.
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
                    if nekad == "0":
                        start()
                    while nekad == "1":
                        print("""
                        när han inser vad du gjort blir han förargad
                        """)
                        val = input("""
                        Motstånd är meningslöst,
                        Gurg äter up dig,
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
                        while agent == "1":
                            val = input("""
                            "mycket bra val"
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
                            input("""
                            PANG! *det isar i bröstet* innan du hinner reagera har agenten skutit dig...
                            "mycket dåligt val"
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
        val = input("""
        Motstånd är meningslöst,
        Gurg äter up dig,
        Ending: upäten av gurg
    
        börja om: 0
        """)
        if val == "0":
            start()

#dra igång allt
start()