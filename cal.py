##Have the function Calculator(str) take the str parameter being passed and evaluate the mathematical expression within in. For example, if str were "2+(3-1)*3" the output should be 8.
##Another example: if str were "(2-0)(6/2)" the output should be 6.
##There can be parenthesis within the string so you must evaluate it
##properly according to the rules of arithmetic.
##The string will contain the operators: +, -, /, *, (, and ).
##If you have a string like this: #/#*# or #+#(#)/#,
##then evaluate from left to right. So divide then multiply,
##and for the second one multiply, divide, then add.
##The evaluations will be such that there will not be any decimal operations,
##so you do not need to account for rounding and whatnot. 
##
##Hard challenges are worth 15 points and you are not timed for them. Use the Parameter Testing feature in the box below to test your code with different arguments.
def Calculator(str): 
    # code goes here 
    # deal with () first
   # print(str)
   # print(eval(str))
    #if '(' in str:
     #   start = str.find('(')
      #  end = str.find(')')
     #   ans = Calculator(str[start+1:end])
    index = 1
    for s in str[1:-1]:
        if s == '(':
             
            if str[index-1].isdigit():
                 
                str = str[0:index] + "*" + str[index:]
        elif s == ')':
            if str[index+1] == '(':
                str = str[0:index+1] + "*" + str[index+1:]
        index = index + 1
    #print(str)
             
         
    
    
    return eval(str)
# keep this function call here  
print Calculator(raw_input())
