list_a = [8, 19, 148, 4, ]
list_b = [9, 1, 33, 83, ]
list_c = []


"""testcode

Parameter is below

"""
test = 1
list_c = [3, 4, 5, ]
list_d = [10, 20, 30, ]
list_e = []

# Add return to list_e

for c in list_c:
    # print(c * test) <-not needed
    for d in list_d:
        # e = c*d
        list_e.append(c*d)
        print(list_e)
