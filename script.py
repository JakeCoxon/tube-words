
stations = []

with open('tube_stations.txt', 'r') as file:
    stations = list(file.readlines())


def thing(word):
    stations_without_any_letters = []
    for station in stations:
        station = station.lower()
        if all(c not in station for c in word):
            stations_without_any_letters.append(station)
    if len(stations_without_any_letters) < 3:
        return stations_without_any_letters


with open('common_alpha.txt', 'r') as file:
    words = file.readlines()

    for word in words:
        word = word.strip().lower()
        stations_without_any_letters = thing(word)
        if stations_without_any_letters:
            print(word, stations_without_any_letters)

