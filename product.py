def product_details(name, prod_id, quantity, price):
    result = (
       f"Product Name   : {name}\n"
        f"Product ID     : {prod_id}\n"
        f"Quantity      : {quantity}\n"  
        f"Price          : {price}"
    )
    return result
if _name_ == "_main_":
    name="Laptop"
    prod_id="F1007"
    quantity=1
    price=95000
    print(product_details(name, prod_id, quantity, price))
