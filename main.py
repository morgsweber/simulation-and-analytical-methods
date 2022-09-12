#Elias Matos e Morgana Weber
from matplotlib import pyplot

def linear_congruential_generator(x0, a, c, M, size):
    values = [0] * size
    values[0] = x0
    i = 1
    while i < size:
        values[i] = (a * values[i - 1] + c) % M
        i += 1
    values.pop(0)
    #print(i)
    return values

sizeV = 1000
values = linear_congruential_generator(1, 1.3, 0.2, 1, sizeV)
#print(len(values))

f = open("exit.txt", "w")
for i, value in enumerate(values):
    f.write(f"{i}: {value}\n")
    #print(i, value)

pyplot.scatter(range(0, sizeV - 1), values)
pyplot.show()