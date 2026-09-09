x=10
if x == "Java" or "Python":
  print("This one")
  
else:
    print("That one")
    
## The above code will always print "This one" because the condition is not properly structured.Also, the condition is taken to be true because "Python" is a non-empty string, which is considered true in Python. To fix this, you should compare x to both "Java" and "Python" separately: