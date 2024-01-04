from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def homepage(request):
    text = """<h1 style="color: #F4CE14;">Welcome to Little Lemons</h1>"""
    date = datetime.today().year
    message = "Welcome to the year of {}".format(date)
    text_with_message = f"{text}\n<p>{message}</p>"
    return HttpResponse(text_with_message)


def menuitems(request, dish):
    items = {
        'pasta': 'Pasta, a global favorite, blends durum wheat and water into versatile shapes like spaghetti and penne. Boiled or baked, it achieves a cherished al dente texture. Pairing with diverse sauces, from marinara to Alfredo, pasta adapts worldwide, embodying comfort, tradition, and culinary adaptability for countless palates.',
        'falafel': 'Falafel, a beloved Middle Eastern dish, features ground chickpeas or fava beans mixed with herbs and spices. Formed into balls or patties, these are fried to a crispy, golden brown. Served in pita pockets or as part of a mezze, falafel delights with its crunchy exterior and flavorful, herb-infused interior.',
        'cheesecake':'Cheesecake, a luscious dessert, stars a creamy, velvety filling crafted from cream cheese, sugar, and eggs atop a crust, often made from crushed cookies or graham crackers. Baked or set in a refrigerator, its indulgent texture and rich flavor variations—from classic New York to fruity delights—make it a dessert aficionado delight.'
    }

    discription = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + discription)
  
def drinks(request, drink):
    items = {
        'mocha': 'Type of coffee.',
        'tea': 'Type of hot beverage.',
        'lemonade':'Type of refreshment'
    }

    discription = items[drink]

    return HttpResponse(f"<h2> {drink} </h2>" + discription)
  