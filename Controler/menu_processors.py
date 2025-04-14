from .orders_logic import create_order, pay
from Visual.messages import print_message
from Visual.orders_visuals import print_cart


def process_main_menu_choice(user_choice, order):
    if user_choice == "1":
        new_order = create_order()
        return new_order

    elif user_choice == "2":
        print_cart(order)

    elif user_choice == "3":
        pay()

    elif user_choice == "0":
        return None

    else:
        print_message("zadal si spatnou volbu")

    return 1