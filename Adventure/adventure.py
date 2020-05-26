import main_title, death
from termcolor import colored, cprint

hp = 20

def start_adventure():
    print('Inside you will find adventure and suprizes around every corner')
    name = input('My name is Aligor. what is your name? ')
    print('Welcome ' + name + ', a new adventure awaits if you are ready.')
    begin = input('Would you like to begin(y/n)? ').lower()
    if begin.lower().strip() == 'y':
        print('Great, lets start!')
        the_path(name)
    else:
        print(colored('I will always be here when you are ready to start.', 'magenta'))
    print(colored('End', 'magenta'))
    return name

def red_door():
    return


def the_path():
    print('The rain is beating down all around you. You awake to find that you in the middle of the path with no idea how you got there.As you stand up you look around and notice that there are lighs ahead of you and the dark forest behind you. You decide that you are going to see wht the lights are. As you approach the castle, and see a red door to your left and a blue door to your right. There is a sign in the middle of them. "You may enter if you wish. if you do there is great adventure waiting for you. ')
    door_picked = input('Do you pick the ' + colored('red', 'red', attrs=['underline']) + ' door or ' + colored('blue', 'blue', attrs=['underline']) + ' door? ')

    if door_picked.lower().strip() == 'red':
        print('You picked the red door')
        print('\n')
        print('Your HP is {0}'.format(hp))
        death.reaper_death()
    elif door_picked.lower().strip() == 'blue':
        print('You picked the blue door')
        print('As you turn the knob your heart starts to beat faster. You are not sure why but there is s feeling of dread that over takes you.')
        print('The door creaks as you open it. The room on the other side of the door is lit with a torch. Its a small room that has another door.')
        print('\n')
        print(death.reaper_death.__doc__)

    else:
        print('Sorry, it\'s either '  + colored('red', 'red', attrs=['underline']) + ' or ' + colored('blue', 'blue', attrs=['underline']) + ' as the answer. You\'re the weakest link, goodbye!')


def master():
    main_title.title_name()
    main_title.castle()
    the_path()


if __name__ == '__main__':
    master()
