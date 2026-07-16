A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B
union = A.union(B)
print(union)    #{19, 20, 22, 24, 25, 26, 27, 28}

#Find A intersection B
intersection = A.intersection(B)
print(intersection)    #{19, 20, 22, 24, 25, 26}

#Is A subset of B
print(A.issubset(B))  #True

#Are A and B disjoint sets
print(A.isdisjoint(B))    #False

#What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(sym_diff)    #{27, 28}

#Join A with B and B with A
A.update(B)
print(A)    #{19, 20, 22, 24, 25, 26, 27, 28}

B.update(A)
print(B)    #{19, 20, 22, 24, 25, 26, 27, 28}   

#Delete the sets completely
del A
del B
del union
del intersection
del sym_diff
