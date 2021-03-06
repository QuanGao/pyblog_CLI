from database import Database
import uuid
import datetime


class Post(object):
    def __init__(self,
                 blog_id,
                 title, content,
                 author,
                 date=datetime.datetime.utcnow(),
                 id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert("posts", self.json())

    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'date': self.date,
            'id': self.id
        }

    @classmethod
    def get_post_by_id(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['date'],
                   id=post_data['id'])

    @staticmethod
    def get_posts_by_blog(blog_id):
        return [post for post in
                Database.find(collection='posts', query={'blog_id': blog_id})]