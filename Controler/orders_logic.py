from Fake_DB.builder_order import BuilderOrder
from Visual.inputs import get_user_input
from Visual.menu import print_pizza_menu


def create_order():
    print_pizza_menu()

    user_choice = int(get_user_input())

    return (BuilderOrder()
            .add_choice(user_choice - 1)
            .add_choice(user_choice - 1)
            .build())


def pay():
    pass