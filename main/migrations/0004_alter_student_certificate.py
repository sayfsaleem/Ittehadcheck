# Generated by Django 4.0.6 on 2023-07-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_student_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
