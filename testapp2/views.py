from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    recipe=Recipes.objects.all()
    return render(request, 'items/home.html',{'recipe':recipe})

def details(request):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'testapp3/details.html', {'recipe': recipe})

def create(request):
    return render(request, 'items/create.html')

def data(request):
    if request.method == "POST":
        Recipes.objects.create(
        food=request.POST["food"],
        ingredients=request.POST["ingredients"],
        process=request.POST["process"],

        )
        return HttpResponseRedirect('/testapp3/recipe_list/')
    return render(request,'testapp3/create.html')

def recipe_list(request):
    recipe = Recipes.objects.all()
    return render(request, 'testapp3/list.html',{'recipe': recipe})