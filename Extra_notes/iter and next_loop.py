fruits = ['apple', 'banana', 'mango', 'orange']
iter_object = iter(fruits)
while True:
    try:
        fruit = next(iter_object)
        print(fruit)
    except StopIteration:
        break 
        
