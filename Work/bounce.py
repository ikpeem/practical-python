# bounce.py
#
# Exercise 1.5

#A ball is dropped from a height of 100 metres, each bounce is 3/5 of previous height
#Print first ten bounces

height = 100

for i in range(10):
    height *= 0.6
    print(round(height, 4))
