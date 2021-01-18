import sys


def get_dist(stars, a, b):
    return round(((stars[a][0] - stars[b][0]) ** 2 + (stars[a][1] - stars[b][1]) ** 2) ** 0.5, 2)

class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


n = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
edge = []
for i in range(n):
    for j in range(i, n):
        if i != j:
            edge.append([get_dist(stars, i, j), i, j])
edge.sort(key=lambda x: x[0])
cluster = DisjointSet(n)
result = 0
res =[]
for dist, s1, s2 in edge:
    if cluster.find(s1) != cluster.find(s2):
        cluster.union(cluster.find(s1), cluster.find(s2))
        res.append([s1, s2])
        result += dist
print(result)

