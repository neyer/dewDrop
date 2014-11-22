import re

DDV2_TOKEN = '#ddv2'

import statements
import inspect

def get_tokens(raw_text):
  words = raw_text.split(" ")

  index = 0
  try:
    index = words.index(DDV2_TOKEN)
  except ValueError:
    return []
  # now chop out empty words
  return [word for word in words[index:] if word]
  

def is_valid_dddv1(tokens):
  return len(tokens) and tokens[0] == DDV2_TOKEN

def get_statement_type(tokens):
  return len(tokens) > 2 and tokens[1]

def parse(text):
  tokens = get_tokens(text)
  stype = get_statement_type(tokens)
  statement = statements.get_class_for_token(stype)()
  statement.parse(tokens)
  return statement
