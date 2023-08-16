import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")
django.setup()

from core.Country.models import Country

with open("countries.txt") as file:
    data = [c.strip() for c in file.readlines()]
    print(data)

for country_name in data:
    print(country_name)
    country, created = Country.objects.get_or_create(name=country_name)
    if created:
        print(f"Created country: {country.name}")
    else:
        print(f"Country already exists: {country.name}")
