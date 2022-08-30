from operator import truediv
from image_search import bird_image
from random_birds import bird_chosen, bird_options


menu_options = {
    1: 'Guess some birds',
    2: 'Show your score',
    3: 'Exit',
}

game_options = {
    1: bird_options[0],
    2: bird_options[1],
    3: bird_options[2],
    4: bird_options[3],
    5: 'Main Menu',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def print_game_menu():
    for key in game_options.keys():
        print(key, '--', game_options[key] )

def option1():
     while(True):
        print('SELECT THE BIRD THAT IS SHOWN')
        bird_image()
        print_game_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number 1-5 ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            if bird_options[0] == bird_chosen:
                print("CORRECT!!!")
                break
            else:
                print("ERRR WRONG...")
                print("The correct bird was a", bird_chosen)
                break
        elif option == 2:
            if bird_options[1] == bird_chosen:
                print("CORRECT!!!")
                break
            else:
                print("ERRR WRONG...")
                print("The correct bird was a", bird_chosen)
                break
        elif option == 3:
            if bird_options[2] == bird_chosen:
                print("CORRECT!!!")
                break
            else:
                print("ERRR WRONG...")
                print("The correct bird was a", bird_chosen)
                break
        elif option == 4:
            if bird_options[3] == bird_chosen:
                print("CORRECT!!!")
                break
            else:
                print("ERRR WRONG...")
                print("The correct bird was a", bird_chosen)
                break
        elif option == 5:
            print('Those were some cool birds... bye!')
            print("""
                ,~
                ('v)__
               (/ (``/
                \__>' 
                 ^^
            """)
            break
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


def option2():
     print('Handle option \'Option 2\'')
     #print out the users points - easy :)

if __name__== '__main__':
    while(True):
        print("""
             ___     ___
            (o o)   (o o)
           (  v  ) (  v  ) 
          /--m-m- /--m-m-
        """)
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')