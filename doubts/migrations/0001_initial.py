# Generated by Django 3.2.7 on 2021-10-25 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_tag'),
        ('chapters', '0002_headingchapter_linkchapter_textchapter_videochapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubts', to='chapters.chapter')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubts', to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
