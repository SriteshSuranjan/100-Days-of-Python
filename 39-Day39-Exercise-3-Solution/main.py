print("=" * 80)
print("★ ★ ★  K A U N   B A N E G A   C R O R E P A T I  ★ ★ ★".center(80))
print("-" * 80)
print("A N S W E R   T H E   Q U E S T I O N S   &   W I N   B I G !".center(80))
print("=" * 80)


questions = [
    ["Which programming language is widely used for Data Science and Artificial Intelligence?", "Java", "Python", "C++", "PHP", "None", 2],

    ["Which country won the ICC Men's Cricket World Cup in 2023?", "India", "Australia", "England", "New Zealand", "None", 2],

    ["Who played the character of Harry Potter in the Harry Potter film series?", "Rupert Grint", "Daniel Radcliffe", "Tom Felton", "Robert Pattinson", "None", 2],

    ["Which is the largest continent in the world by area?", "Africa", "Europe", "Asia", "North America", "None", 3],

    ["Which organ in the human body produces insulin?", "Heart", "Liver", "Pancreas", "Kidney", "None", 3],

    ["Which car manufacturer produces the Mustang?", "Chevrolet", "Ford", "Dodge", "Toyota", "None", 2],

    ["Who played Iron Man in the Marvel Cinematic Universe?", "Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo", "None", 3],

    ["In football, how many players from one team are normally on the field at the start of a match?", "9", "10", "11", "12", "None", 3],

    ["Which Bollywood film won the Academy Award for Best Original Song for 'Naatu Naatu'?", "RRR", "Dangal", "Lagaan", "Pushpa", "None", 1],

    ["In the Fast & Furious film series, what is the name of Dominic Toretto's sister?", "Letty", "Mia", "Elena", "Ramsey", "None", 2],

    ["Which fundamental right in the Indian Constitution is known as the 'Right to Equality'?", "Article 14", "Article 19", "Article 21", "Article 32", "None", 1],

    ["What is the SI unit of electric resistance?", "Volt", "Watt", "Ohm", "Ampere", "None", 3],

    ["Which Indian classical musician was famous for playing the shehnai and was awarded the Bharat Ratna?", "Ravi Shankar", "Bismillah Khan", "Zakir Hussain", "Hariprasad Chaurasia", "None", 2],

    ["Which Indian space mission successfully landed near the Moon's south polar region in 2023?", "Mangalyaan", "Chandrayaan-2", "Chandrayaan-3", "Aditya-L1", "None", 3],

    ["Which company manufactures the luxury sports car model 911?", "Ferrari", "Porsche", "Lamborghini", "McLaren", "None", 2],

    ["Which actor portrayed Captain Jack Sparrow in the Pirates of the Caribbean film series?", "Leonardo DiCaprio", "Johnny Depp", "Brad Pitt", "Tom Cruise", "None", 2],

    ["Which treaty formally ended World War I?", "Treaty of Paris", "Treaty of Versailles", "Treaty of Vienna", "Treaty of Rome", "None", 2]
]

levels = [5000, 10000, 15000, 20000, 25000, 50000, 100000, 200000, 300000, 500000, 750000, 1250000, 2500000, 5000000, 10000000, 70000000, 75000000]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"A. {question[1]}           B. {question[2]}")
    print(f"C. {question[3]}           D. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    money = 0
    # Quit
    if reply == 0:
        if i < 5:
            money = 0
        elif i < 10:
            money = 20000
        elif i < 15:
            money = 300000
        else:
            money = 5000000

        print("You decided to quit the game.")
        break
    
    # Correct Answer
     # Correct answer
    elif reply == question[-1]:

        print(f"Correct Answer! You have won Rs. {levels[i]}")

        # Safe/base levels
        if i < 5:
            money = 0
        elif i < 10:
            money = 20000
        elif i < 15:
            money = 300000
        elif i < 16:
            money = 5000000
        else:
            money = 75000000
    
    # Wrong Answer
    else:
        print("Wrong Answer!")

        # Player takes the safe/base amount
        if i < 5:
            money = 0
        elif i < 10:
            money = 20000
        elif i < 15:
            money = 300000
        else:
            money = 5000000

        break

print("=" * 80)
print("★ ★ ★  C O N G R A T U L A T I O N S !  ★ ★ ★".center(80))
print("-" * 80)
print(f"You have won Rs. {money}".center(80))
print("T H A N K   Y O U   F O R   P L A Y I N G !".center(80))
print("=" * 80)
