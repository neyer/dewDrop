from unittest import TestCase

import ddparser as parser
import statements


class ParserTest(TestCase):

  def test_is(self):
    s = parser.parse("#ddv2 ISA #troll http://t.co")

    self.assertIsInstance(s, statements.IsA)
    self.assertEqual(s.group, '#troll')


    s = parser.parse("#ddv2 ISA #troll @trollbob")
    self.assertIsInstance(s, statements.IsA)
    self.assertEqual(s.group, "#troll")
    self.assertEqual(s.member, "@trollbob")

