# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('photoblog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('photoblog', ['Category'])

        # Adding model 'Location'
        db.create_table('photoblog_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('photoblog', ['Location'])

        # Adding model 'Tag'
        db.create_table('photoblog_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('photoblog', ['Tag'])

        # Adding model 'Photo'
        db.create_table('photoblog_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('date_uploaded', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photos', null=True, to=orm['photoblog.Category'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photos', null=True, to=orm['photoblog.Location'])),
        ))
        db.send_create_signal('photoblog', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('photoblog_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['photoblog.photo'], null=False)),
            ('tag', models.ForeignKey(orm['photoblog.tag'], null=False))
        ))
        db.create_unique('photoblog_photo_tags', ['photo_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('photoblog_category')

        # Deleting model 'Location'
        db.delete_table('photoblog_location')

        # Deleting model 'Tag'
        db.delete_table('photoblog_tag')

        # Deleting model 'Photo'
        db.delete_table('photoblog_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('photoblog_photo_tags')


    models = {
        'photoblog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'photoblog.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'photoblog.photo': {
            'Meta': {'object_name': 'Photo'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'to': "orm['photoblog.Category']"}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'date_uploaded': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'to': "orm['photoblog.Location']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photoblog.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'photoblog.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['photoblog']