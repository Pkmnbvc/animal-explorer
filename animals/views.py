from django.shortcuts import render, get_object_or_404
from .models import Animal
# Create your views here.
def home(request):
    return render(request, 'animals/home.html')

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals/animal_detail.html', {'animal': animal})

def animal_category(request, category):
    animals = Animal.objects.filter(category=category)
    return render(
        request,
        'animals/animal_category.html',
        {'animals': animals, 'category': category}
    )

def search_animals(request):
    query = request.GET.get('q', '')

    if query:
        animals = Animal.objects.filter(name__icontains=query)
    else:
        animals = Animal.objects.none()

    return render(
        request,
        'animals/search_results.html',
        {
            'animals': animals,
            'query': query,
        }
    )