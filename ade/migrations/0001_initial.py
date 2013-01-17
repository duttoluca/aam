# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ADE_request'
        db.create_table('ade_ade_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('return_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('ade', ['ADE_request'])

        # Adding model 'ADE_detail'
        db.create_table('ade_ade_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cfisc', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('ADE_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ade.ADE_request'])),
        ))
        db.send_create_signal('ade', ['ADE_detail'])


    def backwards(self, orm):
        # Deleting model 'ADE_request'
        db.delete_table('ade_ade_request')

        # Deleting model 'ADE_detail'
        db.delete_table('ade_ade_detail')


    models = {
        'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ade.ADE_request']"}),
            'Meta': {'object_name': 'ADE_detail'},
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ade.ade_request': {
            'Meta': {'object_name': 'ADE_request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ade']