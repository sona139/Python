from datetime import datetime

class Film:
    def __init__(self, film_id, film_type, date_public, film_name, film_episode_number):
        self.film_id = film_id
        self.film_name = film_name
        self.date_public = date_public
        self.film_type = film_type
        self.film_episode_number = film_episode_number
        self.date = datetime.strptime(self.date_public, '%d/%m/%Y')
        
    def __str__(self):
        return '{} {} {} {} {}'.format(self.film_id, self.film_type.type_name, self.date_public, self.film_name, self.film_episode_number)
        
class Type:
    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name

n, m = [int(i) for i in input().split()]
map_type = {}
list_type = []
list_film = []

for i in range(n):
    list_type += [Type('TL{0:0>3}'.format(i+1), input())]
    map_type[list_type[i].type_id] = list_type[i]

for i in range(m):
    list_film += [Film('P{0:0>3}'.format(i+1), map_type[input()], input(), input(), int(input()))]
    
list_film.sort(key=lambda ele: (ele.date, ele.film_name, ele.film_episode_number))
print(*list_film, sep='\n')    