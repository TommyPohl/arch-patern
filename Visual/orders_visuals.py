from Visual.messages import print_message


def print_cart(order):
    if order is None:
        print_message("prazdny kosik")
        return

    print("Tvuj kosik")
    for i, item in enumerate(order.items):
        print(f"polozka {i + 1}")
        print(f"{item.name} -     {item.price}")