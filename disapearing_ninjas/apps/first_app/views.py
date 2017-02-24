from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'text': "No Ninjas here"
    }
    return render(request, 'first_app/index.html', context)


def ninjas(request):
    context = {
        'text': "All the Ninjas",
        'color': "tmnt.png"
    }
    return render(request, 'first_app/index.html', context)


def show(request, color):

    data = {
        'orange': 'michelangelo.jpeg',
        'red': 'rafaelo.jpeg',
        'purple': 'donatello.jpeg',
        'blue': 'leonardo.jpeg'
    }
    if color not in data:
        context = {
            'text':   "Who are you looking for?",
            'color': 'megan_fox.jpeg'
        }
    else:
        context = {
            'color': data[color],
            'text': color
        }
    return render(request, 'first_app/index.html', context)
