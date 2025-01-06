import React, { useEffect, useState } from "react";

const QuizApp: React.FC = () => {
    const [questions, setquestions] = useState<any[]>([]);
    const [currquestion, setcurrquestion] = useState<number>(0);
    const [score, setscore] = useState<number>(0);
    const [timeleft, settimeleft] = useState<number>(15);
    const [quizover, setquizover] = useState<boolean>(false);
    const [suffledanswers, setShuffledAnswers] = useState<string[]>([]);

    const fetchQuestions = async () => {
        try {
            const response = await fetch(
                "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple"
            );
            const data = await response.json()
            setquestions(data.results);
            console.log(questions)
        } catch (error) {
            console.log("error fetching questions", error)
        }
    }
    useEffect(() => {
        fetchQuestions();
    }, []);

    useEffect(() => {
        if (questions.length > 0) {
            const currentQuestion = questions[currquestion];
            const answers = [
                ...currentQuestion.incorrect_answers, currentQuestion.correct_answer
            ].sort(() => Math.random() - 0.5);
            setShuffledAnswers(answers);
        }
    }, [questions, currquestion])

    useEffect(() => {
        if (!quizover && timeleft > 0) {
            const timer = setTimeout(() => {
                settimeleft(timeleft - 1)
            }, 1000);
            return ()=> clearTimeout(timer);
        }else if (timeleft==0) {
            handleNextQuestion();
        }
    }, [timeleft, quizover]);

    const handleAnswerClick = (isCorrect: boolean) => {
        if (isCorrect) {
            setscore(score + 1)
        }
        handleNextQuestion()
    }

    const handleNextQuestion = () => {
        if (currquestion + 1 < questions.length) {
            setcurrquestion(currquestion + 1)
            settimeleft(15)
        } else { setquizover(true) }
    }

    const restartQuiz=()=>{
        setquestions([])
        setcurrquestion(0)
        setscore(0)
        settimeleft(15)
        fetchQuestions()
    }

    if (questions.length==0){
        return <h2>Loading quiz...</h2>
    }

    if (quizover){
        return (
            <div>
                <h1>quiz over </h1>
                <h2>score : {score}/{questions.length}</h2>
                <button
                    onClick={restartQuiz}
                    style={{
                        padding: "10px 20px",
                        backgroundColor: "#007BFF",
                        color: "white",
                        border: "none",
                        borderRadius: "5px",
                        cursor: "pointer",
                    }}
                >
                    Restart Quiz
                </button>
            </div>
        )
    }

    const currQ = questions[currquestion];
    return (
        <div>
            <h1>Trivia quiz</h1>
            <div>
                <h3>question {currquestion + 1} :{currQ.question} </h3>

                {
                    suffledanswers.map((answer) => (
                        <button onClick={() => handleAnswerClick(answer === currQ.correct_answer)} style={{
                            display: "block",
                            margin: "10px auto",
                            padding: "10px 20px",
                            backgroundColor: "#f0f0f0",
                            border: "1px solid #ccc",
                            borderRadius: "5px",
                            cursor: "pointer",
                        }}>
                            {answer}
                        </button>
                    ))
                }
                <div>
                    timeleft: {timeleft}
                </div>
            </div>
        </div>
    )


}

export default QuizApp;
