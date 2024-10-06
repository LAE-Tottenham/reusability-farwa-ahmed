# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def input_opp1():
    opp1 = float(input("Enter your first triangle's opposite side length: "))
    return(opp1)
def input_adj1():
    adj1 = float(input("Enter your first triangle's adjacent side length: "))
    return(adj1)
opp1=input_opp1()
adj1=input_adj1()
    
import math
def find_hyp1():
    hyp1 = math.sqrt(opp1**2 + adj1**2)
    return(hyp1)


def input_opp2():
    opp2 = float(input("Enter your second triangle's opposite side length: "))
    return(opp2)
def input_adj2():
    adj2 = float(input("Enter your second triangle's adjacent side length: "))
    return(adj2)
opp2=input_opp2()
adj2=input_adj2()    

def find_hyp2():
    hyp2 = math.sqrt(opp2**2 + adj2**2)
    return(hyp2)
hyp2=find_hyp2()    


    import math
    hyp3 = math.sqrt(hyp1**2 + hyp2**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
