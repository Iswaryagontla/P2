import re
txt = "Use of python in Machine Learning"
x = re.search("^Python.*in$",txt)
if(x):
    print("YES! We have a match!")
else:
    print("No match")