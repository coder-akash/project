# Generated by Django 4.1.4 on 2023-03-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="employeedetails",
            fields=[
                ("EMPLOYEE_ID", models.AutoField(primary_key=True, serialize=False)),
                ("EMPLOYEE_NAME", models.CharField(max_length=70)),
                ("DATE_OF_JOINING", models.DateField()),
                ("SALARY", models.BigIntegerField()),
                ("MOBILE", models.BigIntegerField()),
                ("DESIGNATION", models.CharField(max_length=100)),
                (
                    "GENDER",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
