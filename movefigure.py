import curses

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()


    y, x = 0, 0 # start position
    stdscr.addch(y, x, '#')  # Ritar upp figuren på start positionen
   
    max_y, max_x = stdscr.getmaxyx() # Ger dimensionerna av terminalfönstret
   
    y, x = max_y // 2, max_x // 2


    while True:
        key = stdscr.getch()  # får input från användaren


        # Flytta 'X' med piltangenterna
        if key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
     
            
                   
            
        # Skapar en portal i bordern som gör att 'X' åker igenom till andra sidan
        if y == 0:
            y = max_y
        elif y == max_y:
            y = 0
        elif x == 0:
            x = max_x
        elif x == max_x:
            x = 0
           
        # Ser till att 'X' stannar inom bordern och att det inte går sönder.
        y = max(0, min(y, max_y - 1))
        x = max(0, min(x, max_x - 1))


        stdscr.clear()  # Tömmer skärmen
        stdscr.addch(y, x, '#')  # Visar figuren på en ny position
       
        stdscr.border() # Ritar upp bordern


if __name__ == "__main__":
   curses.wrapper(main)









