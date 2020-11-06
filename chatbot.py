from determiner import give_answer

i = 0

def communicate():
    question = input("Hello\n What question about Pratyush do you want the answer to ?")
    answer = give_answer(question)
    print(answer)
    quality = None
    if i < 5000 :
        
        good_answer = input("Was my anwer valid(yes/no)?\n")
        
        if good_answer.lower() == "yes":
            quality = True
        elif good_answer.lower() == "no":
            quality = False
        
        add_to_answer(quality)