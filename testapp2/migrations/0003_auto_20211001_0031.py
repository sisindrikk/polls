# Generated by Django 3.2.7 on 2021-09-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp2', '0002_alter_question_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=25)),
                ('ingredients', models.TextField(max_length=200)),
                ('process', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
