class Animal:
    def __init__(self, name, vegetarina):
        self.name = name
        self.vegetarina = vegetarina
        
    def attack(self, other):
        print(f'{self.name} attack {other.name}')
        
    def meet(self, other):
        print(f'{self.name} meet {other.name}')
        if isinstance(self, Human):
            if isinstance(other, Human):
                if other.name in self.friends:
                    if other.vegetarina == self.vegetarina:
                        self.dinner_with(other)
                else:
                    self.add_friend_with(other)
            else:
                if self.vegetarina and other.vegetarina:
                    self.pet(other)
                elif not self.vegetarina and other.vegetarina:
                    self.attack(other)
                else:
                    self.run_away_from(other)
        else:
            if not isinstance(other, Human):
                if isinstance(self, Terrestrial) and isinstance(other, Terrestrial):
                    self.speak()
            else:
                if isinstance(self, Terrestrial):
                    self.speak();
                elif self.vegetarina == False:
                    self.attack(other)
                else:
                    if not isinstance(self, Amphibians):
                        if isinstance(self, Aquatic):
                            self.swim_away_from(other)
                        else:
                            self.run_away_from(other)
                    else:
                        if isinstance(self, Aquatic) and self.good_swimmer == True or isinstance(self, Amphibians) and self.live_on_land == False:
                            self.swim_away_from(other)
                        else:
                            self.run_away_from(other)
                            
    def __str__(self):
        return self.name
    
    def run_away_from(self, other):
        print(f'{self.name} run_away_from {other.name}')
        
class Aquatic(Animal):
    def __init__(self, name, vegetarina, good_swimmer, speak_sound = None):
        super().__init__(name, vegetarina)
        self.good_swimmer = good_swimmer
        self.speak_sound = speak_sound
        
    def swim_away_from(self, other):
        print(f'{self.name} swim_away_from {other.name}')
        
    def run_away_from(self, other):
        super().run_away_from(other)
        
class Terrestrial(Animal):
    def __init__(self, name, vegetarina, speak_sound = None):
        super().__init__(name, vegetarina)
        self.speak_sound = speak_sound
        
    def run_away_from(self, other):
        super().run_away_from(other)
        
    def speak(self):
        print(f'{self.name} speak {self.speak_sound}')
    
class Amphibians(Animal):
    def __init__(self, name, vegetarina, live_on_land, speak_sound = None):
        super().__init__(name, vegetarina)
        self.live_on_land = live_on_land
        self.speak_sound = speak_sound
        
    def run_away_from(self, other):
        super().run_away_from(other)
        
class Human(Animal):
    def __init__(self, name, vegetarina):
        super().__init__(name, vegetarina)
        self.friends = []
        
    def add_friend_with(self, other):
        print(f'{self.name} add_friend_with {other.name}')
        self.friends += [other.name]
        other.friends += [self.name]
        
    def dinner_with(self, other):
        print(f'{self.name} dinner_with {other.name}')
    
    def run_away_from(self, other):
        super().run_away_from(other)
        
    def pet(self, other):
        print(f'{self.name} pet {other.name}')
        
n = 0
animals = []
while(True):
    str = input()
    try:
        n = int(str)
        break
    except:
        str = str.split()
        if str[0] == 'Amphibians':
            dosomething = f'animals += [{str[0]}("{str[1]}", {str[2]}, {str[3]}, "{str[4]}")]'
        elif str[0] == 'Human':
            dosomething = f'animals += [{str[0]}("{str[1]}", {str[2]})]'
        elif str[0] == 'Terrestrial':
            dosomething = f'animals += [{str[0]}("{str[1]}", {str[2]}, "{str[3]}")]'
        else:
            dosomething = f'animals += [{str[0]}("{str[1]}", {str[2]}, {str[3]})]'
        exec(dosomething)
            
for i in range(n):
    names = input().split()
    for i in range(len(animals)):
        if isinstance(animals[i], Human) and animals[i].name == names[0]:
            animals[i].friends += [names[1]]
        elif isinstance(animals[i], Human) and animals[i].name == names[1]:
           	animals[i].friends += [names[0]]
while True:
    try:
        names = input().split()
        index_of_animal1, index_of_animal2 = -1, -1
        for i in range(len(animals)):
            if animals[i].name == names[0]:
                index_of_animal1 = i
            elif animals[i].name == names[1]:
                index_of_animal2 = i
        animals[index_of_animal1].meet(animals[index_of_animal2])
    except:
        break