# Generated by Django 3.2.7 on 2021-10-01 01:12

import coupons.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponM',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('discount', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('code', models.CharField(default=coupons.models.random_code, max_length=6)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon', to='courses.course')),
            ],
        ),
    ]
