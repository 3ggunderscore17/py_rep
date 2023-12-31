import numpy as np
E= np.array([0,2,4,6,8])
N= np.array([1,2,3,4,5,])
result1= np.union1d(E, N)
result2= np.intersect1d(E, N)
result3= np.setdiff1d(E, N)
result4= np.setxor1d(E, N)
print(f"The union of sets E and N is{result1}")
print(f"The intersection of sets E and N is{result2}")
print(f"The difference of sets E and N is{result3}")
print(f"The symmetric difference of sets E and N is{result4}")