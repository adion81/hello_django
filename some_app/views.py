from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context ={
        'name' : "Mr. Nibbles"
    }
    return render(request,"index.html",context)

def another_page(request):
    return render(request, "another_page.html")


def does_nothing(request):
    print("Does nothing but print this sentence.")
    return redirect('/')