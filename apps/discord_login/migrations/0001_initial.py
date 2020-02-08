# Generated by Django 3.0.1 on 2020-02-08 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordGuild',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('icon', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('avatar', models.TextField(blank=True)),
                ('username', models.TextField()),
                ('discriminator', models.TextField()),
                ('locale', models.TextField()),
                ('guilds', models.ManyToManyField(related_name='users', to='discord_login.DiscordGuild')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='discord',
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
