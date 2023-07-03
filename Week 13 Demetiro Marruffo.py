#Demetrio Marruffo
#IST - 2310
#Try Any Treat Version 1
#11/20/22

#This program will take the input of prices of items purchased by the customer and then subtract the corresponding discount.

#This defines the input of the prices of the items purchased.
items_in_order = input("Enter all item prices seperated by space: ")

#This defines the input as a list. 
list  = items_in_order.split()

#This prints out letting the user know that this is the grand total.

print("Grand total: ")

#This computes the sum of the subtotal.
sum = 0
for num in list:
    sum += int(num)

#This counts the items in the list.
number_of_items = len(items_in_order)


#These if statements find the corresponding discount.

if number_of_items: 1
discoun_total = (sum * 1)

if number_of_items: 2
discount_total = (sum * -0.10)

if number_of_items: 3
discount_total = (sum * -0.15)

if number_of_items: 4 
discount_total = (sum * -0.20)

if number_of_items: 4-99    
discount_total = (sum * -0.20)

#This prints out the final grand total. 

print(sum + discount_total)

#This adds the message of a free item if it meets the criteria.

if number_of_items: 4-99    
print("Congrats you got a 20 pecent off discount!!!")