class Solution:
    def find(self, dsuf, v):
        if dsuf[v] == 1:
            return v
        dsuf[v] = self.find(dsuf, dsuf[v]) 
        return dsuf[v]

    def findRedundantConnection(self, edges):
        n = len(edges)
        dsuf = [-1] * (n + 1)

        for edge in edges:
            parent_x = self.find(dsuf, edge[0])
            parent_y = self.find(dsuf, edge[1])

            if parent_x == parent_y:  
                return edge
            else: 
                dsuf[parent_x] = parent_y
        
        return [0, 0]