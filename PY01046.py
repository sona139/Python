def tower(n, pile1 = 'A', pile2 = 'B', pile3 = 'C'):
    if n == 1:
        print(pile1 + ' -> ' + pile3)
        return 
    tower(n-1, pile1, pile3, pile2)
    tower(1, pile1, pile2, pile3)
    tower(n-1, pile2, pile1, pile3)
    
tower(int(input()))