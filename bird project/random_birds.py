from bird_name_gen import get_bird
import random

def rand_bird_list_of_4():
    birds = []
    for i in range(4):
        birds.append(get_bird())
        i+=1
    return birds

bird_options = rand_bird_list_of_4()
bird_chosen = random.choice(bird_options)