#IMPORT RANDOM
import random
dis = random.choice ([10, 20, 30])
#Discount is working so that is great
dis1 = dis/100

print ("Congratulations! As our 30000th customer, you get a discount of:", dis, "On today's purchase.")

def purchase_1(amount_1, discount):  
    total_1 = 0
    for accumulation in range (amount_1):
        x_1 = float(input("Tell me the price of your item."))
        total_1 = total_1 + x_1
        print (total_1)
    GST = total_1 *1.05
    DIS1 = (GST *discount) 
    DIS2 = GST- DIS1
    final = (round(DIS2,2))
    return final

#Output
amount = int(input("Please tell me the number of items you wish to purchase.")) 
price = purchase_1(amount,dis1)
print ("Your Total is", price, "Have a nice day!")
