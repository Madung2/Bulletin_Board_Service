# Generated by Django 4.1 on 2022-08-31 10:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=13,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$"
                    )
                ],
                verbose_name="폰 번호",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user.usertype",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(default=0, verbose_name="나이"),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "남성"), ("female", "여성"), ("undefined", "미선택")],
                default="undefined",
                max_length=20,
                verbose_name="성별",
            ),
        ),
    ]
