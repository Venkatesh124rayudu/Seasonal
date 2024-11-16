# Generated by Django 5.1.3 on 2024-11-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('flavor_suggestion', models.TextField()),
                ('allergy_concerns', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerFeedback',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='seasonalflavor',
            name='available_until',
        ),
        migrations.AddField(
            model_name='seasonalflavor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='seasonalflavor',
            name='season',
            field=models.CharField(default='Winter', max_length=50),
        ),
    ]