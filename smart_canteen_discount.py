# Topic 1: Conditional Statements
# Program 1: Smart Canteen Discount System with Improvements

print("===== SMART CANTEEN =====")

# Improvement 1: User ka naam pochna
student_name = input("Enter your name: ")

bill_amount = float(input("Enter your total bill amount (Rs.): "))

# Improvement 2: Rs. 5000 se zyada par 25% discount ki nayi condition add ki hai
if bill_amount >= 5000:
    discount_rate = 25
elif bill_amount >= 3000:
    discount_rate = 20
elif bill_amount >= 2000:
    discount_rate = 10
elif bill_amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount_amount = bill_amount * discount_rate / 100
final_amount = bill_amount - discount_amount

print("\n===== BILL SUMMARY =====")
print(f"Student Name: {student_name}")
print(f"Original Bill: Rs. {bill_amount:.2f}")
print(f"Discount Rate: {discount_rate}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Payable: Rs. {final_amount:.2f}")
print("========================")
print(f"Thank you {student_name} for visiting Smart Canteen! Enjoy your meal! 🍔")