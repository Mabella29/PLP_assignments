

def calculate_discount(price, discount_percent):
     if discount_percent >= 20:
          discount_amount = price * (discount_percent / 100)
          final_price = price - discount_amount
          return final_price
     else:
         return price
user_input = float(input("Enter the Original price "))
u_input = float(input("Enter the discount percent "))
     

price = user_input
discount_percent = u_input

final_price = calculate_discount(price, discount_percent)
     
if discount_percent >= 20:
    print(f"The final price after discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")    