print("Welcome to the Love Calculator!")

name1 = input("Input the first name: ")
name2 = input("Input the second name: ")
combined_name = (name1 + name2).lower()

first_digit = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
second_digit = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")
love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}%, you go together like coca cola and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}%, you are mid together.")
elif love_score == 69:
    print(f"Your love score is {love_score}%, you are like ying and yang.")    
else:
    print(f"Your love score is {love_score}%, you are like bonnie and clyde.")
