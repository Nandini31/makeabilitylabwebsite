# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20151220_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='award',
            field=models.CharField(choices=[('Best Paper Award', 'Best Paper Award'), ('Honorable Mention', 'Honorable Mention'), ('Best Paper Nominee', 'Best Paper Nominee')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='extended_abstract',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='publication',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='num_pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='official_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='page_num_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='page_num_start',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='peer_reviewed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='publication',
            name='projects',
            field=models.ManyToManyField(blank=True, null=True, to='website.Project'),
        ),
        migrations.AddField(
            model_name='publication',
            name='pub_venue_type',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Article', 'Article'), ('Journal', 'Journal'), ('Book Chapter', 'Book Chapter'), ('Book', 'Book'), ('MS Thesis', 'MS Thesis'), ('PhD Dissertation', 'PhD Dissertation'), ('Workshop', 'Workshop'), ('Poster', 'Poster'), ('Demo', 'Demo'), ('Work in Progress', 'Work in Progress'), ('Late Breaking Result', 'Late Breaking Result'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='talk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Talk'),
        ),
        migrations.AddField(
            model_name='publication',
            name='total_papers_admitted',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='total_papers_submitted',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='video_preview_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='website.Keyword'),
        ),
    ]
