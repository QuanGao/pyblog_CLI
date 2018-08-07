from database import Database
import uuid
import datetime
from models.post import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('Enter post  title')
        content = input('Enter post content')
        date = input('Enter date (MMDDYYYY) or leave blank for today')
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, '%d%m%Y')
        post = Post(title=title,
                    content=content,
                    author=self.author,
                    blog_id=self.id,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.get_posts_by_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_blog(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id':id})
        return cls(author = blog_data['author'],
                   title = blog_data['title'],
                   content = blog_data['content'],
                   description = blog_data['description'],
                   id = blog_data['id'])
