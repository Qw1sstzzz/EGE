with open('Task-26-9171-file.txt') as file:
    m, k, n = map(int, file.readline().split())
    passengers = [list(map(int, i.split())) for i in file]

passengers = sorted(passengers, key=lambda x: (x[0], -x[1]))

accepted = 0
free_places = [0] * k
last_station = 1
full_stations = 0

for start, stop in passengers:
    while start != last_station:
        if 0 not in free_places:
            full_stations += 1
        last_station += 1
        while last_station in free_places:
            free_places[free_places.index(last_station)] = 0
    if 0 in free_places:
        free_places[free_places.index(0)] = stop
        accepted += 1

print(accepted, full_stations)