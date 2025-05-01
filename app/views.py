from django.shortcuts import render
import requests
# Create your views here.
api_key ='giveurapikey'
def index(request):
    context =None
    if request.method == "POST":
        city = request.POST.get('city')
        data= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
        # print(data)
        main=data["weather"][0]['main']
        description=data["weather"][0]['description']
        temp=data['main']['temp']
        wind=data['wind']['speed']
        name=data['name']
        print(main,description,temp,wind,name)
        context={
        "main":main,
        "description":description,
        "temp":temp,
        "wind":wind,
        "name":name
     }
    return render(request, 'index.html',context)
