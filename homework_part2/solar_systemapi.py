# Task 2
import requests
import json

weights = {}

def fetch_planet_data():
    
    response = requests.get('https://api.le-systeme-solaire.net/rest/bodies')
    planets = response.json()['bodies']
    for planet in planets:
        if planet['isPlanet']:
            weights = {
                'Name': planet['name'],
                'Mass': int(planet['mass']['massValue']),
                "Sideral Orbit": planet['sideralOrbit']
            }
            print(weights)

fetch_planet_data()

def heaviest_planet():
    response = requests.get('https://api.le-systeme-solaire.net/rest/bodies')
    planets = response.json()['bodies']
    for planet in planets:
        if planet['isPlanet']:
            weights = {
                'Name': planet['name'],
                'Mass': int(planet['mass']['massValue']),
                "Sideral Orbit": planet['sideralOrbit']
            }
            for key, value in weights:
                



heaviest_planet()