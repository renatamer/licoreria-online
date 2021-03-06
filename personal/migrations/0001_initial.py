# Generated by Django 3.1.4 on 2020-12-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('pregunta', models.TextField(max_length=400)),
                ('prioridad', models.CharField(choices=[('B', 'Baja'), ('M', 'Media'), ('A', 'Alta')], max_length=1)),
            ],
        ),
    ]
