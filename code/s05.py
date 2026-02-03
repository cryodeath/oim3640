# a product would close $100, how much tax do we pay? 

# product = 100 # in dollars
# tax_rate = 0.0625
# tax = product * tax_rate
# print (f'The tax for the product which costs ${product} is ${tax}. ')


def calc_tax(price, tax_rate): 
    '''Calculate product tax based on given price and return the tax amount'''
    product = 100 # in dollars
    tax_rate = 0.0625
    tax = price * tax_rate
    # print (f'The tax for the product which costs ${price} is ${tax}. ')
    # print (tax)
    return tax

computer_price = float(input('Enter the product price:'))
iphone_price = 1100
mass_rate = 0.0625 
ny_rate = 0.075 / 100
tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone =calc_tax(iphone_price, ny_rate)

total_tax = tax_computer + tax_iphone 
print(total_tax)

# calc_tax(100)
# calc_tax(20)

