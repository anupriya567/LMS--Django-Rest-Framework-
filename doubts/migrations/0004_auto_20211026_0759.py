# Generated by Django 3.2.7 on 2021-10-26 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doubts', '0003_rename_doubtq_doubtanswers_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubtanswers',
            name='answer',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doubtanswers',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
