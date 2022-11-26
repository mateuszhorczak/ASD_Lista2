# W ASD-kowie, ekologicznej – zielonej krainie zostało jeszcze mnostwo działek na sprzedaz.
# Ich centralny rejestr prowadzi naczelny geodeta ALGOT. Rejestr nie jest uporzadkowany i
# wyszukiwanie w nim danych zajmuje ALGOTOWI zbyt wiele czasu. Pomoz
# bałaganiarskiemu geodecie zrealizowac pierwsze zapytanie do bazy działek, które zwróci
# dane k-tej co do powierzchni działki.


from random import choice


def rect_area(list_of_plots):
    list_of_areas = []
    for plot in list_of_plots:
        length = abs(plot[0] - plot[2])
        weight = abs(plot[1] - plot[3])
        list_of_areas.append(length * weight)
    return list_of_areas


def quick_select(list_of_areas, k_element):
    pivot = choice(list_of_areas)
    left = [area for area in list_of_areas if area > pivot]
    mid = [pivot]
    right = [area for area in list_of_areas if area < pivot]

    left_length = len(left)
    mid_length = 1
    if k_element <= left_length:
        return quick_select(left, k_element)
    elif k_element > left_length + mid_length:
        return quick_select(right, k_element - left_length - mid_length)
    else:
        return mid[0]


array = []
n = int(input())
for i in range(n):
    inp = list(map(int, input().split()))
    array.append(inp)
k = int(input())


results = []
areas = rect_area(array)
for i in range(len(array)):
    results.append([array[i], areas[i]])

searched_area = quick_select(areas, k)
for result in results:
    if result[1] == searched_area:
        print(result[0])
