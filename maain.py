from flask import Flask

from funct import *

app = Flask(__name__)


if __name__ == '__main__':

    # определям переменную для файла
    file = 'candidates.json'

    @app.route('/')
    def main_page():
        """Корневая страница"""
        return get_all()

    @app.route('/candidate/<int:x>/')
    def candidate_page(pk):
        """страница выдает данные кандидата по пк"""
        return get_by_pk(pk)

    @app.route('/skills/<skill>/')
    def skills_page(skill):
        """Страница выдает данные кандидата по скилу"""
        return get_by_skill(skill)

#127.0.0.1:5000/skills/python   для теста

    app.run()