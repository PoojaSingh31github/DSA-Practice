def love_calculator(name1, name2):
    add_names = name1 + name2
    add_names = add_names.lower()
    
    true_count = sum(add_names.count(char) for char in "true")
    print(true_count)
    love_count = sum(add_names.count(char) for char in "love")
    print(love_count)
    score = int(str(true_count) + str(love_count))
    print(score)
    
    if score > 90 or score < 10:
        result = f"Your score is {score}, you go together like coke and mentos."
    elif 40 <= score <= 50:
        result = f"Your score is {score}, you are alright together."
    else:
        result = f"Your score is {score}."
    
    return result

# Example usage:
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
print(love_calculator(name1, name2))


