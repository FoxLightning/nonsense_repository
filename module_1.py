def snail(snail_map):
    # murk up memory
    sa = []
    # boundary conditions
    start_height = 0
    start_width = 0
    height = len(snail_map)
    width = len(snail_map)
    # current position
    row = 0
    col = 0
    # start sort
    while start_width < width and start_height < height:
        #1
        while col < width:
            sa.append(snail_map[row][col])
            col += 1
        col -= 1
        start_height += 1
        row = start_height
        #2
        while row < height:
            sa.append(snail_map[row][col])
            row += 1
        row -= 1
        width -= 1
        col = width - 1
        #3
        while col >= start_width:
            sa.append(snail_map[row][col])
            col -= 1
        col += 1
        height -= 1
        row = height - 1
        #4
        while row >= start_height:
            sa.append(snail_map[row][col])
            row -= 1
        row += 1
        start_width += 1
        col = start_width
    return sa





def test(snail):
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]

    print("Test 1: {}".format("Pass" if snail(array) == expected else "Fail"))


    array = [[1,2],
             [8,9]]
    expected = [1,2,9,8]

    print("Test 2: {}".format("Pass" if snail(array) == expected else "Fail"))

test(snail)