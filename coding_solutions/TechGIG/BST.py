class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def insert(root, node):
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


def main():
    N = int(input())
    inp = list(map(int, input().split()))
    r = Node(inp[0])
    for i in range(1, N):
        insert(r, Node(inp[i]))
    inorder(r)


main()
