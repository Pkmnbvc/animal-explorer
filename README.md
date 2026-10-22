# Animal Explorer 🐾

Animal Explorer is a colorful, kid-friendly animal encyclopedia built with Django for CSCI 4830.

The application allows users to explore animal categories, meet themed mascot guides, search for animals, and view individual animal passport pages with information such as habitat, diet, lifespan, scientific name, and fun facts.

## Features

- Animal category browsing
- Search by animal name
- Individual animal passport pages
- Mascot team pages for each animal category
- Responsive, child-friendly interface
- Animal data stored with Django models
- Deployed on Amazon AWS EC2

## Animal Categories

- Mammals
- Birds
- Reptiles
- Amphibians
- Fish
- Arthropods

Each category has its own mascot guide:

- Katie & Joey — Mammals
- Philippe — Birds
- Mushu — Reptiles
- Lilypad — Amphibians
- Cora — Fish
- Sheldon — Arthropods

## Technology

- Python
- Django
- HTML
- CSS
- Git / GitHub
- Amazon AWS EC2
- SQLite

## Live Application

http://34.229.140.24:8000/animals/

## Project Structure

`animals/models.py` — Animal database model

`animals/views.py` — Application views and mascot routing

`animals/urls.py` — Application URL routes

`animals/templates/animals/` — Django HTML templates

`animals/static/animals/` — CSS, mascot artwork, backgrounds, and other static assets

`animals/fixtures/animals.json` — Initial animal data fixture

## Running Locally

Activate the project environment and run:

```bash
python manage.py migrate
python manage.py loaddata animals
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/animals/
```

## Course

CSCI 4830 — Introduction to Software Engineering

Tech Exercise Project
