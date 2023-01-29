import json
from json import JSONDecodeError

"""
создаем класс PostHandler, который загружает, ищет, добавляет и сохраняет посты
"""


class PostHandler:
    def __init__(self, path):
        self.path = path

    """
    Загружает посты из json
    """
    def load_posts(self):
        posts = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            return posts, 'Ошибка получения данных из JSON'

        return posts, None

    """
    ищет посты по вхождению
    """

    def search_posts(self, substr):
        posts = []
        load_posts, error = self.load_posts()
        for post in load_posts:
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts, error

    """
    сохраняет новые посты в json
    """

    def save_posts_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    """
    добавляет пост на страницу
    """

    def add_post(self, post):
        posts, error = self.load_posts()
        posts.append(post)
        self.save_posts_to_json(posts)
