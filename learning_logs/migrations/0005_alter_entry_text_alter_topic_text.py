# Generated by Django 4.1.2 on 2022-11-06 18:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_alter_entry_text_alter_topic_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
