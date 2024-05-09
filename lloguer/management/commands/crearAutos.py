from django.core.management.base import BaseCommand
from faker import Faker
from faker_vehicle import VehicleProvider

from lloguer.models import *

faker = Faker(["es_CA","es_ES"])

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(VehicleProvider)

        for _ in range(200):
            marca = fake.vehicle_make()
            model = fake.vehicle_model()
            matricula = faker.license_plate()
            Automobil.objects.create(marca=marca, model=model, matricula=matricula)
            print(f'Automobil {marca} {model} {matricula} creat')
        self.stdout.write('Productos añadidos correctamente')
