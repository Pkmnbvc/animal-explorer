from django.db import models

# Create your models here.
class Animal(models.Model):
    CATEGORY_CHOICES = [
        ('Mammal', 'Mammal'),
        ('Bird', 'Bird'),
        ('Reptile', 'Reptile'),
        ('Amphibian', 'Amphibian'),
        ('Fish', 'Fish'),
        ('Insect', 'Insect'),
        ('Arthropod', 'Arthropod'),
        ('Other Invertebrate', 'Other Invertebrate'),
    ]

    DIET_CHOICES = [
        ('Herbivore', 'Herbivore'),
        ('Carnivore', 'Carnivore'),
        ('Omnivore', 'Omnivore'),
        ('Filter Feeder', 'Filter Feeder'),
        ('Scavenger', 'Scavenger'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    diet = models.CharField(max_length=100, choices=DIET_CHOICES)
    habitat = models.CharField(max_length=100)
    lifespan = models.CharField(max_length=100)
    fun_fact = models.TextField()
    image = models.ImageField(upload_to='animal_images/', null=True, blank=True)

    def __str__(self):
        return self.name