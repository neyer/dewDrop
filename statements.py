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

    classs.Fields.insert(0, (self.name, self.category))

    return classs

class Statement(object):
    
    def __init__(*args, **kwargs):
      for key, value in kwargs.items():
        setattr(self, key, value)


    def parse(statement, tokens):
      token_offset = 1
      fields = statement.__class__.Fields
      for field, token in zip(fields,
                              tokens[token_offset:]):
        print 'setting', field
        setattr(statement, field[0], token)
    


@HasField("group","hashtag")
@HasField("member","url")
@HasField("claimaint","url")
class IsA(Statement): pass


@HasField("group","hashtag")
@HasField("nonmember", "url")
@HasField("claimaint","url")
class NotA(Statement): pass

@HasField("statement","url")
@HasField("agreer","url")
@HasField("claimant","url")
class Agree(Statement): pass

@HasField("statement","url")
@HasField("disagreer","url")
@HasField("claimant","url")
class Disagree(Statement): pass

@HasField("statement","url")
@HasField("truster","url")
@HasField("claimant","url")
class Trust(Statement): pass

@HasField("statement","url")
@HasField("distruster","url")
@HasField("claimant","url")
class Distrust(Statement): pass

@HasField("source","url")
@HasField("dest","url")
@HasField("claimant","url")
class Same(Statement): pass

@HasField("description","url")
@HasField("accused","url")
@HasField("accuser","url")
class Hurt(Statement): pass

@HasField("description","url")
@HasField("forgiven","url")
@HasField("forgiver","url")
class Forgive(Statement): pass

@HasField("description","url")
@HasField("recipient","url")
@HasField("giver","url")
class Thanks(Statement): pass

@HasField("description","url")
@HasField("recipient","url")
@HasField("giver","url")
class Sorry(Statement): pass

def get_class_for_token(token):
  return all_statement_classes.get(token)


