def zodiac(sign):
    if sign <= '0119':
        return 'Ma Ket'
    if sign <= '0218':
        return 'Bao Binh'
    if sign <= '0320':
        return 'Song Ngu'
    if sign <= '0419':
        return 'Bach Duong'
    if sign <= '0520':
        return 'Kim Nguu'
    if sign <= '0620':
        return 'Song Tu'
    if sign <= '0722':
        return 'Cu Giai'
    if sign <= '0822':
        return 'Su Tu'
    if sign <= '0922':
        return 'Xu Nu'
    if sign <= '1022':
        return 'Thien Binh'
    if sign <= '1122':
        return 'Thien Yet'
    if sign <= '1221':
        return 'Nhan Ma'
    return 'Ma Ket'

for _ in range(int(input())):
    day, month = [int(i) for i in input().split()]
    print(zodiac('{0:0>2}'.format(month) + '{0:0>2}'.format(day)))