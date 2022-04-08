

def get_p_distance(list1, list2):
    index = 0
    difference = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            difference +=1
        index +=1
    p_distance = difference / len(list1)
    return p_distance

def get_p_distance_matrix(dataset):
    p_distance_matrix = []
    for row_list in dataset:
        row = []
        for column_list in dataset:
            row.append(get_p_distance(row_list,column_list))
        p_distance_matrix.append(row)
    return p_distance_matrix