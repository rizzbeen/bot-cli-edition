import time
from modules.function import slowtype, red, green, yellow, blue, magenta, cyan, white, black

def run_quiz():
    question_count = 0
    quiz_list = [
    {
        "question": "Q1 [GEOGRAPHY] - What is the capital of France?",
        "options": ["A) Paris", "B) Madrid", "C) Rome", "D) Berlin"],
        "answer": "A) Paris"
    },
    {
        "question": "Q2 [SCIENCE] - Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C) Mars"
    },
    {
        "question": "Q3 [TECH] - What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Central Processing Unit", "C) Control Process Unit", "D) Computer Power Unit"],
        "answer": "B) Central Processing Unit"
    },
    {
        "question": "Q4 [HISTORY] - Who was the first President of the United States?",
        "options": ["A) George Washington", "B) Abraham Lincoln", "C) John Adams", "D) Thomas Jefferson"],
        "answer": "A) George Washington"
    },
    {
        "question": "Q5 [MATH] - What is the square root of 64?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C) 8"
    },
    {
        "question": "Q6 [LITERATURE] - Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
        "answer": "B) William Shakespeare"
    },
    {
        "question": "Q7 [GENERAL] - What color is the 'G' in Google logo?",
        "options": ["A) Blue", "B) Red", "C) Green", "D) Yellow"],
        "answer": "A) Blue"
    },
    {
        "question": "Q8 [SCIENCE] - What is H2O commonly known as?",
        "options": ["A) Salt", "B) Water", "C) Oxygen", "D) Hydrogen"],
        "answer": "B) Water"
    },
    {
        "question": "Q9 [GEOGRAPHY] - Which is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "answer": "C) Pacific"
    },
    {
        "question": "Q10 [MATH] - What is 15 * 6?",
        "options": ["A) 85", "B) 90", "C) 95", "D) 100"],
        "answer": "B) 90"
    },

    {
        "question": "Q11 [HISTORY] - In which year did World War II end?",
        "options": ["A) 1940", "B) 1943", "C) 1945", "D) 1947"],
        "answer": "C) 1945"
    },
    {
        "question": "Q12 [TECH] - What is the name of the first electronic computer?",
        "options": ["A) UNIVAC", "B) ENIAC", "C) IBM-1", "D) Altair"],
        "answer": "B) ENIAC"
    },
    {
        "question": "Q13 [SCIENCE] - Which gas do plants absorb?",
        "options": ["A) Nitrogen", "B) Carbon Dioxide", "C) Oxygen", "D) Hydrogen"],
        "answer": "B) Carbon Dioxide"
    },
    {
        "question": "Q14 [MATH] - What is the value of π (up to 2 decimal points)?",
        "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
        "answer": "B) 3.14"
    },
    {
        "question": "Q15 [TECH] - Which company created the iPhone?",
        "options": ["A) Microsoft", "B) Apple", "C) Google", "D) Samsung"],
        "answer": "B) Apple"
    },
    {
        "question": "Q16 [LITERATURE] - What is the name of Sherlock Holmes' assistant?",
        "options": ["A) Watson", "B) Hudson", "C) Doyle", "D) Lestrade"],
        "answer": "A) Watson"
    },
    {
        "question": "Q17 [GEOGRAPHY] - Which continent is known as the 'Dark Continent'?",
        "options": ["A) Asia", "B) Australia", "C) Africa", "D) South America"],
        "answer": "C) Africa"
    },
    {
        "question": "Q18 [GENERAL] - What is the currency of Japan?",
        "options": ["A) Yuan", "B) Yen", "C) Won", "D) Ringgit"],
        "answer": "B) Yen"
    },
    {
        "question": "Q19 [SCIENCE] - What part of the cell contains DNA?",
        "options": ["A) Cytoplasm", "B) Membrane", "C) Nucleus", "D) Ribosome"],
        "answer": "C) Nucleus"
    },
    {
        "question": "Q20 [TECH] - What does HTML stand for?",
        "options": ["A) HighText Machine Language", "B) HyperText and links Markup Language", "C) HyperText Markup Language", "D) None"],
        "answer": "C) HyperText Markup Language"
    },

    {
        "question": "Q21 [MATH] - What is 12 squared?",
        "options": ["A) 124", "B) 144", "C) 122", "D) 112"],
        "answer": "B) 144"
    },
    {
        "question": "Q22 [HISTORY] - Who discovered America?",
        "options": ["A) Vasco da Gama", "B) Christopher Columbus", "C) Ferdinand Magellan", "D) Marco Polo"],
        "answer": "B) Christopher Columbus"
    },
    {
        "question": "Q23 [SCIENCE] - Which vitamin is obtained from sunlight?",
        "options": ["A) Vitamin A", "B) Vitamin B", "C) Vitamin C", "D) Vitamin D"],
        "answer": "D) Vitamin D"
    },
    {
        "question": "Q24 [GENERAL] - How many continents are there?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C) 7"
    },
    {
        "question": "Q25 [TECH] - Who founded Microsoft?",
        "options": ["A) Steve Jobs", "B) Bill Gates", "C) Elon Musk", "D) Mark Zuckerberg"],
        "answer": "B) Bill Gates"
    },
    {
        "question": "Q26 [LITERATURE] - What is the famous opening line of 'A Tale of Two Cities'?",
        "options": ["A) It was the worst of times", "B) It was a dark and stormy night", "C) It was the best of times, it was the worst of times", "D) Call me Ishmael"],
        "answer": "C) It was the best of times, it was the worst of times"
    },
    {
        "question": "Q27 [SCIENCE] - What is the boiling point of water in Celsius?",
        "options": ["A) 50°C", "B) 90°C", "C) 100°C", "D) 120°C"],
        "answer": "C) 100°C"
    },
    {
        "question": "Q28 [GEOGRAPHY] - What is the smallest country in the world?",
        "options": ["A) Monaco", "B) San Marino", "C) Vatican City", "D) Malta"],
        "answer": "C) Vatican City"
    },
    {
        "question": "Q29 [GENERAL] - How many players are there in a soccer team (on field)?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 9"],
        "answer": "B) 11"
    },
    {
        "question": "Q30 [TECH] - What is the shortcut for 'copy' on most computers?",
        "options": ["A) Ctrl + C", "B) Ctrl + V", "C) Ctrl + X", "D) Ctrl + Z"],
        "answer": "A) Ctrl + C"
    },

    {
        "question": "Q31 [HISTORY] - Who wrote the Indian national anthem?",
        "options": ["A) Rabindranath Tagore", "B) Bankim Chandra", "C) Subhash Chandra Bose", "D) M.K. Gandhi"],
        "answer": "A) Rabindranath Tagore"
    },
    {
        "question": "Q32 [SCIENCE] - What is the chemical symbol for gold?",
        "options": ["A) Gd", "B) Au", "C) Ag", "D) Go"],
        "answer": "B) Au"
    },
    {
        "question": "Q33 [MATH] - What is the derivative of x²?",
        "options": ["A) 2x", "B) x", "C) x²", "D) 2"],
        "answer": "A) 2x"
    },
    {
        "question": "Q34 [LITERATURE] - Who is the author of '1984'?",
        "options": ["A) George Orwell", "B) Aldous Huxley", "C) J.K. Rowling", "D) Ray Bradbury"],
        "answer": "A) George Orwell"
    },
    {
        "question": "Q35 [TECH] - What is the name of Google's parent company?",
        "options": ["A) Google Inc.", "B) Alphabet Inc.", "C) Meta", "D) Pixel"],
        "answer": "B) Alphabet Inc."
    },
    {
        "question": "Q36 [GEOGRAPHY] - Mount Everest lies on the border of which two countries?",
        "options": ["A) India and Nepal", "B) Nepal and China", "C) India and Bhutan", "D) China and Bhutan"],
        "answer": "B) Nepal and China"
    },
    {
        "question": "Q37 [GENERAL] - Which day comes after Christmas?",
        "options": ["A) Boxing Day", "B) New Year's Eve", "C) Thanksgiving", "D) Good Friday"],
        "answer": "A) Boxing Day"
    },
    {
        "question": "Q38 [SCIENCE] - What does DNA stand for?",
        "options": ["A) Digital Network Architecture", "B) Deoxyribonucleic Acid", "C) Data Numeric Analysis", "D) Dynamic Natural Array"],
        "answer": "B) Deoxyribonucleic Acid"
    },
    {
        "question": "Q39 [TECH] - What programming language is used for iOS app development?",
        "options": ["A) Python", "B) Kotlin", "C) Swift", "D) Java"],
        "answer": "C) Swift"
    },
    {
        "question": "Q40 [MATH] - What is 7 factorial (7!)?",
        "options": ["A) 5040", "B) 720", "C) 2400", "D) 840"],
        "answer": "A) 5040"
    },

    {
        "question": "Q41 [HISTORY] - What wall fell in 1989 symbolizing the end of the Cold War?",
        "options": ["A) China Wall", "B) Berlin Wall", "C) Vietnam Wall", "D) Kremlin"],
        "answer": "B) Berlin Wall"
    },
    {
        "question": "Q42 [SCIENCE] - What is Newton's Third Law?",
        "options": ["A) Gravity pulls", "B) Every action has an equal and opposite reaction", "C) Force = mass × acceleration", "D) Energy = mc²"],
        "answer": "B) Every action has an equal and opposite reaction"
    },
    {
        "question": "Q43 [GEOGRAPHY] - Which river is the longest in the world?",
        "options": ["A) Nile", "B) Amazon", "C) Mississippi", "D) Yangtze"],
        "answer": "A) Nile"
    },
    {
        "question": "Q44 [TECH] - What does URL stand for?",
        "options": ["A) Uniform Resource Locator", "B) Universal Remote Link", "C) User Reference Log", "D) United Runtime Library"],
        "answer": "A) Uniform Resource Locator"
    },
    {
        "question": "Q45 [GENERAL] - What is the primary ingredient in guacamole?",
        "options": ["A) Tomato", "B) Avocado", "C) Cucumber", "D) Lime"],
        "answer": "B) Avocado"
    },
    {
        "question": "Q46 [MATH] - What’s the next prime number after 7?",
        "options": ["A) 9", "B) 10", "C) 11", "D) 13"],
        "answer": "C) 11"
    },
    {
        "question": "Q47 [SCIENCE] - What is the process of turning gas into liquid?",
        "options": ["A) Evaporation", "B) Condensation", "C) Sublimation", "D) Freezing"],
        "answer": "B) Condensation"
    },
    {
        "question": "Q48 [TECH] - What company created ChatGPT?",
        "options": ["A) Meta", "B) Microsoft", "C) Google", "D) OpenAI"],
        "answer": "D) OpenAI"
    },
    {
        "question": "Q49 [GEOGRAPHY] - Which country has the most time zones?",
        "options": ["A) Russia", "B) USA", "C) China", "D) France"],
        "answer": "D) France"
    },
    {
        "question": "Q50 [MATH] - What is the value of log(100)?",
        "options": ["A) 10", "B) 1", "C) 100", "D) 2"],
        "answer": "D) 2"
    },

    # 51–60: Intermediate World Knowledge
    {
        "question": "Which African country has the most pyramids?",
        "options": ["A) Egypt", "B) Sudan", "C) Ethiopia", "D) Libya"],
        "answer": "B) Sudan"
    },
    {
        "question": "Which Indian physicist won the Nobel Prize in 1930?",
        "options": ["A) C.V. Raman", "B) Satyendra Nath Bose", "C) Homi Bhabha", "D) A.P.J Abdul Kalam"],
        "answer": "A) C.V. Raman"
    },
    {
        "question": "Which U.S. president was in office during the Great Depression and WWII?",
        "options": ["A) Harry Truman", "B) Woodrow Wilson", "C) Franklin D. Roosevelt", "D) Theodore Roosevelt"],
        "answer": "C) Franklin D. Roosevelt"
    },
    {
        "question": "Which element has the highest melting point?",
        "options": ["A) Iron", "B) Tungsten", "C) Carbon", "D) Titanium"],
        "answer": "B) Tungsten"
    },
    {
        "question": "Which is the longest bone in the human body?",
        "options": ["A) Femur", "B) Humerus", "C) Tibia", "D) Fibula"],
        "answer": "A) Femur"
    },
    {
        "question": "Who painted 'The Persistence of Memory'?",
        "options": ["A) Salvador Dalí", "B) Pablo Picasso", "C) Claude Monet", "D) Vincent van Gogh"],
        "answer": "A) Salvador Dalí"
    },
    {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["A) Spanish", "B) Mandarin", "C) English", "D) Hindi"],
        "answer": "B) Mandarin"
    },
    {
        "question": "What is the capital city of Kazakhstan?",
        "options": ["A) Astana", "B) Almaty", "C) Tashkent", "D) Bishkek"],
        "answer": "A) Astana"
    },
    {
        "question": "In music, what does 'allegro' mean?",
        "options": ["A) Very slow", "B) Moderate pace", "C) Fast", "D) Loud"],
        "answer": "C) Fast"
    },
    {
        "question": "What year did the Berlin Wall fall?",
        "options": ["A) 1987", "B) 1989", "C) 1991", "D) 1993"],
        "answer": "B) 1989"
    },

    # 61–70: Coding & Tech
    {
        "question": "What does the acronym 'RAM' stand for?",
        "options": ["A) Read Access Memory", "B) Random Access Memory", "C) Ready Access Mode", "D) Run All Memory"],
        "answer": "B) Random Access Memory"
    },
    {
        "question": "Which language is primarily used for data science and AI?",
        "options": ["A) C", "B) Python", "C) Java", "D) Ruby"],
        "answer": "B) Python"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["A) HyperText Transfer Protocol", "B) High Transfer Text Protocol", "C) HyperText Translation Protocol", "D) Host Transfer Text Protocol"],
        "answer": "A) HyperText Transfer Protocol"
    },
    {
        "question": "Which company created the Linux kernel?",
        "options": ["A) IBM", "B) Linus Torvalds", "C) Google", "D) Apple"],
        "answer": "B) Linus Torvalds"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["A) O(n)", "B) O(log n)", "C) O(n log n)", "D) O(1)"],
        "answer": "B) O(log n)"
    },
    {
        "question": "Which HTML tag is used to define an internal style sheet?",
        "options": ["A) <script>", "B) <css>", "C) <style>", "D) <link>"],
        "answer": "C) <style>"
    },
    {
        "question": "Which Python library is used for data manipulation and analysis?",
        "options": ["A) NumPy", "B) TensorFlow", "C) Pandas", "D) Matplotlib"],
        "answer": "C) Pandas"
    },
    {
        "question": "What is Git primarily used for?",
        "options": ["A) Designing websites", "B) Managing databases", "C) Version control", "D) Machine learning"],
        "answer": "C) Version control"
    },
    {
        "question": "Which programming paradigm does Python support?",
        "options": ["A) Object-oriented", "B) Functional", "C) Procedural", "D) All of the above"],
        "answer": "D) All of the above"
    },
    {
        "question": "Which port does HTTP use by default?",
        "options": ["A) 21", "B) 443", "C) 80", "D) 25"],
        "answer": "C) 80"
    },

    # 71–80: Advanced Concepts and Logic
    {
        "question": "What is Schrödinger's cat a paradox of?",
        "options": ["A) Quantum mechanics", "B) Evolution", "C) Relativity", "D) Thermodynamics"],
        "answer": "A) Quantum mechanics"
    },
    {
        "question": "What is the derivative of sin(x)?",
        "options": ["A) cos(x)", "B) -cos(x)", "C) -sin(x)", "D) tan(x)"],
        "answer": "A) cos(x)"
    },
    {
        "question": "What does a VPN do?",
        "options": ["A) Improves WiFi", "B) Blocks spam", "C) Encrypts internet traffic", "D) Increases RAM"],
        "answer": "C) Encrypts internet traffic"
    },
    {
        "question": "What does ‘NaN’ stand for in programming?",
        "options": ["A) Not a Network", "B) Not a Name", "C) Not a Number", "D) Null and None"],
        "answer": "C) Not a Number"
    },
    {
        "question": "Which of these sorting algorithms has the best average case time complexity?",
        "options": ["A) Bubble Sort", "B) Merge Sort", "C) Selection Sort", "D) Insertion Sort"],
        "answer": "B) Merge Sort"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C) 2"
    },
    {
        "question": "What unit is used to measure the frequency of waves?",
        "options": ["A) Joules", "B) Hertz", "C) Pascal", "D) Volt"],
        "answer": "B) Hertz"
    },
    {
        "question": "Which gas is most abundant in Earth’s atmosphere?",
        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
        "answer": "C) Nitrogen"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["A) Structured Query Language", "B) Simple Query Logic", "C) System Queue Language", "D) Structured Queue List"],
        "answer": "A) Structured Query Language"
    },
    {
        "question": "In binary, what does 1010 represent in decimal?",
        "options": ["A) 10", "B) 12", "C) 15", "D) 8"],
        "answer": "A) 10"
    },

    # 81–100: Advanced Trivia & Philosophy
    {
        "question": "Which philosopher wrote 'Critique of Pure Reason'?",
        "options": ["A) Immanuel Kant", "B) Plato", "C) Nietzsche", "D) Socrates"],
        "answer": "A) Immanuel Kant"
    },
    {
        "question": "What’s the maximum number of electrons in the second shell of an atom?",
        "options": ["A) 2", "B) 4", "C) 8", "D) 16"],
        "answer": "C) 8"
    },
    {
        "question": "Which blood type is known as the universal donor?",
        "options": ["A) A", "B) O-", "C) AB+", "D) B"],
        "answer": "B) O-"
    },
    {
        "question": "Which is the most stable configuration of carbon?",
        "options": ["A) Graphene", "B) Diamond", "C) Carbon nanotube", "D) Fullerene"],
        "answer": "B) Diamond"
    },
    {
        "question": "What is the Heisenberg Uncertainty Principle about?",
        "options": ["A) Gravity", "B) Electricity", "C) Position and momentum", "D) Entropy"],
        "answer": "C) Position and momentum"
    },
    {
        "question": "What is the sum of angles in a pentagon?",
        "options": ["A) 540°", "B) 360°", "C) 720°", "D) 600°"],
        "answer": "A) 540°"
    },
    {
        "question": "What year did man first step on the Moon?",
        "options": ["A) 1965", "B) 1969", "C) 1972", "D) 1970"],
        "answer": "B) 1969"
    },
    {
        "question": "What’s the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Gd", "D) Go"],
        "answer": "A) Au"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "answer": "B) 12"
    },
    {
        "question": "Which country hosted the 2022 FIFA World Cup?",
        "options": ["A) Brazil", "B) Qatar", "C) Russia", "D) France"],
        "answer": "B) Qatar"
    }
]   
    green_text = green("QUIZ SIMULATOR-- CLI EDITION")
    text = "\nQUIZ SIMULATOR-- CLI EDITION"
    width = 35
    spaces = width-len(text) // 2
    print(f"{' '*spaces}{green_text}")
    print(f"{' '* 12}{"═" * 46}")
    answer_count = 0
    for question in quiz_list:
      q_text = green("QUESTION")
      print(f"\n\n{q_text}: {question["question"]}")
      question_count +=1
      print(red("\nOPTION:\n"))
      for option in question["options"]:
        print(f' {option}')
      guess_count = 2
      correct_answer = question["answer"][0]
      try:
        while guess_count > 0:
         choice = input(f'\n➡️    {black("Enter your choice:\t")}').strip().upper()
         time.sleep(1)
         if choice in ["EXIT", "QUIT", "BYE","BYEE", "OFF", "EXITT"]:
           print(f"\n✅ Congratulations. You got {answer_count}/{question_count - 1} correct")
           exit()
         if choice.isdigit() or choice not in ["A", "B", "C", "D"]:
            print(f'\n🚫  {red("PLEASE ENTER BEETWEEN A-D")}')
            continue
         if choice == correct_answer:
           text_congo = green("✅  CONGRATULATIONS. IT WAS CORRECT")
           slowtype(f'\n\n{text_congo}', 0.021)
           answer_count += 1
           break
         if choice != correct_answer: 
           guess_count -= 1
           if guess_count == 1:
            print("\n❌", end="  ")
            slowtype(red('INCORRECT. THIS IS YOUR LAST CHANCE'), 0.022)
           elif guess_count == 0:
            print(f"\n🚫  ALL ATTEMPTS FAILED. THE CORRECT ANSWER WAS {question['answer']}")
      except Exception:
         print("\n😓  SOMETHING WENT WRONG, PLEASE TRY AGAIN LATER")     

    print(f'\n🎉  Conratulations...You got {answer_count}/{question_count} correct ')
               
    
   

 



