from functools import wraps
import re
import inspect
URL_REGEX = re.compile(".*") # fuck it
HASHTAG_REGEX = re.compile("#\w+")

all_statement_classes = {}

class HasField(object):

  def __init__(self, name, category):
    self.name = name
    self.category = category

  def __call__(self, classs):
    
    field_name = '_'+self.name

    def _check_for_prop(instance):
      if not hasattr(instance, field_name):
        instance.__dict__[field_name] = None

    def _check_for_category(value):
      if self.category == "url":
        if not URL_REGEX.match(value):
          raise ValueError(value+" is not a url")
      elif self.category == "hashtag":
        if not HASHTAG_REGEX.match(value):
          raise ValueError(value+" is not a hashtag")

    def getter(instance):
      _check_for_prop(instance)
      return getattr(instance, field_name)

    def setter(instance, value):
      _check_for_prop(instance)
      _check_for_category(value)
      return setattr(instance, field_name, value)

    setattr(classs, self.name, property(getter, setter))

    # put this guy in the list
    upper_name = classs.__name__.upper()
    all_statement_classes[upper_name] = classs
    # add the list of fields to this class
    if not hasattr(classs, 'Fields'):
      classs.Fields = []

    classs.Fields.append((self.name, self.category))

    return classs

@HasField("context","url")
class Statement(object):
    
    def __init__(*args, **kwargs):
      for key, value in kwargs.items():
        setattr(self, key, value)


@HasField("group","hashtag")
@HasField("member","url")
@HasField("description","url")
class IsA(Statement): 

  def parse(self, tokens):
    self.group = tokens[2]
    if len(tokens) > 3:
      self.member = tokens[3]
    if len(tokens) > 4:
      self.description = tokens[4]


@HasField("group","hashtag")
@HasField("description","url")
class NotA(Statement):

  def parse(self, tokens):
    self.group = tokens[2]
    if len(tokens) > 3:
      self.description = tokens[3] 

@HasField("statement","url")
class Agree(Statement): 
  def parse(self, tokens):
    self.statement = tokens[2]

@HasField("statement","url")
class Disagree(Statement):
  def parse(self, tokens):
    self.statement = tokens[2]


@HasField("statement","url")
class Trust(Statement):

  def parse(self, tokens):
    self.statement = tokens[2]


@HasField("statement","url")
class Distrust(Statement):
  def parse(self, tokens):
    self.statement = tokens[2]

@HasField("source","url")
@HasField("dest","url")
class Same(Statement):
  def parse(self, tokens):
    self.source = tokens[2]
    self.source = tokens[3]


def apply_tripart_statement(statement, tokens):
  token_offset = 2
  fields = statement.__class__.Fields
  for field, token in zip(names, tokens[token_offset:]):
    setattr(statement, field[0], token)


@HasField("accused","url")
@HasField("accuser","url")
@HasField("description","url")
class Hurt(Statement):
  parse = apply_tripart_statement


@HasField("forgiven","url")
@HasField("forgiver","url")
@HasField("description","url")
class Forgive(Statement):
  parse = apply_tripart_statement


@HasField("giver","url")
@HasField("recipient","url")
@HasField("description","url")
class Thanks(Statement):
  parse = apply_tripart_statement


def get_class_for_token(token):
  return all_statement_classes.get(token)


