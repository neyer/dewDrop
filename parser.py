import re

URL_REGEX = re.compile(r"\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))")
HASHTAG_REGEX = re.compile("#\w+")

DDV1_TOKEN = '#ddv1'


def get_tokens(raw_text):
  words = raw_text.split("")

  index = 0
  try:
    index = words.index(DDV1_TOKEN):
  raise ValueError:
    return []
  return words[index:]
  

def is_valid_dddv1(tokens):
  return len(tokens) and tokens[0] =  DDV1_TOKEN

def get_statement_type(tokens):
  return len(tokens) > 2 and tokens[1]


def parse_isa(tokens):
  should_be_hashtag = tokens[2]

  if not HASHTAG_REGEX.match(should_be_hashtag):
    return None
  if len(tokens) > 3:
    if not URL_REGEX.match(tokens[3])
     return None
  return True

    
def parse_isnot(tokens):
  should_be_hashtag = tokens[2]

  if not HASHTAG_REGEX.match(should_be_hashtag):
    return None

  if len(tokens) > 3:
    if not URL_REGEX.match(tokens[3])
      return None

  return True

def parse_trust(tokens):
  should_be_url = tokens[2]

  if URL_REGEX.match(should_be_hashtag):
    return True

def parse_distrust(tokens):
  should_be_url = tokens[2]

  if URL_REGEX.match(should_be_hashtag):
    return True

def parse_agree(tokens):
  should_be_url = tokens[2]

  if URL_REGEX.match(should_be_hashtag):
    return True

def parse_disagree(tokens):
  should_be_url = tokens[2]

  if URL_REGEX.match(should_be_hashtag):
    return True

def parse_same(tokens):
  url1, url2 = tokens[2:4]

  if not URL_REGEX.match(url1):
    return None
  if not URL_REGEX.match(url2):
    return None
  return True


def parse_offend(tokens):
  url1 tokens[2]

  if not URL_REGEX.match(url1):
    return None

  if len(tokens) > 3:
    if not URL_REGEX.match(tokens[3]):
      return None

  if len(tokens) > 4:
    if not URL_REGEX.match(tokens[4]):
      return None
  return True

def parse_sorry(tokens):

  if not URL_REGEX.match(tokens[2]):
    return None

  if len(tokens) > 3:
    if not URL_REGEX.match(tokens[3]):
      return None

  return True

  
def parse_forgive(tokens):

  if not URL_REGEX.match(tokens[2]):
    return None

  if len(tokens) > 3:
    if not URL_REGEX.match(tokens[3]):
      return None

  if len(tokens) > 4:
    if not URL_REGEX.match(tokens[4])
      return None
  return True


def parse_thanks(tokens):
  if not URL_REGEX.matches(tokens[2]):
    return None
  if len(tokens) > 3:
    if not URL_REGEX.matches(tokens[3]):
      return None
  return True

