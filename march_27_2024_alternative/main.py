import os
def clear():
    os.system('clear')

import product_class

def add(product_list, p_name, u_cost, u_price, p_category):
    id = f"{len(product_list) + 1:04d}"
    product = product_class.Products(id,p_name, u_cost, u_price, p_category)  
    product_list.append(product)
    

def display(product_list):
    if len(product_list) >= 1:
        print("\n\t ** PRODUCTS ** \n")
        for p in product_list:
            print(p)


def main():
    #clear()
    product_list = []
    while True:
        p_name = input("\n Enter new product name: ")
        u_cost = input("\n Enter new unit cost: ")
        u_price = input("\n Enter new unit price : ")
        p_category = input("\n Enter new p_category: ")
        add(product_list, p_name, u_cost, u_price,p_category)
        display(product_list)

if __name__ == "__main__":
    main()