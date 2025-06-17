import random

# 10-question quiz bank
quiz = [
    {
        "question": "What is the output of type(3.14)?",
        "options": ["A) int", "B) float", "C) str", "D) bool"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) define", "D) function"],
        "answer": "B"
    },
    {
        "question": "What does 'Hello'[1] return?",
        "options": ["A) H", "B) e", "C) l", "D) o"],
        "answer": "B"
    },
    {
        "question": "What is the result of True and False?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
        "answer": "D"
    },
    {
        "question": "Which of these is a correct list in Python?",
        "options": ["A) (1,2,3)", "B) [1;2;3]", "C) [1,2,3]", "D) {1,2,3}"],
        "answer": "C"
    },
    {
        "question": "What does len({1,2,2,3}) return?",
        "options": ["A) 4", "B) 3", "C) 2", "D) 1"],
        "answer": "B"
    },
    {
        "question": "What is used to read a file in Python?",
        "options": ["A) 'w'", "B) 'a'", "C) 'r'", "D) 'x'"],
        "answer": "C"
    },
    {
        "question": "Which of these is not a valid variable name?",
        "options": ["A) my_var", "B) 2var", "C) var_2", "D) _var"],
        "answer": "B"
    },
    {
        "question": "How do you insert comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"
    }
]

# Shuffle questions
random.shuffle(quiz)

score = 0
print("🧠 Welcome to the Random Python Quiz!\n")

for i, q in enumerate(quiz, start=1):
    print(f"Q{i}. {q['question']}")
    for opt in q["options"]:
        print(opt)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. Correct answer is: {q['answer']}\n")

print(f"🏁 Quiz Completed! You scored {score} out of {len(quiz)}.")
