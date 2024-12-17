# Generated by Django 5.1.3 on 2024-12-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica4', '0002_like'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen_url',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('usuario', 'post'), name='unique_like_usuario_post'),
        ),
    ]