from utils import format_joke
import asyncio
import requests
import random
import httpx

cache = {}

def fibonacci(n):
  if n in cache:
    return cache[n]
  else:
    if n == 0:
        value = 0
    elif n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = value
    return value

async def get_joke():
  async with httpx.AsyncClient() as client:
    response = await client.get('https://v2.jokeapi.dev/joke/Any', timeout=5)
    json = response.json()
  number = fibonacci(random.randint(32, 35))
  return f'{number}# {format_joke(json)}'

async def print_jokes():
  jokes = await asyncio.gather(*[get_joke() for _ in range(8)])
  jokes = '\n'.join([f'{joke}\n' for joke in jokes])
  print(jokes)

async def main():
  import cProfile
  import pstats

  with cProfile.Profile() as pr:
    await print_jokes()
  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  # stats.print_stats()
  stats.dump_stats(filename='stats.prof')

if __name__ == '__main__':
  asyncio.run(main())
