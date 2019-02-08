from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars',
                                            to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(
                    choices=[('char', 'char'), ('text', 'text'), ('datetime', 'datetime'), ('date', 'date'),
                             ('float', 'float'), ('integer', 'integer'), ('boolean', 'boolean')], max_length=30)),
                ('length', models.PositiveIntegerField(null=True)),
                ('options',
                 django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), null=True,
                                                           size=None)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
