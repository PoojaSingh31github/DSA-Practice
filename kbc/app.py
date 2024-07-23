from flask import Flask, render_template, request

app = Flask(__name__)

quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for web development?",
        "choices": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "choices": ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann", "D. Bill Gates"],
        "answer": "A"
    },
    {
        "question": "Which ocean is the largest?",
        "choices": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Which continent is known as the 'Dark Continent'?",
        "choices": ["A. Asia", "B. Africa", "C. Europe", "D. South America"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the main ingredient in traditional Japanese miso soup?",
        "choices": ["A. Rice", "B. Seaweed", "C. Soybean paste", "D. Tofu"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "Which country is the largest by land area?",
        "choices": ["A. Canada", "B. China", "C. Russia", "D. United States"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["A. Gold", "B. Diamond", "C. Iron", "D. Platinum"],
        "answer": "B"
    },
    {
        "question": "Which year did the Titanic sink?",
        "choices": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"],
        "answer": "B"
    },
    {
        "question": "Which element is the most abundant in the Earth's atmosphere?",
        "choices": ["A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "What is the longest river in the world?",
        "choices": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
        "answer": "B"
    },
    {
        "question": "Which vitamin is produced when a person is exposed to sunlight?",
        "choices": ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
        "answer": "D"
    },
    {
        "question": "Who discovered penicillin?",
        "choices": ["A. Alexander Fleming", "B. Marie Curie", "C. Louis Pasteur", "D. Thomas Edison"],
        "answer": "A"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": ["A. Yen", "B. Yuan", "C. Won", "D. Baht"],
        "answer": "A"
    }
]

def run_quiz(quiz):
    score=0
    for i in quiz:
        print(i["question"])
        for j in i["choices"]:
            print(j)
        answer=input("Enter your prefferable answer A, B, C or D ").upper() 

        if answer==i["answer"]:
            print("correct anwser")
            score+=10
        else:
            print(f"Wrong! The correct answer is {i['answer']}")
        print()   

    print("your total score is", score)     

run_quiz(quiz)

@app.route('/')
def index():
    return render_template('index.html', quiz=quiz)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    results = []
    for i, item in enumerate(quiz):
        user_answer = request.form.get(f'question-{i}')
        if user_answer == item['answer']:
            score += 1
            results.append(f"Question: {item['question']} - Correct")
        else:
            results.append(f"Question: {item['question']} - Wrong (Your answer: {user_answer}, Correct answer: {item['answer']})")
    return render_template('result.html', score=score, results=results, total=len(quiz))

if __name__ == '__main__':
    app.run(debug=True)