Questions={
    "1. Who was the first President of India?":'b',
    "2. What is the capital of Australia?":'d',
    "3. Which is the largest planet in our solar system?":'c',
    "4. Who wrote the national anthem of India?":'b',
    "5. Which gas do plants absorb from the atmosphere?":'c',
    "6. What is the currency of Japan?":'a',
    "7. How many players are there in a cricket team?":'c',
    "8. Which planet is known as the \"Red Planet\"?":'c',
    "9. Who invented the light bulb?":'d',
    "10. Which river is the longest in the world?":'b'
}

options = [
    ["A) Jawaharlal Nehru", "B) Rajendra Prasad", "C) Sardar Patel", "D) B.R. Ambedkar"],
    ["A) Sydney", "B) Melbourne", "C) Perth", "D) Canberra"],
    ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
    ["A) Bankim Chandra Chatterjee", "B) Rabindranath Tagore", "C) Subhash Chandra Bose", "D) Mahatma Gandhi"],
    ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
    ["A) Yen", "B) Dollar", "C) Rupee", "D) Euro"],
    ["A) 9", "B) 10", "C) 11", "D) 12"],
    ["A) Mercury", "B) Venus", "C) Mars", "D) Jupiter"],
    ["A) Alexander Graham Bell", "B) Isaac Newton", "C) Albert Einstein", "D) Thomas Edison"],
    ["A) Amazon", "B) Nile", "C) Ganga", "D) Mississippi"]
]
question_no=0
score=0
ask=input("You want to play (Y/N)?\n").lower()
if ask!="y":
    quit()
else:
    print("let's Play".center(20,'*'))

    for quetion,ans in Questions.items() :
        print('\n')
        print(quetion)
        for option in options[question_no]:
            print(option)
        
        Answer=input("Answer(a/b/c/d) : ").lower()

        if ans==Answer:
            score+=4
            print("Correct ✅")
            print(f"Answer is {ans}")
        else:
            score-=1
            print("Wrong ❌")
            print(f"Answer is {ans}")
        question_no+=1
print(f"\nTotal score = {score}/40")