#Faith and Fate
#A text based Video Game
#Project Start On 8/9/22
#Check Me out At www.pancakeari.com
#-------------------------------------------------
#Import Dependencies
import os
import time
import sys
import random
#Variables (I really love variables)
waitpls = time.sleep
#Starting The game
waitpls(random.randint(0,7))
print('.######..####..######.######.##..##.........####..##..##.#####.........######..####..######.######.\n.##.....##..##...##.....##...##..##........##..##.###.##.##..##........##.....##..##...##...##.....\n.####...######...##.....##...######........######.##.###.##..##........####...######...##...####...\n.##.....##..##...##.....##...##..##........##..##.##..##.##..##........##.....##..##...##...##.....\n.##.....##..##.######...##...##..##........##..##.##..##.#####.........##.....##..##...##...######.\n...................................................................................................\n')
print('A text based game build in a graphical game world')
waitpls(random.randint(0,3))
startquery = input('\nType "Play" To Start, type anything else to quit (Proper Capatilization is nessecary)\nType Here:')
if startquery == 'Play':
    print('\nThe Game Begins in 3...')
    waitpls(1)
    print('2...')
    waitpls(1)
    print('1...')
    waitpls(1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("You wake up, and push yourself off the ground with your palms, they're raw, like they were scratched on a tree or some concrete. The Ground feels mossy and is almost plesant to touch. Using a nearby tree as help, you push yourself off the ground and feel a pang of pain coming from your leg.\nWhat do you do?\n")
    choice1 = input('1 -- Investigate Your Surroundings\n2 -- Rest for awhile, in hopes that standing will cause less anguish\n\nMake Your Choice:')
    if choice1 == '1':
        print('\nTaking a deep breath, you look around, and mutter "What a strange place this is" Under your breath. The reason for this being, of course, is that your surroundings seem to be a small forest, but inside of some sort of building, with grimy white brick walls. You observe that up ahead you have two choices to make, A choice of two paths. The first path looks like the forest you stand in continues into it, and the second being the opposite, having tiled floors and pristeen walls\nWhat do you do?\n')
        choice11 = input('1 -- Continue into the forest path\n2 -- Continue into the building path\n\nMake Your Choice:')
        if choice11 == '1':
            print("\nYou start towards the path of the forest which is green and filled with life, and after about five or six minutes, you find a sword and shield, the sword lodged into the base of a tree, and the shield placed beside it. What do you do?")
            choice111 = input('1 -- Pick up the sword and shield\n2 -- Pick up the sword\n3 -- Pick up the shield\n4 -- Pick up none and continue\nMake Your Choice:')
            if choice111 == '1':
                print('1')
            elif choice111 == '2':
                print('2')
            elif choice111 == '3':
                print('3')
            elif choice111 == '4':
                print('4')
        elif choice11 == '2':
            print("\nYou start towards the path of the bulding area, as soon as both your feet leave the soft moss carpet of the previous area, you feel chills run down your spine. Something insn't right, but you're not sure what it is. You continue down the path, each of your footfalls make an echo around the halls. You start to hear distant voices, and see your first turn in the hall, after thirty-five minutes of your steady walk. Excited by the sound of voices, you change from your slow walk to a full sprint. Once you reach the corner, you fling yourself around it, only to find that you would've had much better luck taking the other path. Standing infront of you, is a 10-foot tall frost giant. Taking a second glance at the walls, you noice that they're not made of bricks, they're made of solid blocks of ice, so cold that they've lost any resemblance of transparency. The Frost Giant swings it's giant axe at you, and you die. \n\n.##..##...####...##..##..........#####...######..######..#####..\n..####...##..##..##..##..........##..##....##....##......##..##.\n...##....##..##..##..##..........##..##....##....####....##..##.\n...##....##..##..##..##..........##..##....##....##......##..##.\n...##.....####....####...........#####...######..######..#####..\n................................................................\n\nRe-Open the game to restart ")
    elif choice1 == '2':
        print("\nYou lay down on the soft moss blanket that is the floor, and your eyelids start to droop. You're much more tired than you would've thought. You're just about to drift off when the floor opens up, and swallows you like its lunch.\n\n.##..##...####...##..##..........#####...######..######..#####..\n..####...##..##..##..##..........##..##....##....##......##..##.\n...##....##..##..##..##..........##..##....##....####....##..##.\n...##....##..##..##..##..........##..##....##....##......##..##.\n...##.....####....####...........#####...######..######..#####..\n................................................................\n\nRe-Open the game to restart")
elif startquery == '69':
    print('Wow, you found the secret code\n')
    waitpls(0.5)
    print("It Dosen't actually do much \n")
    waitpls(2)
    print('but...\n')
    waitpls(0.5)
    print('you can try going to www.pancakeari.com/69420')
else:
    sys.exit()
    


