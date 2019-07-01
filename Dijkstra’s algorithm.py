import time
start_time = time.monotonic()

graph = {
'a' : {
'b' : [5,2], 'c' : [3,4], 'd' : [8]
},
'b' : {
'a' : [5, 2], 'd' : [3] #ну, тут, крч, все создается и тд и тп, трали-вали
},
'c' : {
'a' : [2, 4], 'd' : [3]
},
'd' : {
'a' : [8], 'b' : [3], 'c' : [3]
}
}
dots = ['a','b','c']
road = dict([])

def cut_road(lengthsRoad):
    for dot in dots:                                    #тут, крч, убираем все лишнии пути, с условием, что у них такая же длина, и А уже направлена только в сторону B, исходя из min()
        if (len(lengthsRoad) > 1) and (not (dots.index(dot)+1) == len(dots)):
            try:
                lengthsRoad[dot] = min(lengthsRoad[dot])
                if(lengthsRoad[dots[dots.index(dot) + 1]][0] != lengthsRoad[dot]):
                    lengthsRoad.pop(dots[dots.index(dot) + 1])                      #то самое условие и исключение лишней вершины
            except:
                continue
        else:
            continue
    standartLengths = [i for i in lengthsRoad.values() if not type(i) is list]
    listerLengths = [i[0] for i in lengthsRoad.values() if type(i) is list]
    lengthsValues = standartLengths + listerLengths
    road_dots = ''.join(lengthsRoad.keys()) + 'd'
    max_length = sum(lengthsValues)
    return max_length #а вот и результат
        
    
def find_road(): 
    global all_roads
    all_roads = {}
    for key, value in graph.items():
        if key != 'd':                 #d нам в all_roads не нужно, тк после неё не идет веток.
            all_roads[key] = []
            all_roads[key] = [roadValue for roadKey, roadValue in road.items() if key == roadKey[0]] #лень вникать в условие
        else:
            continue
    return cut_road(all_roads)

def road_map(key, dotKey): #создаем парные комбинации, из каждой точки: ab ac ad 
    for weight in graph[key][dotKey]:
        ownKey = ''.join(sorted(key + dotKey))
        if( ownKey in road ): 
            if( (road[ownKey] == []) or (road[ownKey][0] > weight) ):                 #хз, что тут. Я отходил на полтора часа
                road[ownKey] = graph[key][dotKey][graph[key][dotKey].index(weight)]
            else:
                continue
        else:
            road[ownKey] = []

for key, value in graph.items(): #проходимся по всем элементам графа, возвращая списки из одного элемента для каждой вершины/узла, исходя из условия ниже
    for dotKey, dotValue in graph[key].items():
        if len(dotValue) > 1: #условие, исходя из которого возвращаем min(dotValue), чтобы избавиться от лишних, длинных путей в другие точки.
            graph[key][dotKey] = [min(dotValue)]
            road_map(key, dotKey)
        else:
            road_map(key, dotKey)
    pass

if __name__ == '__main__':
    print(find_road()) #О, ПРИВЕТ
    print(time.monotonic() - start_time)
else:
    quit()
