from utils import format_joke
import requests
import random

def fibonacci(n):
  if n == 0:
      return 0
  elif n == 1 or n == 2:
      return 1
  else:
      return fibonacci(n-1) + fibonacci(n-2)

def get_joke():
  response = requests.get('https://v2.jokeapi.dev/joke/Any')
  json = response.json()
  number = fibonacci(random.randint(30, 34))
  return f'{number}# {format_joke(json)}'

def print_jokes():
  jokes = '\n'.join([f'{get_joke()}\n' for _ in range(8)])
  print(jokes)

def main():
  print_jokes()




























# def main():
#   import cProfile
#   import pstats
#
#   with cProfile.Profile() as pr:
#     print_jokes()
#   stats = pstats.Stats(pr)
#   stats.sort_stats(pstats.SortKey.TIME)
#   stats.print_stats()
#   # stats.dump_stats(filename='slow.prof')

if __name__ == '__main__':
  main()
