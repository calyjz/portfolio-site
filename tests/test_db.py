import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

#use an in-memory sqlite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of 
        # all models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live 
        # for the duration of the connection, and in the next step we close the connection but 
        # good practice all the same
        test_db.drop_tables(MODELS)

        #close connection to db
        test_db.close()

    def test_timeline_post(self):
        #create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe', 
                                         email = 'john@exmaple.com',
                                         content='Hello world, I\'m John!')
        
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Jane Doe', 
                                         email = 'jane@exmaple.com',
                                         content='Hello world, I\'m Jane!')
        
        assert second_post.id == 2

        #get timeline posts and assert that they're correct
        posts = list(TimelinePost.select().order_by(TimelinePost.created_at.desc()))

        assert len(posts) == 2

        # newest first
        assert posts[0].id == second_post.id
        assert posts[0].name == 'Jane Doe'
        assert posts[0].email == 'jane@exmaple.com'
        assert posts[0].content == 'Hello world, I\'m Jane!'

        assert posts[1].id == first_post.id
        assert posts[1].name == 'John Doe'
        assert posts[1].email == 'john@exmaple.com'
        assert posts[1].content == 'Hello world, I\'m John!'