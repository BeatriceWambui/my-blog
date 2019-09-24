import unittest
from app import db
from app.models import Post, User

class PostTest(unittest.TestCase):
    def setUp(self):
        self.user_user= User(username = 'bae',password = 'wambui', email = 'wambui@gmail.com')
        self.new_post = Post(id = 1,title='new post',description='hello this is my post trial',user_id = self.user_user )
    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'new post')
        self.assertEquals(self.new_blog.content, 'hello this is my post trial')
        self.assertEquals(self.new_blog.user_id, self.user_user.id)

    def test_save_blog(self):
        self.new_post.save()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_blog(self):
        self.new_post.save()
        post = Post.get_posts(1)
        self.assertTrue(get_posts is not None)
