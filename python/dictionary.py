Zelda = {'name': 'Zelda',
        'genre': 'Action-Adventure',
        'platform': 'Switch',
        'rating': 9.5}

if Zelda['rating'] <= 99.5:
    print("yay")
else:
    print("no")
Zelda['game'] = 'yes'
print(Zelda['game'])
pop_item = Zelda.pop('rating')
print(pop_item)

