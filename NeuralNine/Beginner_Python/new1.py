planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_to_initial = {planet:planet[0] for planet in planets}

print(planet_to_initial)

print(planet_to_initial['Venus'])

print('Saturn' in planet_to_initial)