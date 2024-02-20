import math
def minimax(tree,depth):
    max_turn=bool(depth%2)
    for i in range(depth):
        zipped = zip(tree[::2],tree[1::2])
        if max_turn:
            tree=[max(a,b) for a,b in zipped]
        else:
            tree=[min(a,b) for a,b in zipped]
        max_turn = not max_turn
    return tree[0]
tree=[1,2,3,-4,5,6,7,-9]#input("Enter the elements of the array divided by space")
#array1=[int(x)for x in tree.split()]
depth=math.ceil(math.log(len(tree),2))
print(f"Minimax Algorithm Result is : {minimax(tree,depth)}")