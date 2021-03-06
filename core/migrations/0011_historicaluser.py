# Generated by Django 2.2.12 on 2020-04-15 03:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20200414_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('user_iid', models.IntegerField(blank=True, db_index=True)),
                ('user_type', models.CharField(help_text='Tipo de usuario', max_length=32, verbose_name='Tipo')),
                ('user_value', models.CharField(help_text='Valor/Nombre de Usuario', max_length=128, verbose_name='Sujeto')),
                ('name', models.CharField(blank=True, help_text='Nombre Completo del Usuario', max_length=512, null=True, verbose_name='Nombre Completo')),
                ('email', models.CharField(blank=True, help_text='Correo Electrónico del Usuario', max_length=256, null=True, verbose_name='Correo Electrónico')),
                ('phone', models.CharField(blank=True, help_text='Número Telefónico del Usuario', max_length=64, null=True, verbose_name='Teléfono')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación del Dispositivo', verbose_name='Creado')),
                ('last_seen', models.DateTimeField(blank=True, editable=False, help_text='Última Visita del Dispositivo', verbose_name='Última Visita')),
                ('created_ip_address', models.CharField(blank=True, help_text='Dirección IP desde la que fue creado', max_length=32, null=True, verbose_name='IP de creación')),
                ('address', models.CharField(blank=True, help_text='Dirección por defecto del Usuario', max_length=400, null=True, verbose_name='Dirección')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Ubicación por defecto del Usuario', null=True, srid=4326, verbose_name='Ubicación')),
                ('city', models.CharField(blank=True, help_text='Dirección por defecto del Usuario', max_length=30, null=True, verbose_name='Ciudad')),
                ('city_code', models.CharField(blank=True, help_text='Código de Ciudad por Defecto del Usuario', max_length=30, null=True, verbose_name='Código Ciudad')),
                ('password_hash', models.CharField(blank=True, help_text='Contraseña del Usuario', max_length=64, null=True, verbose_name='Password')),
                ('password_salt', models.CharField(blank=True, help_text='Salt de Contraseña del Usuario', max_length=64, null=True, verbose_name='Password Salta')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
