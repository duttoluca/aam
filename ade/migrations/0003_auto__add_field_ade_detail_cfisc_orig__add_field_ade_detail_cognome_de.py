# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ADE_detail.cfisc_orig'
        db.add_column('ade_ade_detail', 'cfisc_orig',
                      self.gf('django.db.models.fields.CharField')(default='pippo', max_length=16),
                      keep_default=False)

        # Adding field 'ADE_detail.cognome_denominazione'
        db.add_column('ade_ade_detail', 'cognome_denominazione',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.nome_acronimo'
        db.add_column('ade_ade_detail', 'nome_acronimo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ADE_detail.cfisc_orig'
        db.delete_column('ade_ade_detail', 'cfisc_orig')

        # Deleting field 'ADE_detail.cognome_denominazione'
        db.delete_column('ade_ade_detail', 'cognome_denominazione')

        # Deleting field 'ADE_detail.nome_acronimo'
        db.delete_column('ade_ade_detail', 'nome_acronimo')


    models = {
        'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ade.ADE_request']"}),
            'Meta': {'ordering': "['ADE_request', 'cfisc_orig']", 'object_name': 'ADE_detail'},
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cfisc_orig': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'cognome_denominazione': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_acronimo': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        'ade.ade_request': {
            'Meta': {'ordering': "['insert_date']", 'object_name': 'ADE_request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ade']