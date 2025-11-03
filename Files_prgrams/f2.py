def function2(age,name):
 print name
 print age
 return

function2(35, name="minku")
#incorrect assignment, non-keyword argument after a keyword argument
#def function2(name,age)
#function2(name="minku",age)
 
def function3(name,age=35):
 print "name is ", name
 print "age is ", age


function3("rosy")


