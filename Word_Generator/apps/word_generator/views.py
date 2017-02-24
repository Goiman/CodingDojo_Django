from django.shortcuts import render
from django.utils.crypto import get_random_string
import random

def index(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1
	context = {
	"counter":request.session['counter'],
	"word":get_random_string(length=14)
	}
	return render(request, 'word_generator/index.html', context)

def submit(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1
	word=""
	rgb = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(0,14):
		word = word + str(random.choice(rbg))
	context = {
	"counter":request.session['counter'],
	"word":word
	}
	return redirect('/')
