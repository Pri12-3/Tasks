def set_op(E, N):
    union_set = E | N
    intersection_set = E & N
    difference_set = E - N
    symmetric_diff_set = E ^ N
    
    print(f"Union of E and N is {union_set}")
    print(f"Intersection of E and N is {intersection_set}")
    print(f"Difference of E and N is {difference_set}")
    print(f"Symmetric difference of E and N is {symmetric_diff_set}")

E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

set_op(E, N)
