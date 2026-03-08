import timeit

# What is frozenset?
# A frozenset is an immutable version of a set in Python.
# Difference between set and frozenset:
# set is mutable, so you can add or remove elements.
# frozenset is immutable, so once created, it cannot be changed.
# Real-world use:
# frozenset is useful when you want a hashable group of unique items,
# such as using category combinations as dictionary keys in pricing,
# permissions, caching, or rule engines.

bundle_discounts = {
    frozenset({"Electronics", "Books"}): 10,
    frozenset({"Clothing", "Home"}): 15,
    frozenset({"Electronics", "Home"}): 12
}

def check_bundle_discount(cart):
    cart_categories = {product.category for product in cart}
    applicable_discounts = []

    for bundle_categories, discount in bundle_discounts.items():
        if bundle_categories.issubset(cart_categories):
            applicable_discounts.append((bundle_categories, discount))

    return applicable_discounts

def benchmark_set_vs_frozenset():
    set_time = timeit.timeit("set(['Electronics', 'Books'])", number=100000)
    frozenset_time = timeit.timeit("frozenset(['Electronics', 'Books'])", number=100000)

    print("\nPerformance Benchmark for 100000 iterations")
    print(f"set creation time: {set_time:.6f} seconds")
    print(f"frozenset creation time: {frozenset_time:.6f} seconds")

    # Observation:
    # Both are fast.
    # set creation is often slightly faster or very close.
    # frozenset is preferred when immutability and hashability matter more than tiny creation differences.

if __name__ == "__main__":
    from product_analytics import customer_1_cart, customer_2_cart

    print("Bundle discounts for Customer 1 cart:")
    print(check_bundle_discount(customer_1_cart))

    print("\nBundle discounts for Customer 2 cart:")
    print(check_bundle_discount(customer_2_cart))

    benchmark_set_vs_frozenset()