#  i have created this file - GTA
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product, Contact
import random
import requests


def index(request):
    if request.method == 'POST':
        led_id = request.POST.get('led_id')  # Assuming buttons have values like 'led1', 'led2', ...
        state = request.POST.get('state')    # Assuming state values are 'on' or 'off'
        print(f"{led_id} {state}")
    return render(request, 'index.html')

def fetch_data(request):
    url = "https://api.thingspeak.com/channels/1921629/feeds.json?results=2"

    response = requests.get(url)
    data = response.json()

    feeds = data.get('feeds', [])
    for feed in feeds:
        created_at = feed.get('created_at')
        temperature = feed.get('field5')
        humidity = feed.get('field6')
        print(f"Temperature: {temperature}, Humidity: {humidity}")
        return render(request, 'index.html', {'temperature': temperature, 'humidity': humidity})
    
    return HttpResponse('AlexIoT    |     Error in fetching temperature and humidity data')

led_states = {
        'LED1': False,
        'LED2': False,
        'LED3': False,
        'LED4': False,
    }
temperature = 0
humidity = 0
created_at = 0

def write_request():
    # print(f"LED1: {led_states['LED1']}")
    # print(f"LED2: {led_states['LED2']}")
    # print(f"LED3: {led_states['LED3']}")
    # print(f"LED4: {led_states['LED4']}")
    channelStatus = [0,0,0,0]
    channelNameStatus = ['LED1', 'LED2', 'LED3', 'LED4']
    for item in range(len(channelStatus)):
        val = channelNameStatus[item]
        if led_states[val] == True:
            channelStatus[item] = 1
        else:
            channelStatus[item] = 0
    print(channelStatus)

    url = f"https://api.thingspeak.com/update?api_key=87JIILFZ88HY6E9D&field1={channelStatus[0]}&field2={channelStatus[1]}&field3={channelStatus[2]}&field4={channelStatus[3]}&field5={temperature}&field6={humidity}"
    response = requests.get(url)
    data = response.json()


def control_view(request):
    global temperature, humidity, created_at

    if request.method == 'POST':
        led_name = request.POST.get('led')
        led_states[led_name] = not led_states[led_name]
        led_state = 'On' if led_states[led_name] else 'Off'
        print(f"currrent : {led_name} {led_state}")
        write_request()

    else:
        url = "https://api.thingspeak.com/channels/1921629/feeds.json?results=2"
        response = requests.get(url)
        data = response.json()

        feeds = data.get('feeds', [])
        for feed in feeds:
            global temperature, humidity, created_at
            created_at = feed.get('created_at')
            temperature = feed.get('field5')
            humidity = feed.get('field6')
            print(f"Temperature: {temperature}, Humidity: {humidity}")
            data = {
                'led_states': led_states, 
                'temperature': temperature, 
                'humidity': humidity, 
                'created_at' : created_at
                }
            return render(request, 'index.html', data)
    
    data = {
    'led_states': led_states, 
    'temperature': temperature, 
    'humidity': humidity, 
    'created_at' : created_at
    }
    return render(request, 'index.html', data)



def temperature_humidity_view(request):
    api_url = "https://api.thingspeak.com/channels/1921629/feeds.json?results=2"
    
    response = requests.get(api_url)
    data = response.json()

    feeds = data.get('feeds', [])
    for feed in feeds:
        temperature = feed.get('field5')
        humidity = feed.get('field6')
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
    
    return render(request, 'index.html', {'feeds': feeds})


# =======================================================================================================================


# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n]) 

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)


# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')


'''

Api Testing:

https://api.thingspeak.com/update?api_key=87JIILFZ88HY6E9D&field1=0&field2=1&field3=1&field4=0&field5=36&field6=80


https://api.thingspeak.com/channels/1921629/feeds.json?results=2
{
"channel": {
"id": 1921629,
"name": "Alex IoT",
"latitude": "0.0",
"longitude": "0.0",
"field1": "ch1",
"field2": "ch2",
"field3": "ch3",
"field4": "ch4",
"field5": "temp",
"field6": "hum",
"created_at": "2022-11-04T19:44:28Z",
"updated_at": "2023-08-20T17:58:53Z",
"last_entry_id": 2
},
"feeds": [
{
"created_at": "2023-08-20T18:00:24Z",
"entry_id": 1,
"field1": "0",
"field2": "1",
"field3": "1",
"field4": "0",
"field5": "36",
"field6": "80"
},
{
"created_at": "2023-08-20T18:00:53Z",
"entry_id": 2,
"field1": "0",
"field2": "1",
"field3": "1",
"field4": "0",
"field5": "36",
"field6": "80"
}
]
}

i want to print feeds values of field5 and field6
'''