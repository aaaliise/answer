from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def tit():
    return render_template('index2.html', title='Главная страница')


@app.route('/answer')
@app.route('/auto_answer')
def index():
    title = 'Анкета'
    surname = 'Watny'
    name = 'Mark'
    education = 'выше среднего'
    profession = 'штурман марсохода'
    sex = 'male'
    motivation = 'Всегда мечтал застрять на Марсе!'
    ready = 'True'
    dic = {'Фамилия': surname, 'Имя': name, 'Образование': education, 'Профессия': profession,
         'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}
    return render_template('auto_answer.html', title=title, dic=dic)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
