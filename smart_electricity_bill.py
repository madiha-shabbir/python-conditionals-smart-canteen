# Electricity Bill Calculator using Loops & Conditionals

print("=== SMART ELECTRICITY BILL CALCULATOR ===")

# Loop to process multiple households
num_households = int(input("Enter number of households to calculate bill for: "))

for i in range(1, num_households + 1):
    print(f"\n--- Household #{i} ---")
    units = float(input("Enter electricity units consumed: "))
    
    # Calculate bill based on unit slabs
    if units <= 100:
        rate = 10
        total_bill = units * rate
    elif units <= 300:
        rate = 15
        total_bill = (100 * 10) + ((units - 100) * rate)
    else:
        rate = 20
        total_bill = (100 * 10) + (200 * 15) + ((units - 300) * rate)
        
    print(f"Total Bill for Household #{i}: Rs. {total_bill:.2f}")

print("\nAll calculations completed successfully!")

