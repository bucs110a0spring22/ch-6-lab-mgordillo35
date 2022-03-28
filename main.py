'''
        Print the 3n+1 sequence from n, terminating when it             reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
'''

def seq3np1(n):
    count = 0

    while(n != 1):
      count = count + 1
        #print(n)    # delete the print function - may
      if(n % 2) == 0:        # n is even
            n = n // 2
      else:                 # n is odd
            n = n * 3 + 1
    return count


# PART B
def graphLine(turtle = None , x_up = 0, y_it = 0):
  upper_bound_2 = int(input(" A positive value for upper bound of range: "))
  
  max_value = upperboun


  wn = turtle.Screen()
  wn.setworldcoordinates()
  wn.bgcolor("light green")

  ray = turtle.Turtle() 
  ray.color("hot pink")
  ray.pensize(3)





def main():
  upper_bound = int(input(" A positive value for upper bound of range: "))
  if (upper_bound < 0):
    return # ask - is this how you end the program 

  for start in range (1, upper_bound + 1):
    seq3np1(upper_bound)
    print("The current loop value: ",start, "The number of iterations: ",seq3np1(start)) # ask - start  
    
  seq3np1(3)
main()
