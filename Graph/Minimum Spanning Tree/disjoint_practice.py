class DisJointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)


    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] =  self.find(self.parent[item])
        return self.parent[item]


    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot

        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot

        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


vertices = ['A', "B", "C", "D", "E", "F"]
ds = DisJointSet(vertices)

ds.union('B', "E")
ds.union('C', "F")

print(f"Parent of E is {ds.find('E')}")
print("........")
print(f"Parent of F  is  {ds.find('F')}")
print("........")
