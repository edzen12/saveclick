# Generated by Django 4.1.4 on 2022-12-14 07:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title_1', models.CharField(blank=True, max_length=233, null=True, verbose_name='Заголовок баннера №1')),
                ('banner_title_1_ru', models.CharField(blank=True, max_length=233, null=True, verbose_name='Заголовок баннера №1')),
                ('banner_title_1_en', models.CharField(blank=True, max_length=233, null=True, verbose_name='Заголовок баннера №1')),
                ('banner_desc_1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание баннера №1')),
                ('banner_desc_1_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание баннера №1')),
                ('banner_desc_1_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание баннера №1')),
                ('aboutus_title_1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №1')),
                ('aboutus_title_1_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №1')),
                ('aboutus_title_1_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №1')),
                ('aboutus_title_2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №2')),
                ('aboutus_title_2_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №2')),
                ('aboutus_title_2_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №2')),
                ('aboutus_title_3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №3')),
                ('aboutus_title_3_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №3')),
                ('aboutus_title_3_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №3')),
            ],
            options={
                'verbose_name': 'О нас - главная стр',
                'verbose_name_plural': 'О нас - главная стр',
            },
        ),
        migrations.CreateModel(
            name='Harassment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title_1', models.CharField(blank=True, max_length=233, null=True, verbose_name='название')),
                ('banner_title_1_ru', models.CharField(blank=True, max_length=233, null=True, verbose_name='название')),
                ('banner_title_1_en', models.CharField(blank=True, max_length=233, null=True, verbose_name='название')),
                ('harassment_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание харассмента')),
                ('harassment_desc_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание харассмента')),
                ('harassment_desc_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание харассмента')),
            ],
            options={
                'verbose_name': 'харассмент - обучение стр',
                'verbose_name_plural': 'харассмент - обучение стр',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название сайта')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Название сайта')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Название сайта')),
                ('icon', models.ImageField(blank=True, upload_to='images/', verbose_name='Логотип')),
                ('keywords', models.TextField(blank=True, max_length=255, null=True, verbose_name='Ключевые слова для поиска')),
                ('keywords_ru', models.TextField(blank=True, max_length=255, null=True, verbose_name='Ключевые слова для поиска')),
                ('keywords_en', models.TextField(blank=True, max_length=255, null=True, verbose_name='Ключевые слова для поиска')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Пара слов для поиска')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Пара слов для поиска')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Пара слов для поиска')),
                ('address_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('address_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на расположение по карте')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='Электронная почта')),
                ('whatsapp', models.CharField(blank=True, help_text='Поставьте сюда ссылку на whatsapp, например: https://wa.me/+996700400400', max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, help_text='Поставьте сюда ссылку на telegram, например: https://t.me/noviritm', max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, help_text='Поставьте сюда ссылку на facebook, например: https://www.facebook.com/newrhythm', max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, help_text='Поставьте сюда ссылку на instagram, например: https://www.instagram.com/noviritm/', max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, help_text='Поставьте сюда ссылку на twitter, например: https://twitter.com/NoviRitm_2014', max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, help_text='Поставьте сюда ссылку на youtube, например: https://www.youtube.com/channel/UC5YyBkynZRxAIKSGBzMlftw', max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'основные настройки',
                'verbose_name_plural': 'Основные настройки',
            },
        ),
    ]