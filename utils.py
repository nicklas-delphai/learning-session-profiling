from time import perf_counter
from delphai_utils.logging import logging

def format_joke(json):
  if 'setup' in json:
    return f'{json["setup"]} {json["delivery"]}'
  else:
    return json['joke']

def performance(func):
  def wrapper(*args):
    now = perf_counter()
    func(*args)
    logging.info(f'took {perf_counter() - now:.3f}')
  return wrapper
