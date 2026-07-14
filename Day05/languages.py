#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)    #['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

#Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)    #'HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']
