# Generated by Django 4.2.6 on 2023-10-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-created",)},
        ),
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.CharField(max_length=100),
        ),
    ]
