import numpy as np


def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape

    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))

    return neighbours


# Current optimization objective: local/global maximum
def hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
    for neighbour in neighbours: #Find the neighbour with the greatest value
        if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbour
            ascended = True

    return ascended, next_state


def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6)  # matrix index coordinates
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ", landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ", landscape[current_state[0]][current_state[1]])


__main__()


""" :::::::: OUTPUT ::::::::

[[23 38 49  1 19 14 28  3 32  4]
 [43 43 30 33 33  2 28  8 31 21]
 [ 7 13 13  5 40  2  5  7 16 41]
 [31  1 43  7 19 28 35 12 48 38]
 [22 32 27  3 17 38 11 32  3  2]
 [ 5 15 20  2 32 44 31 32 34 46]
 [48 36 12 12  4 49 43 47  3 18]
 [33  7  2 16  1 46  1 42 30 25]
 [24  9 37 25 10 26  4 22  2 41]
 [40 49  1  9 13 33 10 41 32 43]]

Step # 1
Current state coordinates:  (3, 6)
Current state value:  35

Step # 2
Current state coordinates:  (4, 5)
Current state value:  38

Step # 3
Current state coordinates:  (5, 5)
Current state value:  44

Step # 4
Current state coordinates:  (6, 5)
Current state value:  49

Step # 5
Optimization objective reached.
Final state coordinates:  (6, 5)
Final state value:  49

"""
