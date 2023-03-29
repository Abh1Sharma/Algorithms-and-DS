# Abhi Sharma 1006700438
# Credited Websites: Geeks4Geeks:https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
#Stack overflow code used from various sites for cmd line reading_input and _name_ functions and graph class functions

# sample input text for the file
# python python.py gnutella.txt T 
# T can take any value 0-10.     

import heapq
import sys
import time
import argparse


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]
        
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        
    def dijkstra(self, source):
        dist = [sys.maxsize] * self.num_nodes
        dist[source] = 0
        visited = [False] * self.num_nodes
        heap = [(0, source)]
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in self.adj_list[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return dist
    
    def get_spread(self, source, T):
        dist = self.dijkstra(source)
        spread = sum(1 for d in dist if d <= T)
        return spread


def find_top1_influencer(graph, T):
    max_spread = -1
    top1_node = -1
    start_time = time.time()
    for u in range(graph.num_nodes):
        spread = graph.get_spread(u, T)
        if spread > max_spread:
            max_spread = spread
            top1_node = u
    end_time = time.time()
    return top1_node, max_spread, (end_time - start_time)

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    graph = Graph(0)
    for line in lines:
        u, v, weight = map(float, line.split())
        num_nodes = int(max(u, v)) + 1
        if num_nodes > graph.num_nodes:
            graph = Graph(num_nodes)
        graph.add_edge(int(u), int(v), weight)
    return graph

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find top influencer in a graph')
    parser.add_argument('filename', type=str, help='input graph file')
    parser.add_argument('threshold', type=float, help='threshold value')
    args = parser.parse_args()
    
    graph = read_input(args.filename)
    top1_node, max_spread, time_taken = find_top1_influencer(graph, args.threshold)
    print('TOP-1 INFLUENCER: {}, SPREAD: {}, TIME: {:.2f} sec'.format(top1_node, max_spread, time_taken))




