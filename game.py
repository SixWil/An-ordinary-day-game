# test

#imports
import os

#resett
def reset():
    global tid
    tid = 0

    global vakenhet
    vakenhet = ""

    global frukost
    frukost = ""

#Start
försök = 0
def start():
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

        if tid == 9:
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
        if 5 > tid > 2:
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

        if tid > 4 :
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
    frukost = input("sample text: köket")
            

#dra igång allt
start()