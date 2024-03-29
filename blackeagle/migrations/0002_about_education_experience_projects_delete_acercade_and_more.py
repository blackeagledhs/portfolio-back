# Generated by Django 4.2.9 on 2024-02-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackeagle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('desccription', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='educacion_images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('month_of_income', models.CharField(max_length=10)),
                ('year_of_income', models.IntegerField()),
                ('month_of_egress', models.CharField(max_length=10)),
                ('year_of_egress', models.IntegerField()),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('project_url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='proyectos_images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AcercaDe',
        ),
        migrations.DeleteModel(
            name='Educacion',
        ),
        migrations.DeleteModel(
            name='Experiencia',
        ),
        migrations.DeleteModel(
            name='Proyectos',
        ),
    ]
