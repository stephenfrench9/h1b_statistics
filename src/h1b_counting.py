import argparse
import csv
import heapq
from heapq import heappush
from heapq import heappop
from operator import itemgetter

parser = argparse.ArgumentParser(description='Generate a purely text document from the wikidump xml')
parser.add_argument('h1b', metavar='h', type=str, nargs=1, help='The address for the dump file')
parser.add_argument('occupations', metavar='o', type=str, nargs=1, help='The address in which to place.')
parser.add_argument('states', metavar='s', type=str, nargs=1, help='The address in which to place.')
args = parser.parse_args()

def incrementK(k, dictionary):
    if k in dictionary.keys():
        dictionary[k] += 1
    else:
        dictionary[k] = 0

inp = args.h1b[0]
outo = args.occupations[0]
outs = args.states[0]

print(inp)
print(outo)
print(outs)

with open(inp, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    i = 0
    states = {}

    for row in spamreader:
        if i == 1000000:
            break
        if row[2] == "CERTIFIED":
            incrementK(row[12], states)
        i += 1


print(states)
top_states = heapq.nlargest(len(states), states, key=states.get)
print([k for k in top_states])

f = open("tester.txt", mode='w')

for k in top_states:
    f.write(k+"\n")



f.close()