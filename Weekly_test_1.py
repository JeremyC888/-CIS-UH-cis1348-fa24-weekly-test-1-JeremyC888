"""CIS 1348 Weekly Test 1"""

# This code collects information about the user and then displays it
# This code is not working. Please fix it.
# Rename the variables using the conventions learned in the course
# and add useful comments

# Asking for user input
print("\n")
f = input("1) First name: ")
l = input("2) Last name: ")
pp = input("3) Prefix of phone number (e.g., 123): ")
n = input("5) Street Number of your residence : ")
sn = input("5) Street name : ")

city = input("6) City: ")
state = input("7) State: ")
zip_code = input("8) Zip code: ")

# Constructing the required return values
fullname = f + " " + l
phonenumber = pp+"-xxx-xxxx"
fulladdress1 = n + " " + sn
full_address_line2 = city + ", " + state + " " + zip_code

# Display the results
print("\n")
print("Collected Information:")
print("\n")
print("Full Name: ",fullname)
print("Phone Number: ",phonenumber)
print("Full Address: ")
print(fulladdress1)
print(full_address_line2)
