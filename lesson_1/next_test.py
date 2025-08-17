def count_up_to(max_count):
     count = 1
     while count <= max_count:
         yield count
         count += 1

counter = count_up_to(5)
print(next(counter))
# 1
print(next(counter))
# 2
next(counter)
# 3
print(next(counter))
# 4
next(counter)
# 5
print(next(counter))
# StopIteration