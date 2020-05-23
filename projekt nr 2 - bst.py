import random
import time
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif key > root.val:
        root.right = deleteNode(root.right, key)

    else: #znaleziono odpowiedni element

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right) #najmniejszy element poniżej usuwanego wchodzi na jego miejsce
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val) #i jest usuwany
    return root

def fill_incr(root, count):
    if root:
        for i in range(count):
            insert(root, Node(i))

def fill_rand(root, count):
    if root:
        tab = []
        for i in range(count):
            tab.append(i)
        random.shuffle(tab)
        for i in tab:
            insert(root, Node(i))

def sortedArrayToBST(arr):
    temp = None

    if len(arr) >= 1:
        # find middle
        mid = int((len(arr)) / 2)

        # make the middle element the root
        temp = Node(arr[mid])

        if len(arr) >= 2:
            # left subtree of root has all
            # values <arr[mid]
            temp.left = sortedArrayToBST(arr[:mid])

            if len(arr) >= 3:
                # right subtree of root has all
                # values >arr[mid]
                temp.right = sortedArrayToBST(arr[mid + 1:])

    return temp

def fill_balanced(root, count):
    if root:
        tab = []
        for i in range(count):
            tab.append(i)
        insert(root, sortedArrayToBST(tab))

def search(root, value):
    if root:
        if root.val < value:
            search(root.left, value)
        elif root.val > value:
            search(root.right, value)
        #else:
        #    print(root.val)

def search_rand(root, count):
    if root:
        tab = []
        for i in range(count):
            tab.append(i)
        random.shuffle(tab)
        for i in tab:
            search(root, i)

def delete_rand(root, count):
    if root:
        tab = []
        for i in range(count):
            tab.append(i)
        random.shuffle(tab)
        for i in tab:
            root = deleteNode(root, i)
        return root

def fill(method, root, count):
    if method == "rosnące":
        fill_incr(root, count)
    elif method == "losowe":
        fill_rand(root, count)
    elif method == "zbalansowane":
        fill_balanced(root, count)

def main():

    print("wypełnienie drzewa | wielkość instancji | wykonywana akcja | czas wykonania")

    for method in [ "rosnące","losowe","zbalansowane" ]:

        for instance_size in [ 500,1000,1500,2000,2500,3000,3500,4000,4500,5000 ]:

            bst = Node(0)
            start = time.time()
            fill(method, bst, instance_size)
            end = time.time()
            #inorder(bst)
            print(method + " " + str(instance_size) + " wypełnianie " + str(end - start))

            start = time.time()
            search_rand(bst, instance_size)
            end = time.time()
            print(method + " " + str(instance_size) + " wyszukiwanie " + str(end - start))

            #start = time.time()
            delete_rand(bst, instance_size)
            #end = time.time()
            #print(method + " " + str(instance_size) + " usuwanie " + str(end - start))

main()