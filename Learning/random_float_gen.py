# We use random.random(a,b) function get a random value between the provided range but this function will not include number b 
import random
# We cannot pass any argument in random function directly
# this will print any random float between 0 and 1 excluding 1 
# to print a desired range from 0 to desired number multiple output by desired number
Random_float = random.random()
print(Random_float)