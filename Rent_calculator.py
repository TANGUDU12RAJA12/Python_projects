## inputs we need from user
# Total rent
#total fodorderred for snacking 
#electricit units spend 
# Charge per unit 
#Person living in room/flat

## out put 
# total amount you have to  pay

Rent = int(input("Enter your hostel/flat rent = "))
Food = int(input("Enter the amount of food ordered =  "))
Electicity_spend = int(input("Enter the total of electicity spend in terms of units = "))
Charge_per_unit  = int(input("Enter the charge per unit = "))
person  = int(input("Enter the nuber of person living in room/flat = "))

Total_bill = Electicity_spend*Charge_per_unit
Out_put = (Food + Rent + Total_bill) // person

print("Each person to pay : ",Out_put)
