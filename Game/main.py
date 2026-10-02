from Core.vector2 import Vector2
from Entities.player import Player
from Enum.actions import Actions
from Enum.positions import Positions
from Types.entities import EntityType
from World.map import Map

def run():
    print("Iniciando.")

    scene_1 = Map(Vector2(100, 100))

    data = EntityType(
        name="José",
        position=Vector2(50,50),
        life=10,
        max_life=10,
        mana=10,
        map=scene_1
    )

    player = Player(data)
    
    while True:

        anwser = input("-> ")

        if anwser == 'w':
           player.doAction(Actions.MOVE, Positions.UP)
        if anwser == 'a':
           player.doAction(Actions.MOVE,Positions.LEFT)  
        if anwser == 's':
           player.doAction(Actions.MOVE,Positions.DOWN)  
        if anwser == 'd':
           player.doAction(Actions.MOVE,Positions.RIGHT)   
        
        if anwser == "exit":
            break

        print(player.getPosition())


    print("Finalizando.")

if __name__ == '__main__':
    run()