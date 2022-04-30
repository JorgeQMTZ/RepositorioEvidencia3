from operator import itemgetter

C = [[10, 8, 'Cat'], [90, 2, 'Dog'], [45, 6, 'Bird']]

print("Reversed sorted List C based on index 1:%s"%(sorted(C, key=itemgetter(1), reverse=True)))