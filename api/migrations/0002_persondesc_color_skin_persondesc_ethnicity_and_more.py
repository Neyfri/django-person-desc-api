# Generated by Django 5.0.1 on 2024-02-02 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondesc',
            name='color_skin',
            field=models.CharField(choices=[('blanca', 'Blanca'), ('mulata', 'Mulata'), ('mulata', 'Mulata'), ('negra', 'Morena oscura')], default='Blanca', max_length=20),
        ),
        migrations.AddField(
            model_name='persondesc',
            name='ethnicity',
            field=models.CharField(choices=[('mestiza', 'Mestiza'), ('indígena', 'Indígena'), ('afro', 'Afro'), ('blanca', 'Caucásica'), ('americana', 'Americana'), ('asiatica', 'Asiana'), ('latina', 'Latinoamericana')], default='Americana', max_length=20),
        ),
        migrations.AddField(
            model_name='persondesc',
            name='eyes_color',
            field=models.CharField(choices=[('azul', 'Azules'), ('verde', 'Verdes'), ('marron', 'Marrones'), ('multi', 'Multi-Colores'), ('gris', 'grises')], default='Azules', max_length=20),
        ),
        migrations.AddField(
            model_name='persondesc',
            name='gender',
            field=models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('nobinario', 'No binario/Prefiero no decirlo')], default='Mujer', max_length=20),
        ),
        migrations.AddField(
            model_name='persondesc',
            name='height',
            field=models.CharField(choices=[('muybajo', 'Muy Bajo'), ('bajo', 'Bajo'), ('promedio', 'Promedio'), ('alto', 'Alto'), ('muyalto', 'Muy Alto')], default='Promedio', max_length=20),
        ),
        migrations.AddField(
            model_name='persondesc',
            name='weight',
            field=models.CharField(choices=[('delgado', 'Contextura delgado'), ('normal', 'Contextura Promedio'), ('sobrepeso', 'Contextura gruesa')], default='Contextura Promedio', max_length=20),
        ),
    ]
