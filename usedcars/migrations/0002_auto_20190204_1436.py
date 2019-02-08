from django.db import migrations

types = (
    ('price', 'float', None, None),
    ('mark', 'char', 20, None),
    ('model', 'char', 20, None),
    ('production_date', 'date', None, None),
    ('mileage', 'integer', None, None),
    ('style', 'char', 20, ['Convertible', 'Coupe', 'Pickup', 'Hatchback', 'Minivan', 'SUV', 'Sedan', 'Van', 'Wagon']),
    ('fuel_type', 'char', 20, ['Diesel', 'Electric', 'Gas', 'Gasoline', 'Hybrid', 'Unknown']),
    ('engine_capacity', 'integer', None, None),
    ('engine_power', 'integer', None, None),
    ('location', 'char', 50, None),
    ('transmission', 'char', 20, ['Automanual', 'Automatic', 'CVT', 'Manual', 'Other / Unknown']),
    ('doors', 'integer', None, None),
    ('country_of_origin', 'char', 30, None),
    ('accident_free', 'boolean', None, None),
    ('description', 'text', None, None)
)


def default_fields(apps, schema_editor):
    Field = apps.get_model("usedcars", "Field")
    for name, type, length, options in types:
        position = Field(name=name, type=type, length=length, options=options)
        position.save()


class Migration(migrations.Migration):
    dependencies = [
        ('usedcars', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_fields),
    ]
