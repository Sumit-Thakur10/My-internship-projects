# Creating class 'Question' to represent each question.....
class Question:
    # init method is used for initializing objects created..
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    # ask method is defined to present the ques. to user nd handle user input
    def ask(self):
        print(self.question)
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")
        
        while True: # for infinite loop until it encounters a 'break' statement
            user_input = input("Enter your answer (1, 2, 3, ... or the option itself): ").strip().lower() #strip is for removing whitespaces or newline char etc and lower is to convert character in a string to lowercase...
            
            if user_input.isdigit(): #condition : to only  execute when user inputs 1/2/3
                user_choice = int(user_input)
                if 1 <= user_choice <= len(self.options):
                    if self.options[user_choice - 1].lower() == self.correct_answer.lower():
                        print("Correct!")
                        return True
                    else:
                        print(f"Incorrect! The correct answer is: {self.correct_answer}")
                        return False
                else:
                    print("Invalid input. Please enter a valid option number.")
            elif user_input in self.options:
                if user_input.lower() == self.correct_answer.lower():
                    print("Correct!")
                    return True
                else:
                    print(f"Incorrect! The correct answer is: {self.correct_answer}")
                    return False
            else:
                print("Invalid input. Please enter a valid option or its number.")   #for wrong input
# pplay_quiz function is responsible for managing the flow..
def play_quiz(questions):
    score = 0 #scorevariable is initialized to keep track of the user's score
    total_questions = len(questions) # total number of ques = length of ques.. 
    
    for i, question in enumerate(questions, 1):  
        print(f"Question {i}/{total_questions}:")
        if question.ask():
            score += 1      # add +1 to the score when answer is correct!
        print(f"Your current score: {score}/{i}\n")
    
    print(f"Final score: {score}/{total_questions}")

if __name__ == "__main__":
    questions = [
        Question("What is the capital of India?", ["New Delhi", "Madhya Pradesh", "Karnataka"], "New Delhi"),
        Question("What technology is used to record cryptocurrency transactions?", ["Digital wallet", "Blockchain", "Mine"], "Blockchain"),
        Question("Who is the CEO of MICROSOFT?", ["Satya Nadella", "Sunder Pichai", "Tim Cook"], "Satya Nadella"),
        Question('Which country has the largest population?',['India','China','Russia'], 'India'),
        Question('Who is the current PM of INDIA?',['Narendra Modi','Rahul Gandhi','Arvind Kejriwal'],'Narendra Modi'),
        Question('Which country won the U19-cricket World Cup 2024',['India','England','Australia'],'Australia'),
        Question('Who invented javaScript?',['Guido van Rossum','Brendon Eich','James Gosling'],'Brendon Eich'),
        Question('Which sports person has the most followers on instagram? ',['Kohli','Ronaldo','Messi'],'Ronaldo'),
    ]
    
    play_quiz(questions) # play_quiz function is called.. with quiz questions as argument
