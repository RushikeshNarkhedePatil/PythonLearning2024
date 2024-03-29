bob=['Bob Smith',42,30000,'software']
sue=['Sue Jones',45,40000,'hardware']
# Display all Record
print(bob)
print(sue)
# fetch name and pay
print(bob[0],sue[2])

# what's bob last name
print(bob[0].split()[-1])

# give sue a 25% raise
sue[2]=sue[2]*1.25
print(sue)