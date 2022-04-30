A = [[100, 'Yes'], [40, 'No'], [60, 'Maybe']]
print("Sorted List A based on index 0: % s"%(sorted(A, key=lambda x:x[0])))

B = [[2, 'Dog'], [0, 'Bird'], [7, 'Cat']]
print("Sorted List B based on index 1: % s"%(sorted(B, key=lambda x:x[1])))