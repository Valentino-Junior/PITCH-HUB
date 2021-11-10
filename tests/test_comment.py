from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_wikitae = User(username = 'wikitae',password = 'wak234', email = 'wikitae123@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='Demo comment',category="interview",user = self.user_wikitae,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Demoz comment',user=self.user_wikitae,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_wikitae)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)