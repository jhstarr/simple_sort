
# Jeff Starr, 28 September 2017


# I created this to help my daughter with an assignment in her HS java class.
# This code goes through a list comparing each number to the next and switching 
# them if the bigger number comes first in the pair.  
# It goes through the list multiple times 
# switching numbers until it goes through the whole list without 
# doing any switches (so that switches = 0).  At that point, the code breaks 
# out of the loop. Temp is a temporary place to hold a value while 
# doing a swap.  stacks[i] is the height of 1 stack and stack[i+1] 
# is the height of the next stack.  It is a list in python.


stacks = [3,5,0,8,3,6,4,10]

temp = 0

# while True will always execute.  This program relies on the break
# statement to stop when switches == 0.

while True:
    switches = 0
    i = 0
    while i < len(stacks)-1:
        if stacks[i] > stacks[i+1]:
            temp = stacks[i]
            stacks[i] = stacks[i+1]
            stacks[i+1] = temp
            switches += 1
        i +=1
    if switches ==0:
        break

print(stacks)

