from stack import Stack 

# target: ( 52 + 32 ) * 2 * ( 11 + 12 + 32 )
# output: 9240

def string_to_result(input_str):

  input_list = input_str.split(' ')
  steps = Stack()
  nums = Stack()
  
  for x in input_list:
    if x == '(':
      steps.push('(')

    elif x == ')':
      steps.pop(
    
    else:
      nums.push(x)







str1 = '( 52 + 32 ) * 2 * ( 11 + ( 12 + 32 ) )'
string_to_result(str1)

