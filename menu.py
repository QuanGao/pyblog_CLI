from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        self.user = input('Enter your name: ')
        self.user_blog = None
        if self._user_has_account():
            print('Welcome back {}!'.format(self.user))
        else:
            self._make_new_account()

    def run_menu(self):
        read_or_write = input('Do you want to read (R) or write (W)? ')
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog(blog_id=blog_id)
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print('Please input a valid option: ')
            self.run_menu()

    def _user_has_account(self):
        user_data = Database.find_one(collection='blogs', query={'author': self.user})
        print('user_data', user_data)
        if user_data is None:
            return False
        else:
            return True

    def _make_new_account(self):
        title = input('Enter your blog title: ')
        description = input("Description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print('ID: {}\n\nAuthor: {}\n\nTitle: {}'.
                  format(blog.id, blog.author, blog.title))

    def _view_blog(self):
        blog_id = input('Enter ID of the blog you want to read ')
        blog = Blog.get_blog(blog_id)
        posts = blog.get_posts()
        for post in posts:
            print('Title: {}\n\n Date: {}\n\n Content: {}'.
                  format(post.title, post.date, post.content))
