total = 0

while True:
    user_input = input("Enter expense amount or 'quit' to stop: ")
    
    if user_input.lower() == 'quit':
        break
        
    try:
        expense = int(user_input)
        total += expense
    except ValueError:
        print("Invalid Data")

print(f"Total Spent: {total}")