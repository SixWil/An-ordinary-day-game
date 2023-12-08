#imports
import os

#Varables
försök = 0
tid = 0

#Start
def start():
    os.system('cls')
    global försök
    försök = försök + 1
    print(f"""
    AN ORDINARY DAY
    försök {försök}
    """)
start()

# modul
def ending(ending):
    if ending == "simulation":
        print("""
        på labbet sitter en överarbetat arbetare,
        det är kväll och han skulle egentligen fått åka hem för många timmar sedan.
        Han ställer sig upp för att gå och hämta ännu en kopp kaffe,
        han märker inte att en sladd har virat sig runt hans ben och när han går rycker han den från servern.
        Servern med namnet "vintergatan" slocknar.
        """)
        val = input("""
        Oopsy Ending
        för:    skriv:
        börja om: 0
        """)
        if val == "0":
            start()

# sovrum
def väckarkloca():
    vakenhet = input("""
    väckarklockan ringer, vad gör du?
    för:    skriv:
    Somna om: 1.
    Gå upp: 2.
    """)

    if vakenhet == 1:
        tid = tid+1
    if tid == 10:
        ending()