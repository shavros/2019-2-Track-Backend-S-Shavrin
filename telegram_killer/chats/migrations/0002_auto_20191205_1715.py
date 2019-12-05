# Generated by Django 2.2.5 on 2019-12-05 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=16)),
                ('url', models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='chat',
            name='is_group_chat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.CharField(default='null', max_length=32),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('added_at', models.DateTimeField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat')),
            ],
        ),
    ]
