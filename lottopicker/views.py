from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#HttpResponse can only return text. 
	#return HttpResponse("Hello World!")

	#we want to return HTML file
	#use render
	return render(request, "home.html")

def translate(request):
	vowels = ['a', 'e', 'i', 'o', 'u']
	original = request.GET['originaltext']
	translated = []

	if len(original) <= 0:
		original = "You did not provide any word(s) to translate!"
		final_translated = ""
		return render(request, "translate.html", {'original':original})

	for word in original.split():
		first = ""
		if len(word) > 0:
			first = word[0]
			if first in vowels:
				word += "way"
			else:
				word = word[1:]
				word = word + first + "ay"
			translated.append(word)	
	
	final_translated = ""
	for i in range(len(translated)):
		final_translated += (translated[i] + " ")

	return render(request, "translate.html", {'original':original, 'translation':final_translated})	

def about(request):
	return render(request, "about.html", {})