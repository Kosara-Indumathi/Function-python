# if user's age is less than 18 , print “not eligible “,else if user's age is greater than or equal to 18, print “you are eligible"
def eligible_for_vote(a):
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
a=int(input("enter the number"))
eligible_for_vote(a)

