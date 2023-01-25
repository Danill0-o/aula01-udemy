import csv

# Get user input
stock = input("Enter stock name: ")
entry_price = input("Enter entry price: ")
quantity = input("Enter quantity: ")

# Create a list with the data
data = [[stock, entry_price, quantity]]

# Export the data to a CSV file
with open("stock_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Entry price", "Quantity"])
    writer.writerows(data)

print("Data successfully exported to stock_data.csv!")