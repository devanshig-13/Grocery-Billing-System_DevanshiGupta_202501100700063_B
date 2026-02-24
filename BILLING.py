item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
item4 = float(input("Enter price of item 4: "))
item5 = float(input("Enter price of item 5: "))
q1 = int(input())
q2 = int(input())
q3 = int(input())
q4 = int(input())
q5 = int(input())
total = item1*q1 + item2*q2 + item3*q3 + item4*q4 + item5*q5
print(total)
if(total>100):
    discount = total* 0.1
    final_amount = total- discount
    print("Enter amount =", total)
    print("Discount =", discount)
    print("Final amount =", final_amount)
