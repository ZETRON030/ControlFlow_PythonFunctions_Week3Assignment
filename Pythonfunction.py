
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


#Applying a valid  discount price
Original_price = 123200
discount_percent = 27
result = calculate_discount(Original_price, discount_percent)
print(f"Final price: {result}")

#Discount too low
price = 123200
discount_percent = 15
result = calculate_discount(Original_price, discount_percent)
print(f"Final price: {result}")
