# import av moduler
import random
from enum import Enum
from typing import Optional, Iterator, Iterable




class Combatant:
    def __init__(self, name: str, health: float = 50) -> None:
        '''Funktion som sparar namnet du ger i början och
        ger dig 50 hälsa i början så att spelet kan starta'''
        self.name = name
        self.health = health


    def add_hp(self, delta: float) -> None:
        self.health = max(0., self.health + delta)


    @property
    def alive(self) -> bool:
        '''om man har mer än 0 hälsa får man tillbaks
        hur mycket hälsa du har kvar'''
        return self.health > 0


    def __str__(self) -> str:
        return self.name




class Action(Enum):
    HEAL = 'heala'
    ATTACK = 'attackera'




class Move:
    # Sparar de moves man kan göra i ett dictionary
    MAX_HP = {
        Action.HEAL: 5,
        Action.ATTACK: -20,
    }


    def __init__(self, actor: Combatant, opponent: Combatant, action: Optional[Action] = None) -> None:
        self.actor = actor
        self.opponent = opponent
        if action is None:
            action = random.choice(tuple(Action))
        self.action = action
        self.hp = random.uniform(0, self.MAX_HP[action])
        if action == Action.HEAL:
            self.target = actor
        else:
            self.target = opponent


    def apply(self) -> None:
        self.target.add_hp(self.hp)


    def __str__(self) -> str:
        desc = f'{self.actor} {self.action.value}de för {abs(self.hp):.0f} HP.\n'
        if self.target.alive:
            desc += f'{self.target} har nu {self.target.health:.0f} hälsa.'
        else:
            desc += f'{self.target} dog.'
        return desc




class Game:
    def __init__(self, player_name: str, player_actions: Iterable[Action]) -> None:
        self.player = Combatant(name=player_name)
        self.enemy = Combatant(
            name=random.choice(("Vampyr", "Zombie", "Troll")),
        )
        self.combatants = (self.player, self.enemy)
        self.player_actions = player_actions


    def play(self) -> Iterator[Move]:
        for action in self.player_actions:
            for move in (
                Move(*self.combatants, action=action),
                Move(*reversed(self.combatants))
            ):
                move.apply()
                yield move
                if not move.target.alive:
                    return




def ask_player() -> Iterator[Action]:
    ''' Funktion som frågar vad du vill göra, i en while loop för att
    om felaktig input ges så händer inget skärskilt utan frågan ställs 
    bara igen'''
    while True:
        try:
            action_input = input("\nAttackera eller heala?: ").lower()
            action = Action(action_input)
            yield action
        except ValueError:
            action_input


def main() -> None:
    '''main funktionen som körs i början så spelet startar'''
    game = Game(
        player_name=input("Vad heter du?: "),
        player_actions=ask_player(),
    )
    print(f"Välkommen {game.player} till den här textbaserade RPG:n")
    print(f"En vild {game.enemy} har dykt upp! Du måste fighta den!")
    for move in game.play():
        print(move)




if __name__ == '__main__':
    main()
   
   
   
   
   
   







