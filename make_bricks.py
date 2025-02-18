def make_bricks(small, big, goal):
    
    if goal % big and ( goal % small)  = 0:
       return True
    else
       return False
    
int main ():
  
  make_bricks(3, 1, 8)
  
  return 0; 


//AI Generation 

def make_bricks(small, big, goal):
    # Each big brick is 5 units
    max_big = min(goal // 5, big)  # Use as many big bricks as possible without exceeding goal
    remaining = goal - (max_big * 5)  # Remaining units to be filled with small bricks

    return remaining <= small  # True if small bricks can fill the remaining space

def main():
    print(make_bricks(3, 1, 8))  # Output: True

//Explanation of Code 
goal // 5
// is the integer division operator in Python.
goal // 5 calculates how many big bricks (each 5 units) we can use to get close to the goal without exceeding it.
For example, if goal = 8, then 8 // 5 would be 1 (since 5 goes into 8 one time).
2. min(goal // 5, big)
The min() function returns the smaller of the two values.
goal // 5 tells us the maximum number of big bricks that could fit into the goal.
big is the actual number of big bricks we have available.
So, min(goal // 5, big) ensures that we use the smaller number between:
How many big bricks we could use to reach the goal.
How many big bricks we actually have.
