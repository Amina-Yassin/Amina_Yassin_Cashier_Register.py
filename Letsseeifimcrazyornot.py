#TURTLE IMPORTATION AND SETUP HERE
# Set up of the window and turtle in Main Function
#import turtle 
#TURTLE STUFF ENDS

#RANDOM IMPORTATION AND SETUP HERE
import random
dis = random.choice ([10, 20, 30])
#Discount is working so that is great
dis1 = dis/100
print ("Congratulations! As our 30000th customer, you get a discount of:", dis, "On today's purchase.")
#RANDOM STUFF ENDS

#FUNCTION NUMERO UNO HERE
def purchase_1(amount_1,discount):  
    total_1 = 0
    for accumulation in range (amount_1):
        x = input("Tell me the name of your item.")
        x_1 = float(input("Tell me the price of your item."))
        total_1 = total_1 + x_1
        print ()
        print (f"{x:<15} ${x_1}")
        print ()

    #print (total_1)
    GST = total_1 *1.05
    DIS1 = (GST *discount) 
    DIS2 = GST- DIS1
    final = (round(DIS2,2))   
    final=str(final)
    ans = (final,x)
    l = ("Your total is:")
    print (f"{l:<15} ${final}")
    return ans


def purchase_2(amount_2,discount):
    a = 0
    for accum in range(amount_2):
        purchase_1(amount_2,discount)
        print ()
        print (f"{x:<15} ${x_1}")
        print ()


#FUNCTION OF TURTLE DRAWING HERE
# def Birb(Turt,Size):
#     for spider in range(1):
#         Turt.begin_fill()
#         Turt.circle(Size)
#         Turt.end_fill()
#     for legs in range(1):
#         Turt.color("#EEB211")
#         Turt.begin_fill()
#         Turt.right(45)
#         Turt.forward(110)
#         Turt.left(135)
#         Turt.forward(115)
#         Turt.end_fill()
# #TURTLE FUNCTION ENDS

#OUTPUT OF FUNCTION
# amount = int(input("Please tell me the number of items you wish to purchase.")) 
# price = purchase_1(amount,dis1)
# print (price)
#OUTPUT OF TURTLE


def main():
    amount = int(input("Please tell me the number of items you wish to purchase.")) 
    price = purchase_1(amount,dis1)
    #print (price)
    # A1 = turtle.Screen()             
    # A1.bgcolor("lightgreen")
    # Ayo = turtle.Turtle()          
    # Ayo.pensize(3)
    # Ayo.color("#071733")
    # Ayo.right(90)
    # Ayo.speed(100)
    # Amina = Birb(Ayo,100)
    # A1.exitonclick()

if __name__ == "__main__":
    main()