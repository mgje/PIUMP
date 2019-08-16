#Rundreise


def rundreise(cities,path):
    if len(cities)<2:
        path.append(cities[0])
        print path
        return
    for i in range(len(cities)):
        el = cities[i]
        ## Listen kopieren
        c = cities[:]
        p = path[:]
        c.remove(el)
        p.append(el)
        rundreise(c,p)

rundreise(["A","B","C"],["S"])
    