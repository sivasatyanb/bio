class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    queue = []
    visited = []
    
    visited.append(root)
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        print(node.value)
        
        if node.left and node.left not in visited:
            visited.append(node.left)
            queue.append(node.left)
            
        if node.right and node.right not in visited:
            visited.append(node.right)
            queue.append(node.right)


node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)
node4 = Node(value=4)
node5 = Node(value=5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

bfs(node1)


# class Solution:
#     def levelOrder(self, root: list[list[int]]):
        
#         visited = []
#         queue = []
#         levelOrder = []
        
#         visited.append(root[0])
#         queue.append(root[0])
        
#         while queue:
#             s = queue.pop(0)
#             levelOrder.append(s)
            
#             for node in root[s]:
#                 if node not in visited:
#                     visited.append(node)
#                     queue.append(node)
        
#         return levelOrder

# instance = Solution()
# levelOrder = instance.levelOrder(root = [[3],[9,20],[15,7]])
# print(levelOrder)