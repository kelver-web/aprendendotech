# Generated by Django 4.1.2 on 2022-11-06 18:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_entry_text_alter_topic_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
