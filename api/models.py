from django.db import models

# Data to fill the fields
COLOR_CHOICE = (
    ('blanca','Blanca'),
    ('mulata','Mulata'),
    ('rubia','Rubia'),
    ('negra', 'Morena oscura')
)
EYES_CHOICE = (
    ('azul','Azules'),
    ('verde','Verdes'),
    ('cafe','Café'),
    ('ambar','Ámbar'),
    ('gris','grises'),
    ('avellana','Avellana'),
    ('otro','Otros'),
)
ETHNICITY_CHOICE = (
    ("mestiza", "Mestiza"),  # Mixed race, indigenous and white
    ("indígena", "Indígena"),   # Indigenous people of Mexico
    ("afro","Afro"),   # Black African descent
    ("blanca", "Caucásica"),     # White European descent
    ("americana",  "Americana"),     # White American ancestry
    ("asiatica",  "Asiana"),       # Asian ancestry
    ("latina",  "Latinoamericana"), # Latin American ancestry
)
HEIGHT_CHOICE = (
    ("muybajo", "Muy Bajo"),
    ("bajo", "Bajo"),
    ("promedio", "Promedio"),
    ("alto", "Alto"),
    ("muyalto","Muy Alto"),
)
WEIGHT_CHOICE = (
    ("delgado", "Contextura delgado"),
    ("normal", "Contextura Promedio"),
    ("sobrepeso","Contextura gruesa"),
)
GENDER_CHOICE = (
    ("hombre", "Hombre"),
    ("mujer", "Mujer"),
    ("nobinario",  "No binario/Prefiero no decirlo"),
)

# Create your models here.
class PersonDesc(models.Model):
    nickname = models.CharField(max_length=200, blank=False)
    approx_age = models.PositiveSmallIntegerField()
    color_skin = models.CharField(max_length=20, choices=COLOR_CHOICE, default='Blanca')
    eyes_color = models.CharField(max_length=20, choices=EYES_CHOICE, default='Azules')
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_CHOICE, default='Americana')
    height = models.CharField(max_length=20, choices=HEIGHT_CHOICE, default='Promedio')
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICE, default='Contextura Promedio')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='Mujer')
    tattos = models.BooleanField(default=False)
    scares = models.BooleanField(default=False)

