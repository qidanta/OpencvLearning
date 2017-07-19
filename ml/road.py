def Dijkstra(G,v0,INF=999):
    '''get min distance from v0 to each node in G

    - Params:
    @G: node grah
    @v0: start node
    @INF: longest distance between never adjacent nodes

    - Returns:
    a dict of distance of v0 to others nodes
    '''
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