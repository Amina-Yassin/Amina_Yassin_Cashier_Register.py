def purchase_1(amount_1):  
    total_1 = 0
    for accumulation in range (amount_1):
        x = input("Tell me the name of your item.")
        x_1 = float(input("Tell me the price of your item."))
        total_1 = total_1 + x_1
        print (total_1)
    total_1=str(total_1)
    ans = (total_1,x)
    return ans


# def purchase_2(amount_2):
#     for name in range (amount):

#         purchase_1(amount_2)
#     return x 

amount = int(input("Please tell me the number of items you wish to purchase.")) 
price = purchase_1(amount)

print (price)