# Generated by Django 3.2.7 on 2021-09-19 09:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=10000)),
                ('video_plateform', models.CharField(choices=[('Y', 'Youtube'), ('V', 'Vimeo')], max_length=2)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video_chapter', to='chapters.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='TextChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=10000)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_chapter', to='chapters.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='LinkChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('url', models.URLField(max_length=100)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link_chapter', to='chapters.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='HeadingChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='heading_chapter', to='chapters.chapter')),
            ],
        ),
    ]
