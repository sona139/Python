def getScore(ans):
    if ans >= 39: return 9
    if ans >= 37: return 8.5
    if ans >= 35: return 8
    if ans >= 33: return 7.5
    if ans >= 30: return 7
    if ans >= 27: return 6.5
    if ans >= 23: return 6
    if ans >= 20: return 5.5
    if ans >= 16: return 5
    if ans >= 13: return 4.5
    if ans >= 10: return 4
    if ans >= 7: return 3.5
    if ans >= 5: return 3
    if ans >= 3: return 2.5
    return 0

def round(overall):
    decimal = overall-int(overall)
    if decimal >= 0.75: return int(overall)+1
    if decimal >= 0.25: return int(overall)+0.5
    return int(overall)

for _ in range(int(input())):
    r, l, s, w = [float(i) for i in input().split()]
    overall = round((getScore(r) + getScore(l) + s + w)/4)
    print('{:.1f}'.format(overall))