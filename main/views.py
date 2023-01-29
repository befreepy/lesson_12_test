from flask import Blueprint, render_template, request
import logging

from main.utils import PostHandler

"""
создаем блюпринт main
"""
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

"""
вывод формы на главной странице при обращении к /
"""
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

"""
поиск и вывод постов при обращении на /search
"""
@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    logging.info(f'Поиск: {substr}')
    post_handler = PostHandler('posts.json')
    posts, error = post_handler.search_posts(substr)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка!'
    return render_template('post_list.html', posts=posts, substr=substr)
