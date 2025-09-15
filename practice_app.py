# practice_app.py

def practice_typing(word_list, attempts=100):
    correct_count = 0
    total_attempts = attempts

    for i in range(total_attempts):
        user_input = input(f"Enter '{word_list[i]}' or press Enter to try again: ")
        if user_input.lower() == word_list[i].lower():
            correct_count += 1
        else:
            print(f"Incorrect. The correct word is '{word_list[i]}'. Try again.")

    print(f"\nYou were successful! You typed correctly {correct_count}/{total_attempts} times.")
    return correct_count

def main():
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    attempts = practice_typing(word_list)
    
    # Optional: Add a loop to keep practicing
    while True:
        user_input = input("Would you like to practice again? (yes/no): ")
        if user_input.lower() == 'no':
            print("Thanks for practicing!")
            break
        attempts = practice_typing(word_list, attempts=attempts)

if __name__ == "__main__":
    main()

