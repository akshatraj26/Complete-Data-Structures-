class DisjointSet:
    # Time Complexity O(1)
    # Space Complexity O(n)
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)


    # find set
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] =  self.find(self.parent[item])
            return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot

        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] =  xroot
            self.rank[xroot] += 1


vertices = ['A', "B", 'C', "D", "E", "F"]
ds = DisjointSet(vertices)

# ds.union('B', "C")
# ds.union('B', "D")
#
#
# print(ds.find('D'))

ds.union('B', "E")
ds.union('C', "F")

print(f"Parent of E {ds.find('E')}")
print("........")
print(f"Parent of F  {ds.find('F')}")
