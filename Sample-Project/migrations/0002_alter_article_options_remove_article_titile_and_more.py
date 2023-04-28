# Generated by Django 4.1.4 on 2023-01-01 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '記事'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='titile',
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='サンプル', max_length=100, verbose_name='タイトル'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='投稿日'),
        ),
        migrations.AlterField(
            model_name='article',
            name='message',
            field=models.TextField(verbose_name='本文'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, blank=True, verbose_name='投稿日')),
                ('content', models.TextField(verbose_name='本文')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Study.article', verbose_name='記事')),
            ],
            options={
                'verbose_name_plural': 'コメント',
            },
        ),
    ]
