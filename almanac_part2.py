# I brute forced this task by altering the step variable in the second for loop
# and taking an educated guess ¯\_(ツ)_/¯

def seed_map(file):
    seeds = file[0][7:-1].split(" ")
    seed_to_soil = [l[:-1].split(" ") for l in file[3:35]]
    soil_to_fertilizer = [l[:-1].split(" ") for l in file[38:78]]
    fertilizer_to_water = [l[:-1].split(" ") for l in file[81:122]]
    water_to_light = [l[:-1].split(" ") for l in file[125:151]]
    light_to_temperature = [l[:-1].split(" ") for l in file[154:191]]
    temperature_to_humidity = [l[:-1].split(" ") for l in file[194:206]]
    humidity_to_location = [l[:-1].split(" ") for l in file[209:234]]
    smallest = float("inf")
    for i in range(0, len(seeds),2):
        for seed in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]), 5000):
            print("{:13s}{}".format("Seed:", str(seed)))
            soil = lookup(seed_to_soil, seed)
            print("{:13s}{}".format("Soil:", str(soil)))
            fertilizer = lookup(soil_to_fertilizer, soil)
            print("{:13s}{}".format("Fertilizer:", str(fertilizer)))
            water = lookup(fertilizer_to_water, fertilizer)
            print("{:13s}{}".format("Water:", str(water)))
            light = lookup(water_to_light, water)
            print("{:13s}{}".format("Light:", str(light)))
            temperature = lookup(light_to_temperature, light)
            print("{:13s}{}".format("Temperature:", str(temperature)))
            humidity = lookup(temperature_to_humidity, temperature)
            print("{:13s}{}".format("Humidity:", str(humidity)))
            location = lookup(humidity_to_location, humidity)
            print()
            print("{:13s}{}".format("Location:", str(location)))
            print()
            if location < smallest:
                smallest = location
                print("Smallest location seed: "+str(seed))
                print()
    return smallest


def lookup(table, source):
    if type(source) == str:
        source = int(source)
    for map in table:
        start = int(map[1])
        stop = start + int(map[2])
        if source < start or source >= stop: continue
        return int(map[0]) + (source - start)
    return source


if __name__ == "__main__":
    file = open(r"inputs/day5.txt", "r").readlines()
    print(seed_map(file))
