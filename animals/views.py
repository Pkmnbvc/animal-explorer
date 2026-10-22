from django.shortcuts import render, get_object_or_404
from .models import Animal
from django.http import Http404


#views for the animal encyclopedia app



def home(request):
    return render(request, 'animals/home.html')

def categories(request):
    return render(request, 'animals/categories.html')


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

MASCOTS = {
    'katie-joey': {
        'name': 'Katie & Joey',
        'category': 'Mammal',
        'category_label': 'Mammals',
        'image': 'animals/images/mascot-profiles/katie2.png',
        'background': 'animals/images/mascot-backgrounds/katie-bg.png',
    },
    'philippe': {
        'name': 'Philippe',
        'category': 'Bird',
        'category_label': 'Birds',
        'image': 'animals/images/mascot-profiles/philippe2.png',
        'background': 'animals/images/mascot-backgrounds/philippe-bg.png',
    },
    'mushu': {
        'name': 'Mushu',
        'category': 'Reptile',
        'category_label': 'Reptiles',
        'image': 'animals/images/mascot-profiles/mushu2.png',
        'background': 'animals/images/mascot-backgrounds/mushu-bg.png',
    },
    'lilypad': {
        'name': 'Lilypad',
        'category': 'Amphibian',
        'category_label': 'Amphibians',
        'image': 'animals/images/mascot-profiles/lilypad_2.png',
        'background': 'animals/images/mascot-backgrounds/lilypad-bg.png',
    },
    'cora': {
        'name': 'Cora',
        'category': 'Fish',
        'category_label': 'Fish',
        'image': 'animals/images/mascot-profiles/cora2.png',
        'background': 'animals/images/mascot-backgrounds/cora-bg.png',
    },
    'sheldon': {
        'name': 'Sheldon',
        'category': 'Arthropod',
        'category_label': 'Arthropods',
        'image': 'animals/images/mascot-profiles/sheldon_2.png',
        'background': 'animals/images/mascot-backgrounds/sheldon-bg.png',
    },
}

def mascot_profile(request, mascot):
    mascot_data = MASCOTS.get(mascot)

    if mascot_data is None:
        raise Http404("Mascot not found")

    return render(
        request,
        'animals/mascot_profile.html',
        {'mascot': mascot_data}
    )

