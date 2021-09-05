import numpy as np


# Recursive method of finding the "deepest" node in a tree using a method similar to DFS

# Tree definition:
# Each vector represents a single node in the tree, which each element representing attributes.
# [<PARENT NODE'S ID>,  <THIS NODE'S ID>,  <WEIGHT/EDGE LENGTH>,  <DEPTH IN TREE>]

nodeTree = np.array([[0, 1, 0, 0], [1, 2, 5, 0], [1, 3, 8, 0], [2, 4, 11, 0], [4, 5, 15, 0], [3, 6, 21, 0], [5, 7, 2, 0]])


def getMaxDepth(myNode, parentDepth):
    myWeight = nodeTree[myNode - 1, 2] # Retreive weight/length from array
    myDepth = myWeight + parentDepth # Calculate current node's depth in tree

    nodeTree[myNode - 1, 3] = myDepth # Update array with node's depth

    maxChildDepth = 0
    temp = 0
    for node in nodeTree:
        if node[0] == myNode:
            temp = getMaxDepth(node[1], myDepth) # Calling function now as the child node

            if temp > maxChildDepth: # Obtaining max
                maxChildDepth = temp

    if myDepth < maxChildDepth:
        return maxChildDepth
    else:
        return myDepth


# Calling recursive function with initial conditions
print(f"Maximum depth in tree: {getMaxDepth(1, 0)}")

depthValues = list(nodeTree[:, 3])
endNode = depthValues.index(max(depthValues))

# Finding the particular path to the deepest node in tree
branchPath = []
while endNode >= 0:
    branchPath.append(nodeTree[endNode, 1])
    endNode = nodeTree[endNode, 0] - 1

print(f"Longest path: {' -> '.join(str(node) for node in reversed(branchPath))}")

print(f"\nUpdated nodeTree:\n{nodeTree}")