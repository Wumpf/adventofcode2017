#!/usr/bin/python3
import math

# file input
data = open('input.txt').read()

#p=<2568,1371,-634>, v=<365,191,-83>, a=<-25,-13,7>


closest = -1
minaccelsum = 999999999

positions = []
velocities = []
accellerations = []

for i, line in enumerate(data.splitlines()):
    line = line[3:].replace('<', '').replace('>', '').replace('=', '').replace('a', '').replace('v', '')
    px, py, pz, vx, vy, vz, ax, ay, az = [int(elem) for elem in line.split(',')]
    positions.append((px, py, pz))
    velocities.append((vx, vy, vz))
    accellerations.append((ax, ay, az))

    accelsum = abs(ax) + abs(ay) + abs(az)
    if accelsum < minaccelsum:
        closest = i
        minaccelsum = accelsum
    elif accelsum == minaccelsum:
        dist_new = abs(px) + abs(py) + abs(pz)
        dist_old = sum(abs(o) for o in positions[closest])
        if dist_new < dist_old:
            closest = i

print('result part one', closest, minaccelsum)


# p1 = p0 + v0 + a0                                     = p0 + v0 * 1 + a0 * 1
# p2 = p0 + v0 + a0 + v0 + a0 + a0                      = p0 + v0 * 2 + a0 * 3
# p3 = p0 + v0 + a0 + v0 + a0 + a0 + v0 + a0 + a0 + a0  = p0 + v0 * 3 + a0 * 6
#                  ...                                  = p0 + v0 * 4 + a0 * 10
# pt = p0 + v0 * t + a0 * sum(t) = p0 + v0 * t + a0 * (t*t + t) / 2

def get_pos(index, t):
    afac = (t*t + t) * 0.5
    return (positions[index][0] + t * velocities[index][0] + afac * accellerations[index][0],
            positions[index][1] + t * velocities[index][1] + afac * accellerations[index][1],
            positions[index][2] + t * velocities[index][2] + afac * accellerations[index][2])

# p0 + t * v0 + a0 * (t*t + t) / 2 = p1 + t * v1 + a1 * (t*t + t) / 2
# t*t * (a0 - a1) / 2 + t * (v0 - v1 + (a0 - a1) / 2) + p0 - p1 = 0
# (-b +/- sqrt(b* - 4ac)) / 2a
hits = []
def try_add_hit(i, j, t):
    global hits
    if t >= 0 and t == int(t):
        if get_pos(i, t) == get_pos(j, t):
            hits.append((int(t), i, j))

for i in range(len(positions) - 1):
    for j in range(i+1, len(positions)):
        a, b, c = (0, 0, 0)
        for k in range(3):
            a = (accellerations[i][k] - accellerations[j][k]) * 0.5
            b = (velocities[i][k] - velocities[j][k]) + a
            c = positions[i][k] - positions[j][k]
            if a != 0 or b != 0:
                break
        if a != 0: # square eq
            det = b*b - 4 * a * c
            if det >= 0:
                s = math.sqrt(det)
                t = (-b - s) / (2 * a)
                try_add_hit(i, j, t)
                t = (-b + s) / (2 * a)
                try_add_hit(i, j, t)
        elif b != 0:   # linear eq
            t = c / b
            try_add_hit(i, j, t)
        else:
            print('nope')
            
print('number of potential hits', len(hits))


time_of_death = [float('Inf')] * len(positions)
hits = sorted(hits)
for hit in hits:
    t = hit[0]
    if time_of_death[hit[1]] >= t and time_of_death[hit[2]] >= t:
        time_of_death[hit[1]] = t
        time_of_death[hit[2]] = t

print('result part two', sum(d == float('Inf') for d in time_of_death))

# 610 too high