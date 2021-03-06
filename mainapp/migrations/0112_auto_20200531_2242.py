# Generated by Django 2.2.11 on 2020-05-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0111_auto_20190818_2208"),
    ]

    operations = [
        migrations.CreateModel(
            name="HashTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(model_name="announcements", name="hashtags",),
        migrations.AlterField(
            model_name="smsjob",
            name="sms_type",
            field=models.CharField(
                choices=[
                    ("consent", "Consent"),
                    ("info", "Information"),
                    ("survey", "Survey"),
                ],
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="announcements",
            name="hashtags",
            field=models.ManyToManyField(
                blank=True,
                help_text="Add hashtags as comma separated values.",
                to="mainapp.HashTag",
            ),
        ),
    ]
