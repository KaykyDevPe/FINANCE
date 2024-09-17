# Generated by Django 5.1.1 on 2024-09-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('banco', models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa Econômica'), ('BR', 'Bradesco'), ('C6', 'C6 Bank')], max_length=2)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa física'), ('PJ', 'Pessoa jurídica')], max_length=2)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]
