from product import product_details

def test_product_details():
    expected = (
        "Product ID   : P101\n"
        "Product Name : Mobile\n"
        "Quantity     : 10\n"
        "Price        : 15000"
    )
    
    assert product_details("P101", "Mobile", 10, 15000) == expected
