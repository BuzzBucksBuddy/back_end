# Generated by Django 4.2.7 on 2023-11-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(choices=[(1, '성공'), (2, 'DATA코드 오류'), (3, '인증코드 오류'), (4, '일일제한횟수 마감')])),
                ('cur_unit', models.TextField(unique=True)),
                ('ttb', models.TextField()),
                ('tts', models.TextField()),
                ('deal_bas_r', models.TextField()),
                ('bkpr', models.TextField()),
                ('yy_efee_r', models.TextField()),
                ('ten_dd_efee_r', models.TextField()),
                ('kftc_bkpr', models.TextField()),
                ('kftc_deal_bas_r', models.TextField()),
                ('cur_nm', models.TextField()),
            ],
        ),
    ]
