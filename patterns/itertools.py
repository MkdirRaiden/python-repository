import operator
import time 
L1 = [1, 2, 3]
L2 = [2, 3, 4] 
t1 = time.time()
a, b, c = map(operator.mul, L1, L2)
t2 = time.time()
print("Result:", a, b, c)
print("Time taken by map function: %.6f" %(t2 - t1))
t1 = time.time()
print("Result:", end = " ")
for i in range(3):
    print(L1[i] * L2[i], end = " ")
t2 = time.time()
print("\nTime taken by for loop: %.6f" %(t2 - t1)) 