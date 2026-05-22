# Expense Tracker - DecodeLabs Project 2
# Author: Divya Bharti
# Batch: 2026

total = 0  # Accumulator initialized OUTSIDE loop

print("=" * 40)
print("   💰 Divya's Expense Tracker")
print("      Powered by DecodeLabs")
print("=" * 40)
print("Enter expenses one by one.")
print("Type 'quit' to see total.\n")

while True:
    user_input = input("Enter expense amount: ")
    
    # Kill switch
    if user_input.lower() == 'quit':
        break
    
    # Defensive coding
    try:
        expense = float(user_input)
        total += expense  # Accumulator
        print(f"✅ Added! Running total: ${total:.2f}")
    except ValueError:
        print("❌ Invalid input! Enter a number.")

print("\n" + "=" * 40)
print(f"   FINAL TOTAL: ${total:.2f}")
print("=" * 40)
