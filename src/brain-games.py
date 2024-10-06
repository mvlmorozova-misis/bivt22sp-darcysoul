from .game.cli import welcome_user
from .game.game_lcm import play_lcm
from .game.game_progression import play_progression


def main():
    name = welcome_user()
    print("Choose game:")
    print("1 - LCM")
    print("2 - Progression.")
    choice = input("Your choice: ")

    if choice == '1':
        play_lcm(name)
    elif choice == '2':
        play_progression(name)
    else:
        print("Invalid choice. Please select either 1 or 2.")


if __name__ == '__main__':
    main()
