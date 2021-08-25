import asyncio
import requests
import random

API_KEY = '4483890b3e4b68772aab179f4a6b90a2'


async def get_weather(city):
    request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    temp = int(request.json()['main']['temp'])
    a = random.randint(0, 5)
    print(f"{city} {a} секунд")
    await asyncio.sleep(a)
    print(f"{city} {temp} градусов по Цельсию")


async def asynchronous():
    tasks = [main_loop.create_task(get_weather(city)) for city in ['Kalinkavichy', 'Polatsk', 'Minsk']]
    await asyncio.wait(tasks)


main_loop = asyncio.new_event_loop()

main_loop.run_until_complete(asynchronous())
main_loop.close()