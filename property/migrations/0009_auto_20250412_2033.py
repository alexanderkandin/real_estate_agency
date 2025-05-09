# Generated by Django 2.2.24 on 2025-04-12 16:33

from django.db import migrations

def edit_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for number in Flat.objects.all():
        phone = number.owners_phonenumber
        number.owner_pure_phone = phone
        number.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250410_1111'),
    ]

    operations = [migrations.RunPython(edit_numbers)

    ]
