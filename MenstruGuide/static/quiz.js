const quizData = [
    // 1
    {
        question: "What is the average length of a menstrual cycle in days ?",
        a: "21-24 days",
        b: "25-30 days",
        c: "31-35 days",
        d: "36-40 days",
        correct: "a",
    },
    // 2
    {
        question: "What is the main hormone responsible for regulating the menstrual cycle ?",
        a: "Progesterone",
        b: "Testosterone",
        c: "Follicle-stimulating hormone (FSH)",
        d: "Luteinizing hormone (LH)",
        correct: "a",
    },
    // 3
    {
        question: "What is the most common cause of heavy menstrual bleeding ?",
        a: "Polycystic ovary syndrome (PCOS)",
        b: "Endometriosis",
        c: "Uterine fibroids",
        d: "Thyroid problems",
        correct: "c",
    },
    // 4
    {
        question: "What is the medical term for a missed period ?",
        a: "Amenorrhea",
        b: "Menorrhagia",
        c: "Dysmenorrhea",
        d: "Metrorrhagia",
        correct: "a",
    },
    // 5
    {
        question: "What is the recommended daily iron intake for women during their menstrual cycle ?",
        a: "10 milligrams (mg)",
        b: "15 mg",
        c: "18 mg",
        d: "27 mg",
        correct: "c",
    },
    // 6
    {
        question: "What are some alternative menstrual products to manage periods ?",
        a: "Menstrual cups",
        b: "Reusable pads",
        c: "Period underwear",
        d: "All of the above",
        correct: "d",
    },
    // 7
    {
        question: "At what age do most girls start their period ?",
        a: "8-9 years",
        b: "10-11 years",
        c: "12-13 years",
        d: "14-15 years",
        correct: "c",
    },
    // 8
    {
        question: "What is PMS (premenstrual syndrome) ?",
        a: "A group of symptoms that occur in the days leading up to a woman's period",
        b: "A disorder that affects the menstrual cycle",
        c: "A type of birth control",
        d: "None of the above",
        correct: "a",
    },
    // 9
    {
        question: "What is the purpose of a period ?",
        a: "To release the lining of the uterus in case of pregnancy",
        b: "To prepare the uterus for pregnancy",
        c: "To cleanse the uterus",
        d: "None of the above",
        correct: "a",
    },
    // 10
    {
        question: "At what age does menopause usually occur ?",
        a: "30-35 years",
        b: "40-45 years",
        c: "45-55 years",
        d: "55-60 years",
        correct: "c",
    },
    // 11
    {
        question: "What is the medical term for a period that is shorter than normal ?",
        a: "Oligomenorrhea",
        b: "Menorrhagia",
        c: "Hypomenorrhea",
        d: "Polymenorrhea",
        correct: "c",
    },
];

const quiz = document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')

let currentQuiz = 0
let score = 0

loadQuiz()

function loadQuiz() {
    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEls => answerEls.checked = false)
}

function getSelected() {
    let answer 

    answerEls.forEach(answerEls => {
        if(answerEls.checked) {
            answer = answerEls.id
        }
    })
    return answer
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected()

    if(answer) {
        if(answer == quizData[currentQuiz].correct) {
            score++
        }
        currentQuiz++

        if(currentQuiz < quizData.length) {
            loadQuiz()
        }else{
            quiz.innerHTML = `
            <h2>You answered ${score}/${quizData.length} questions correctly</h2>
            <button onclick="location.reload()">Try Again</button>
            `
        }
    }
})
