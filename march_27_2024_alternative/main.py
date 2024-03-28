import os
def clear():
    os.system('clear')

import product_class

def add(product_list, product_name, unit_cost, unit_price, category):
    id = f"{len(product_list) + 1:04d}"
    product = product_class.Products(id,product_name, unit_cost, unit_price, category)  
    product_list.append(product)
    

def display(product_list):
    if len(product_list) >= 1:
        print("\n\t ** PRODUCTS ** \n")
        for p in product_list:
            print(p)


def main():
    clear()
    product_list = []
    while True:
        product_name = input("\n Enter new product name: ")
        unit_cost = input("\n Enter new unit cost: ")
        unit_price = input("\n Enter new unit price : ")
        category = input("\n Enter new category: ")
        add(product_list, product_name, unit_cost, unit_price,category)
        display(product_list)

if __name__ == "__main__":
    main()