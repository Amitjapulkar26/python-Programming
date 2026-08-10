car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "blue"
}

# Remove color
car.pop("color")

# Display all key-value pairs
print(car.items())

# Check whether model exists
if "model" in car:
    print("Model key exists")
else:
    print("Model key does not exist")