name = input("Enter Consumer Name: ")
cid = input("Enter Consumer ID: ")
previous = float(input("Enter Previous Reading: "))
current = float(input("Enter Current Reading: "))
cost = float(input("Enter Cost per Unit: "))

units = current - previous
energy = units * cost
duty = energy * 0.05
fixed = 100
net = energy + duty + fixed

print("\nElectricity Bill")
print("Consumer Name =", name)
print("Consumer ID =", cid)
print("Units Consumed =", units)
print("Energy Charge =", energy)
print("Electricity Duty =", duty)
print("Fixed Meter Charge =", fixed)
print("Net Bill Amount =", net)
