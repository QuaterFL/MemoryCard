from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("")
main_win.resize(600, 400)

class Question():
    def __init__(self, question, r_answer, wron1, wron2, wron3):
        self.question = question
        self.right_answer = r_answer
        self.wron1 = wron1
        self.wron2 = wron2
        self.wron3 = wron3

text = QLabel("Какой национальности не существует?")
button = QPushButton("Ответить")
RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")

vline1 = QVBoxLayout()
vline2 = QVBoxLayout()

vline1.addWidget(rbtn_1)
vline1.addWidget(rbtn_2)
vline2.addWidget(rbtn_3)
vline2.addWidget(rbtn_4)

hline = QHBoxLayout()
hline.addLayout(vline1)
hline.addLayout(vline2)
RadioGroupBox.setLayout(hline)

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox()
correct = QLabel("Правильно или Неправильно")
r_answer = QLabel("Правильный ответ")
vline3 = QVBoxLayout()
vline3.addWidget(correct)
vline3.addWidget(r_answer)
AnsGroupBox.setLayout(vline3)
AnsGroupBox.hide()
v = QVBoxLayout()
v.addWidget(text)
v.addWidget(RadioGroupBox)
v.addWidget(AnsGroupBox)
v.addWidget(button)

main_win.cur_question = -1



def show_question():
    button.setText("Ответить")
    RadioGroupBox.show()
    AnsGroupBox.hide()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    button.setText("Следуйщий вопрос")
    RadioGroupBox.hide()
    AnsGroupBox.show()

def click_OK():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ack(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wron1)
    answer[2].setText(q.wron2)
    answer[3].setText(q.wron3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answer[0].isChecked():
        main_win.score += 1
        show_correct("Правильно")
        print("Статистика:")
        ctat()
        print("Рейтинг:", main_win.score/main_win.total * 100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct("Неправилльно")
        print("Статистика:")
        ctat()
        print("Рейтинг:", main_win.score/main_win.total * 100)

def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ctat()
    ack(q)

def show_correct(res):
    correct.setText(res)
    show_result()

def ctat():
    print("-Всего вопросов:", main_win.total)
    print("-Правильных ответов:", main_win.score)

question_list = []
q = Question("Сколько Петя сидит в туалете", "10799 часов", "3 часа", "10800 секунд", "181 минута")
question_list.append(q)
question_list.append(Question("Сколько будет летать Рыба", "0", "Я хз", "Осминог", "999"))
question_list.append(Question("Если Ваня Иван, то Даня", "Даниил", "Диван", "20", "0"))
question_list.append(Question("Когда 16 раз пукнул Путин от рождения", "через 12592 секунд", "Лёша", "Он пукает постоянно", "через 1 секунду"))
question_list.append(Question("Когда 79 начало ходить", "20", "79", "97", "нет"))
question_list.append(Question("Когда родился Путин", "Он вечен", "в 0 лет", "в 97 лет", "в 9999 году до н. э."))
question_list.append(Question("Битва с евреями закончилась", "цифрами", "звёздами", "Пушкином", "да"))
question_list.append(Question("Какого пола оно", "да", "нет", "не знаю", "не думаю"))
question_list.append(Question("Что будет если Европу поделить на Америку", "Евразия", "Толстой", "6", "5"))
question_list.append(Question("Дождь из", "тако", "да", "Лермонтов", "20"))
question_list.append(Question("Лёд тает только", "зимой", "да", "холодильник", "нет"))

main_win.score = 0
main_win.total = 0
next_question()

button.clicked.connect(click_OK)
main_win.setLayout(v)
main_win.show()
app.exec_()
