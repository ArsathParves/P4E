scores = input("Enter Score: ")
score=float(scores)
if score>1.0:
    print("Enter a proper Grade with in range below 1.0")
if score<0.6:
   print("F")
   exit()
if score>= 0.9:
    print("A")
    exit()
if score>= 0.8:
    print("B")
    exit()
if score>= 0.7:
    print("C")
    exit()
if score>= 0.6:
    print("D")
    exit()
#not elif can be also used for this and I have a to redo this because this is pretty simple program i wrote in a lenthy way.
