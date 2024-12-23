# Generated by Django 5.1.4 on 2024-12-23 12:41

from django.db import migrations


def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='admin',
        email='admin@valorantcheaterreport.com',
        password='Jose32@!'
    )


def delete_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),  # Certifique-se de que esta é a migração correta.
    ]

    operations = [
        migrations.RunPython(create_admin_user, delete_admin_user),
    ]