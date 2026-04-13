"""
Aegis Wireless Toolkit – main entry point.

Run this file directly to start the interactive menu::

    python app.py

Select a mode from the main menu:
    1. Easy Mode     – single-step guided audit (recommended for beginners)
    2. Guided Mode   – step-by-step walkthrough with explanations
    3. Advanced Mode – full access to all toolkit features
    4. Exit
"""

from modes.easy_mode import run_easy_mode
from modes.guided_mode import run_guided_mode
from modes.advanced_mode import run_advanced_mode


def pause():
    input("\nPress Enter to continue...")


def show_main_menu():
    print("\n================================")
    print("        AEGIS TOOLKIT")
    print("================================")
    print("1. Easy Mode (Recommended)")
    print("2. Guided Mode")
    print("3. Advanced Mode")
    print("4. Exit")


def main():
    while True:
        show_main_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            run_easy_mode()
            pause()
        elif choice == "2":
            run_guided_mode()
            pause()
        elif choice == "3":
            run_advanced_mode()
            pause()
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid choice.")
            pause()


if __name__ == "__main__":
    main()