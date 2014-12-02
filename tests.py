from unittest import TestCase

import ddparser as parser
import statements


class ParserTest(TestCase):


  def setUp(self):
    self.magic_token = parser.DDV2_TOKEN

    
  def test_bunchOfStuff(self):

    statements = [
      "ISA #jerk", # i am a jerk
      "ISA #jerk @fred", # fred is a jerk
      "ISA #jerk @fred @joe", #joe says fred is a jerk

      "NOTA #jerk", # i am not a jerk
      "NOTA #jerk @alice", # alice is not a jerk
      "NOTA #jerk @alice @bob", #bob says alice is not a jerk 

      "AGREE http://s1.co",# i agree with this docuent,
      "AGREE http://s1.co @alice", # alice agrees with this document
      "AGREE http://s1.co @alice @eve", # eve says alice agrees with this document
      "DISAGREE http://s1.co", # i disagree with this  document
      "DISAGREE http://s1.co @alice", # alice disagrees with this document,
      "DISAGREE http://s1.co @alice @eve", # eve says alice disagrees with this document
      "TRUST http://s1.co", # i trust this document
      "TRUST http://s1.co @fred", # fred trusts this document
      "TRUST http://s1.co @fred @alice", # alice says fred trusts this document
      "DISTRUST http://s1.co", # i distrust this document
      "DISTRUST http://s1.co @alice", # alice distrusts this document
      "DISTRUST http://s1.co @alce @bob", # bob says alice distrusts this document

      "SAME http://s1.co http://s2.co", # these are the same identities
      "SAME http://s1.co http://s2.co @fred", # fred says these are the same

      "HURT http://s1.co", # this content here hurts. i dissaprove of this. i don't like this, etc
      "HURT http://s1.co @Bob", # bob hurt me, this content explains it
      "HURT http://s1.co @bob @alice", # alice says bob hurt here here

      "FORGIVE dewdrop://link-to-hurt", # this content is forgiven - it's a way of saying you are now ok with this thing that has happend
      # the link should be a previous hurt statementx
      "FORGIVE dewdrop://link-to-hurt @alice", # i forgive alice for this wrong
      "FORGIVE dewdrop://link-to-hurt @alice @bob", # bob has forgiven alice for this wrong

      "THANKS http://s1.co", # i like this, i'm happy about this
      "THANKS http://s1.co @alice", # i like this thing alice did, thanks alice
      "THANKS http://s1.co @alice @bob", #bob says alice is thankfull

      "SORRY http://s1.co", # sorry for doing this thing, to the public
      "SORRY http://s1.co @alice", #alice, sorry i did this
      "SORRY http://s1.co @alcie @bob", #bob has apologized to alice
    ]

    for statement in statements:
      s = parser.parse(self.magic_token + " " +statement)
      

  def test_is(self):
    s = parser.parse(self.magic_token + " ISA #troll http://t.co")

    self.assertIsInstance(s, statements.IsA)
    self.assertEqual(s.group, '#troll')

    s = parser.parse("#ddv2 ISA #troll @trollbob")
    self.assertIsInstance(s, statements.IsA)
    self.assertEqual(s.group, "#troll")
    self.assertEqual(s.member, "@trollbob")

 
  def not_a(self):
    s = parser.parse(self.magic_token + " NOTA #troll")
    self.assertIsInstance(s, statements.NotA)
    self.assertEqual(s.group, "#troll")



