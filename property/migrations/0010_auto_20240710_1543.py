# Generated by Django 3.2.12 on 2024-07-10 12:43

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [migrations.RunPython(copy_owners)
    ]
