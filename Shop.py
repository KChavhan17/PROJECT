cn=input("Enter Customer Name:")
pn=input("Enter Product Name:")
pp=int(input("Enter Product Price:"))
q=int(input("Enter Quantity:"))
gst=int(input("Enter GST percentage:"))
dc=int(input("Enter Delivery Charge:"))
inv="INV20250S20"
id="20 May 2025"

Total_Price=pp*q
GST_Amount=Total_Price*gst%100
Final_Bill_Amount=Total_Price+GST_Amount+dc

print(f"\nCustomer Name  : {cn}")
print(f"Invoice Number : {inv}")
print(f"Invoice Date : {id}\n")

print(f"{'PRODUCT DETAILS':<20} {'PRICE(INR)':<20} {'QUANTITY':<20} {'Total(INR)':<20}")
print(f"\n{pn:<20} {pp:<20} {q:<20} {pp*q}")
print("-"*75)
print(f"\n{'Total Price':<62} {pp*q}")
print(f"{'GST(18%)':<62} {GST_Amount}")
print(f"{'Delivery Charge':<62}  {dc}\n")
print("-"*75)
print(f"{'Final Bill Amount':<20} {Final_Bill_Amount}\n")
print("Thank you for shopping with ShopSmart!")

      

