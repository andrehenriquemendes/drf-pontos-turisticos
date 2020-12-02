# Generated by Django 3.1.4 on 2020-12-02 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pontoturistico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocIdentificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='doc_identificacao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.docidentificacao'),
        ),
    ]
