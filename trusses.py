import argparse
parser = argparse.ArgumentParser()
parser.add_argument("graphfile")
parser.add_argument("size", type=int)

args = parser.parse_args()

graph = args.graphfile
sizeoftruss=args.size
graphlist = []
with open(graph) as f:
    for line in f:
        parts = line.split(" ")
        nodes = parts[0].rstrip()
        neigh = parts[1].rstrip()
        graphlist.append([nodes,neigh])

def neighbours(graphlist,node):
    g={}
    neighbour=[]
    for i in graphlist:
        if i[0]==node:
            g={i[0]: neighbour.append(i[1])}
        elif i[1]==node:
            g={i[1]: neighbour.append(i[0])}
    return g

def intersection(set1,set2):
    sets = set()
    s1 = set(set1)
    s2 = set(set2)
    sets = s1&s2
    return sets

def size(sets):
    return len(sets)

change = False
while change==False:
    for i in graphlist:
        if size(intersection(neighbours(graphlist,i[0]),neighbours(graphlist,i[1]))) < sizeoftruss-2:
            graphlist.remove(i)
            change=False
        else:
            change=True
print(graphlist)
