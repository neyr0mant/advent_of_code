import math
list_data = [i.strip() for i in open("input.txt")]
def count_in_los(station, asteroids):
    detected = set()
    for asteroid in asteroids:
        if asteroid != station:
                dx, dy = asteroid[0]-station[0], asteroid[1]-station[1]
                g = abs(math.gcd(dx, dy))
                reduced = (dx//g, dy//g)
                detected.add(reduced)
    return detected
def get_solve(list_data_, part =1):
    size = (len(list_data_), len(list_data_[0]))
    asteroids = set()
    for x in range(size[0]):
        for y in range(size[1]):
            if list_data_[x][y] == "#":
                    asteroids.add((x, y))
    list_station = []
    for station in asteroids:
        in_los = count_in_los(station, asteroids)
        list_station.append((len(in_los), station, in_los))
        list_station.sort(reverse=True)
        amt_in_los, station, in_los = list_station[0]
    if part ==1:
        return amt_in_los
    destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in in_los]
    destroyed.sort(reverse=True)
    dx, dy = destroyed[199][1]

    x, y = station[0]+dx, station[1]+dy
    while (x, y) not in asteroids:
        x, y = x+dx, y+dy
    return y*100 + x

print(f"Решение части 1:{get_solve(list_data, part=1)}")
print(f"Решение части 2:{get_solve(list_data, part=2)}")