"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):

        """
        :type node: Node
        :rtype: Node
        """
        if(node==None):
            return None
        node_list=[node]
        # mapping node value to node
        mp={}
        while(node_list!=[]):
            vals=[node.val for node in node_list]
            # print(vals)
            node=node_list.pop()
            # print(node)
            newnode=Node(val=node.val,neighbors=[nb.val for nb in node.neighbors ])
            mp[node.val]=newnode
            for nb in node.neighbors:
                if(nb.val not in mp):
                    # print(nb)
                    node_list.append(nb)
        # print(mp)
        for key,node in mp.items():
            vals=[val for val in node.neighbors]
            # print(vals)
            nb_list= [mp[val] for val in node.neighbors]
            node.neighbors =nb_list

        return mp[1]


        
        
