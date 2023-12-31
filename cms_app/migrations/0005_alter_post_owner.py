# Generated by Django 4.1.6 on 2023-07-29 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0004_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='cms_app.user'),
            preserve_default=False,
        ),
    ]
