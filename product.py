def product(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


if __name__ == "__main__":
    product_id = "P101"
    name = "Mobile"
    quantity = 5
    price = 45000

    print(product(product_id, name, quantity, price))
