import turtle

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
def lineGraph(upper_bound):
  bert = turtle.Turtle()     #draw graph 
  pete = turtle.Turtle()      #write out max
  wn = turtle.Screen()
  wn.setworldcoordinates(0 , 0 , 10 , 10)

  pete.pu()
  pete.goto(0,10)
  
  max_so_far = 0
  for x in range(1, upper_bound + 1):
    result = seq3np1(x)
    
    if result > max_so_far:
      max_so_far = result


    pete.goto(0, max_so_far)
    max_text = "Maximum so far: ", x , result
    pete.clear()
    pete.write(max_text)
  
    wn.setworldcoordinates(0 , 0, x + 10, max_so_far + 10 )
    bert.pd()
    bert.goto(x, result)

  wn.exitonclick


  

def main():
  upper_bound = int(input(" A positive value for upper bound of range: "))
  if (upper_bound < 0):
    return

  for start in range (1, upper_bound + 1):
    seq3np1(upper_bound)
    print("The current loop value: ",start, "The number of iterations: ",seq3np1(start)) # ask - why start is being used
    
  seq3np1(3)
  lineGraph(upper_bound)
  
main()
