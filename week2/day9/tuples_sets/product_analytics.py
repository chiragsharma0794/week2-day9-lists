from collections import namedtuple

Product = namedtuple("Product", ["id", "name", "category", "price"])

catalog = [
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Phone", "Electronics", 45000),
    Product(3, "Headphones", "Electronics", 3000),
    Product(4, "Smartwatch", "Electronics", 12000),
    Product(5, "T-Shirt", "Clothing", 1200),
    Product(6, "Jeans", "Clothing", 2500),
    Product(7, "Jacket", "Clothing", 4500),
    Product(8, "Sneakers", "Clothing", 3500),
    Product(9, "Clean Code", "Books", 700),
    Product(10, "Python Crash Course", "Books", 950),
    Product(11, "Deep Learning", "Books", 1200),
    Product(12, "Atomic Habits", "Books", 600),
    Product(13, "Chair", "Home", 4000),
    Product(14, "Lamp", "Home", 1500),
    Product(15, "Bottle", "Home", 800),
    Product(16, "Bedsheet", "Home", 2200)
]

customer_1_cart = {catalog[0], catalog[4], catalog[8], catalog[13]}
customer_2_cart = {catalog[0], catalog[1], catalog[8], catalog[12], catalog[13]}
customer_3_cart = {catalog[0], catalog[5], catalog[8], catalog[9], catalog[13]}
customer_4_cart = {catalog[0], catalog[2], catalog[7], catalog[8], catalog[13]}
customer_5_cart = {catalog[0], catalog[3], catalog[8], catalog[10], catalog[13]}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
]

def get_bestsellers(carts):
    return set.intersection(*carts)

def get_catalog_reach(carts):
    return set.union(*carts)

def get_exclusive_purchases(customer_cart, other_carts):
    others_union = set.union(*other_carts) if other_carts else set()
    return customer_cart - others_union

def recommend_products(customer_cart, all_customer_carts):
    other_products = set()
    for cart in all_customer_carts:
        if cart != customer_cart:
            other_products |= cart
    return other_products - customer_cart

def category_summary():
    categories = {product.category for product in catalog}
    return {
        category: {product.name for product in catalog if product.category == category}
        for category in categories
    }

def show_products(products, title):
    print(f"\n{title}")
    if not products:
        print("No products found.")
        return
    for product in sorted(products, key=lambda p: p.id):
        print(f"{product.id} | {product.name} | {product.category} | ₹{product.price}")

if __name__ == "__main__":
    bestsellers = get_bestsellers(all_carts)
    catalog_reach = get_catalog_reach(all_carts)
    exclusive_customer_1 = get_exclusive_purchases(customer_1_cart, all_carts[1:])
    recommendations_for_customer_1 = recommend_products(customer_1_cart, all_carts)

    show_products(bestsellers, "Products appearing in ALL carts")
    show_products(catalog_reach, "Products appearing in ANY cart")
    show_products(exclusive_customer_1, "Products only Customer 1 bought")
    show_products(recommendations_for_customer_1, "Recommended products for Customer 1")

    print("\nCategory Summary")
    summary = category_summary()
    for category, names in summary.items():
        print(f"{category}: {names}")