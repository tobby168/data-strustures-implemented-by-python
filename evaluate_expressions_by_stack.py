from stack import Stack 

# target: ( ( ( 52 + ( 10 + 22 ) ) * 2 * ( 11 + 12 ) ) )
# output: 3864

def string_to_result(input_str):

  input_list = input_str.split(' ')
  values = Stack()
  operators = Stack()
  
  for x in input_list:
    if x == '(':
      continue
    elif x == ')':
      if operators.pop() == '+':
        values.push(values.pop() + values.pop())
      else:
        values.push(values.pop() * values.pop())
    elif x == '+' or x == '*':
      operators.push(x)
    else:
      values.push(int(x))

  return values.pop()


str1 = '( ( ( 52 + ( 10 + 22 ) ) * 2 * ( 11 + 12 ) ) )'
print(string_to_result(str1))

