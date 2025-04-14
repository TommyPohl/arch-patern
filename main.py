from Visual.menu import print_main_menu
from Visual.inputs import get_user_input
from Visual.messages import print_exit_app


def run():
    while True:
        print_main_menu()
        user_choice = get_user_input()

        if process_main_menu_choice(user_choice) is None:
            break

    print_exit_app()

if __name__ == "__main__":
    run()

