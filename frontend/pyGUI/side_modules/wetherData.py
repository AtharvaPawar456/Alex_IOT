# import nabi as nb
from bs4 import BeautifulSoup
import requests


def wether_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # city = input("Enter the Name of City -> ")
    city = 'mumbai'
    city = city+" weather"

    city = city.replace(" ", "+")
    try:
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')

        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather+"°C")

        # nb.speak("Whether of location" +  location)
        # nb.speak('day and time is' + time)
        # nb.speak('its ' + info)
        # nb.speak('temperature is ' + weather)

        print("Have a Nice Day  :)")

    except:
        print("Got Error while accessing Wether Data")
    # This code is contributed by adityatri
wether_data()
