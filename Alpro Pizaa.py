#Welcome
print('Welcome To Yudha Pizza Shop')
print('We will prepare Your Delicious Pizza Rigth away ')


#The very first bill
Total_harga = 0

# Pizza type
print('Select Your Pizza Type')
print('1.Meat Lovers       | Rp.39000')
print('2.Cheese Lovers     | Rp.40000')
print('3.Tuna Meat         | Rp.43000')
print('4.American Favorite | Rp.38000')
print('5.Chicken Lovers    | Rp.40000')
Type = input('select your pizza ( 1-5 ): ')
if Type == "1":
    print('your pizza is Meat Lovers !!')
    Total_harga += 39000
if Type == "2":
    print('your pizza is Cheese Lovers !!')
    Total_harga += 40000
if Type == "3":
    print('your pizza is Tuna Meat !!')
    Total_harga += 43000
if Type == "4":
    print('your pizza is American Favorite !!')
    Total_harga += 38000
if Type == "5":
    print('your pizza is Chiken Lovers !!')
    Total_harga += 40000

# Size
size = input('Please Choose the size for your pizza ( S(No Charge), M(25k), L(45k)) : ')
if size.lower() == "s":
    print('Your Pizza Size is Small ( S )')
    Total_harga += 0
if size.lower() == "m":
    print('Your Pizza Size is Medium ( M )')
    Total_harga += 25000
if size.lower() == "l":
    print('Your Pizza Size is Large ( L )')
    Total_harga += 45000

# Crust
crust = input('Please Choose the Crust for your pizza ( Thin(10k) or Thick(15k) : ) ')
if crust.lower() == "thin":
    print('Your pizza crust is Thin')
    Total_harga += 10000
if crust.lower() == "thick":
    print('Your pizza crust is thick')
    Total_harga += 15000

# Extra cheese
chesse = input('Do you want the extra Cheese? Only For 8k !! (Y/N) : ')
if chesse.lower() == "y":
    print('Okay Your pizza is filled with extra Cheese')
    Total_harga += 8000
elif chesse.lower() == "n":
    print('Your pizza has the Normal Cheese portion')

# Topping
Pilih_topping = input('Do you want add topping to your pizza? (Y/N) : ')
if Pilih_topping.lower() == "y":
    topping = input('Please choose topping for your pizza (Onion, Peperoni, Meat, Mushroom ,Sausage)')
    if topping.lower() == "onion":
        print('Your topping is ', topping) 
        Total_harga += 1000
    if topping.lower() == "peperoni":
        print('Your topping is ', topping) 
        Total_harga += 1000
    if topping.lower() == "meat":
        print('Your topping is ', topping) 
        Total_harga += 1000
    if topping.lower() == "mushroom":
        print('Your topping is ', topping)
        Total_harga += 1000 
    if topping.lower() == "sausage":
        print('Your topping is ', topping) 
        Total_harga += 1000
    tambah_topping1 = input('Do you want the extra topping? (Y/N) : ')
    if tambah_topping1 == "y":
        topping1 = input('Please choose extra topping for your pizza (Onion, Peperoni, Meat, Mushroom ,Sausage)')
        if topping1.lower() == "onion":
            print('Your topping is ', topping,'with the extra', topping1)
            Total_harga += 1000 
        if topping1.lower() == "peperoni":
            print('Your topping is', topping,'with the extra', topping1) 
            Total_harga += 1000
        if topping1.lower() == "meat":
            print('Your topping is', topping,'with the extra', topping1) 
            Total_harga += 1000
        if topping1.lower() == "mushroom":
            print('Your topping is', topping,'with the extra', topping1)
            Total_harga += 1000
        if topping1.lower() == "sausage":
            print('Your topping is', topping,'with the extra', topping1) 
            Total_harga += 1000
if Pilih_topping.lower() == "n":
    print('Your Pizza has no topping')

# Total bill the user has to pay
print('So your total bill is : Rp.',Total_harga)


