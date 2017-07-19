
G = {1:{1:0,    2:6,    4:6},
     2:{1:6,    2:0,    3:6, 5:6},
     3:{2:6, 3:0, 6:6},
     4:{1:6,    4:0, 5:6,   7:6},
     5:{2:6, 4:6, 5:0, 6:6, 8:6},
     6:{3:6, 5:6, 6:0, 9:6},
     7:{4:6, 7:0, 8:6},
     8:{5:6, 7:6, 8:0, 9:6},
     9:{6:6, 8:6, 9:0}}

def create_rect_grah(n, distance):
    grah = {}
    for row in range(n):
        for col in range(n):
            line = {}
            nodes = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
            for node in nodes:
                if n> node[0] >= 0 and n > node[1] >= 0:
                    index = node[0] * n + node[1] + 1
                    line[index] = distance
            index = row * n + col + 1
            line[index] = 0
            grah[index] = line
    return grah



def Dijkstra(G,v0,INF=999):
    book = set()
    minv = v0
    
    dis = dict((k,INF) for k in G.keys())
    dis[v0] = 0
    
    while len(book)<len(G):
        book.add(minv)                                  
        for w in G[minv]:                               
            if dis[minv] + G[minv][w] < dis[w]:          
                dis[w] = dis[minv] + G[minv][w]         
        
        new = INF                                       
        for v in dis.keys():
            if v in book: continue
            if dis[v] < new: 
                new = dis[v]
                minv = v
    return dis


G = create_rect_grah(3, 6)
dis = Dijkstra(G,v0=1)
dis2 = Dijkstra(G, v0=3)
distance = dis[3] + dis2[9]
print (distance)
print (dis, dis2)