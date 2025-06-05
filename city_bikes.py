# Calculating distances based on coordinates in a file
def get_station_data(filename: str):
    thedictionary = {}
    with open(filename) as file:
        lines = [line.strip() for line in file if line.strip()]
        
    i = 0

    while i <len(lines):
        if lines[i] == "":
            i += 1
            continue

        line = lines[i]

        sep = line.split(";")
        name = sep[3]
        try:
            longitude = float(sep[0])
            latitude = float(sep[1])
        except ValueError:
            i += 1
            continue
        
        thedictionary[name] = (longitude, latitude)
        
        i += 1
    return thedictionary
    
def distance(stations: dict, station1: str, station2: str):
    import math
    coords1 = stations[station1]
    coords2 = stations[station2]
    x_km = (coords1[0] - coords2[0]) * 55.26
    y_km = (coords1[1] - coords2[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station1 = ""
    station2 = ""

    for name1 in stations:
        for name2 in stations:
            if name1 == name2:
                continue

            d = distance(stations, name1, name2)
            if d > max_distance:
                max_distance = d
                station1 = name1
                station2 = name2

    return (station1, station2, max_distance)
        
        

