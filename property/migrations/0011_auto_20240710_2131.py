# Generated by Django 3.2.12 on 2024-07-10 18:31

from django.db import migrations


def set_relation(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner, _ = (
            Owner.objects
            .get_or_create(name=flat.owner,
                           phonenumber=flat.owners_phonenumber,
                           defaults={
                                'pure_phone': flat.owner_pure_phone,
                            })
            )
        flat.owners.set([owner])


def clear_relation(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')

    owners = Owner.objects.all()
    for owner in owners:
        owner.flats.clear()

        

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20240710_1543'),
    ]

    operations = [migrations.RunPython(set_relation,
                                       clear_relation)
    ]
