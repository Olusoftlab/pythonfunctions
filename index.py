#function to calculate orihinal price by entrying price and discount price

def calculate_discount_price(price, discount_percent):
       
        discount_price=price *discount_percent
        final_price=price - discount_price
        
        print(final_price)
    

calculate_discount_price(20000, 0.005)


input_price=int(input("Enter the original price: "))
input_discount=input("Enter the discount price")

if (input_discount==""):
    print(input_price)
else:
    getDiscount=float(input_discount)
    calculate_discount_price(input_price, getDiscount)   

  
    