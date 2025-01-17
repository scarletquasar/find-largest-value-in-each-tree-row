from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        curr_node = stack.pop()
        values.append(curr_node.val)

        if curr_node.right:
            stack.append(curr_node.right)

        if curr_node.left:
            stack.append(curr_node.left)

    return values


def bfs(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        curr_node = queue.popleft()
        values.append(curr_node.val)

        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)

    return values


if __name__ == '__main__':
    root = Node(1, Node(3, Node(5), Node(3)), Node(2, None, Node(9)))
    print(dfs(root)) # [1, 3, 5, 3, 2, 9]
    print(bfs(root)) # [1, 3, 2, 5, 3, 9]
