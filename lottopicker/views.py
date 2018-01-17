from django.http import HttpResponse
from django.shortcuts import render
from random import randint

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

def pick_nums(regs, ll, ul, qty):
    if len(regs) > 0:
        #print "Error! list must be empty. Emptying now."
        del regs[:]

    while len(regs) < qty:
        current_pick = randint(ll, ul)
        if current_pick in regs:
            #print "{0} already chosen. repicking.".format(current_pick)
            continue
        else:
            regs.append(current_pick)

    regs.sort()

def powerball_option(request):
	regs = []
	pb = []
	pick_nums(regs, 1, 69, 5)
	pick_nums(pb, 1, 26, 1)
	powerball = pb[0]
	return render(request, "powerball_option.html", {'regs':regs, 'pb':powerball})

def megamillions_option(request):
	regs = []
	mm = []
	pick_nums(regs, 1, 70, 5)
	pick_nums(mm, 1, 25, 1)
	mmball = mm[0]
	return render(request, "megamillions_option.html", {'regs':regs, 'mm':mmball})

def donate(request):
	return render(request, "donate.html", {})

