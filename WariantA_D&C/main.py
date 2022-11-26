# Wariant A – „Optymalne dostawy”
# Pewnie trudno Ci bdzie uwierzy, ze to nie sen, ale przynajmniej spróbuj sobie wyobrazic,
# ze przez nasz piekny kraj biegnie od gor az do morza szeroka i bezpłatna autostrada. Mało
# tego, po obu jej stronach az si roi od renomowanych stacji benzynowych, restauracji i co
# najwazniejsze równie szybkich jak sama autostrada stacji serwisowych. Własnie jedna z
# wiodacych na rynku firm motoryzacyjnych wygrała przetarg na zbudowanie wzdłuz naszej
# pieknej autostrady, sieci swoich stacji i zastanawia sie, przy której z tych stacji zbudowac
# dodatkowo skład czesci zamiennych. Miejsce jego budowy trzeba zaplanowac tak, azeby
# suma odległosci pomidzy składem a stacjami była najmniejsza. Firma poprosiła Ciebie, jako
# dobrze zapowiadajacego si programiste, abys napisał program ustalajacy miejsce budowy
# składu, przy zadanej lokalizacji stacji serwisowych.


from random import choice


def distance_to_median(list_of_stations, searched_value):
    sum_of_distances = 0
    for i in range(len(list_of_stations)):
        sum_of_distances += abs(list_of_stations[i] - searched_value)
    return sum_of_distances


def quick_select(list_of_stations, k):
    pivot = choice(list_of_stations)
    left = [station for station in list_of_stations if station > pivot]
    mid = [pivot]
    right = [station for station in list_of_stations if station < pivot]

    left_length = len(left)
    mid_length = 1
    if k <= left_length:
        return quick_select(left, k)
    elif k > left_length + mid_length:
        return quick_select(right, k - left_length - mid_length)
    else:
        return mid[0]


stations_arr = []
number_of_station = int(input())
for number in range(number_of_station):
    stations_arr.append(int(input()))

median = number_of_station // 2 + 1  # w przypadku parzystej liczby stacji nie ma znaczenia czy wybierzemy
# miediane z lewej czy prawej strony
distance = distance_to_median(stations_arr, quick_select(stations_arr, median))
print(median)
print(distance)
