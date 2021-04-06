def postorder(root):
    global Child
    if Child[root][0] != 0:  # Traverse Inner Vertices
        for i in range(Child[root][0]):
            postorder(Child[root][i + 1])
    print(root, end=' ')


# Child = [[3, 1, 2, 3], [0], [1, 4], [1, 5], [2, 6, 7], [0], [0], [0]]
# Initialize child as a global variable
# This data structure mirrors that of Ex. 2.30 where the first element in each subarray stores the number of children
Child = [[4, 1, 2, 3, 4], [0], [0], [1, 5], [3, 9, 10, 11], [2, 6, 7], [0], [1, 8], [0], [0], [0], [1, 12], [0]]
Color = ['red'] * len(Child)
Dis = [0] * len(Child)  # array to store each vertex's distance to the furthest leaf


def color_win_loss(root):
    global Child, Dis, Color
    if Child[root][0] == 0:  # the vertex is a Leaf
        Color[root] = 'green'
    else:  # traverse inner vertices
        min_dis_child = Child[root][1]
        for i in range(Child[root][0]):
            child = Child[root][i + 1]
            color_win_loss(child)
            # Find distance to the furthest leaf
            if Dis[child] >= Dis[root]:
                Dis[root] = Dis[child] + 1
            # Find the min distance in all children
            if Dis[child] < Dis[min_dis_child]:
                min_dis_child = child
        # Set color to the opposite of that of the min distance child
        if Color[min_dis_child] == 'red':
            Color[root] = 'green'
        else:
            Color[root] = 'red'
    print(root, Color[root])


# Driver to initiate the process
if __name__ == '__main__':
    color_win_loss(0)
    [print(i, end=' ') for i in Dis]
