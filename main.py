
def game(true=None):
    lockpick = False
    sword = False
    pinky = True
    tower = False
    dungeon = False
    fight = False
    sneak = False

    print('A princess has been captured by a dragon. The king has offered a castle as a reward for rescuing her.')
    valid_text = False
    while not valid_text:
        txt = input('Choose your equipment for the adventure (lockpick or sword): ')
        if txt.lower() == 'lockpick':
            lockpick = True
            valid_text = True
        elif txt.lower() == 'sword':
            sword = True
            valid_text = True
        else:
            print('You must enter "lockpick" or "sword"')

    valid_text = False
    while not valid_text:
        txt = input("You approach the dragon's castle, a goblin guards the entrance.\n"
                    "Do you fight the goblin or sneak past? (fight or sneak): ")
        if txt.lower() == 'fight':
            fight = True
            valid_text = True
        elif txt.lower() == 'sneak':
            sneak = True
            valid_text = True
        else:
            print('You must enter "fight" or "sneak"')

    if fight:
        if sword:
            print('You defeat the goblin with your sword')
        else:
            print('You have no sword! While fighting, the goblin manages to nibble your pinky off')
            pinky = False

    if sneak:
        if sword:
            print('The goblin catches a glimpse of your big shiny sword! While fighting, the goblin manages to nibble your pinky off')
            pinky = False
        else:
            print('You manage to sneak past the goblin')

    valid_text = False
    while not valid_text:
        txt = input("You enter the castle, do you think the princess is in the tower or the dungeon? (tower or dungeon): ")

        if txt.lower() == 'tower':
            tower = True
            valid_text = True
        elif txt.lower() == 'dungeon':
            dungeon = True
            valid_text = True
        else:
            print('You must enter "tower" or "dungeon"')

    print('Hooray! You found the princess door, but there is a code')
    if lockpick:
        print('Thankfully you got through the door with the lockpick!')

    else:
        valid_text = False
        tries = 0
        while not valid_text:
            txt = input(
                "6 x Pineapple = 24\nPineapple x Apple = 32\nWhat does apple = ")
            tries = tries + 1

            if txt == '8':
                valid_text = True
            else:
                if tries < 3:
                    print('Incorrect! Try again')
                elif tries < 10:
                    print('Hint: Pineapple = 4')
                else:
                    print('You give up and break the door with your sword. Your sword breaks')
                    valid_text = True
                    sword = False
    print("You enter the room and it turns out that the dragon is guarding the princess himself!")
    if sword:
        print('The dragon breathes fire and melts your sword!')
        sword = False

    valid_text = False
    while not valid_text:
        txt = input('The dragon whips his tail at you. The tail is 5 meters long and you are 3 meters away.'
                    'How far back do you walk (in meters)?: ')
        number = float(txt)
        if number > 3:
            print('You stepped too far back and fell onto the stairs. Try again')
        elif number > 2:
            print('You dodged it, great job!')
            valid_text = True
        elif number == 2:
            print('Wow, that was close, but you dodged it, great job!')
            valid_text = True
        else:
            print('Oh no! You got smacked to the ground!')
    print('The dragon was about to step on you when you sneak under him!')
    txt = input('You get to the princess and she says "thank you for saving me" with a sparkle in her eye\nDo you wish to return her for the castle or run away and fall in love with her (run away or return): ')
    if txt == 'run away':
        print('You get married to the princess, but she complains that you do not have a castle')
    else:
        print('You take the princess to the king and he gives you a castle, but it is VERY lonely')
    if not pinky:
        print('AND you do not have a pinky')

        print(f"lockpick={lockpick}")
        print(f'sword={sword}')
        print(f'pinky={pinky}')
        print(f'tower={tower}')
        print(f'dungeon={dungeon}')



# Main entry point for script
if __name__ == '__main__':
    game()