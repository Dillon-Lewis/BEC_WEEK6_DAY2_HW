# Task 2

import requests
import json


response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

pokeman_date = response.json()

print(pokeman_date['name'])
print(pokeman_date['abilities'])


## Task 3

def average_weight():
        
        weights = []
        
        poke1 = input('Please enter the first pokeman:  ')
        poke2 = input('Please enter the second pokeman:  ')
        poke3 = input('Please enter the third pokeman:  ')

        response1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke1.lower()}")
        response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke2.lower()}")
        response3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke3.lower()}")

        if response1.status_code == 200:
                pokeman_date = response1.json()
                weights.append(int(pokeman_date['weight']))
        if response2.status_code == 200:
                pokeman_date = response2.json()
                weights.append(int(pokeman_date['weight']))
        if response3.status_code == 200:
                pokeman_date = response3.json()
                weights.append(int(pokeman_date['weight']))
        total = sum(weights)
        average = total / 3
        print(f"The average weight of {poke1}, {poke2} and {poke3} is {average}")


average_weight()


