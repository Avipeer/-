tremp = input("do you have a ride? yes/no") == "yes"
if(tremp):
    print("take the ride")
else:
    niceday =  input("is it a nice day? yes/no") == "yes"
    print("asked nice day")
    schooldistance = input("is the school close? yes/no") == "yes"
    if niceday and schooldistance:
        print("walk")
    else:
        print("take the bus")
