# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'ADE_detail', fields ['cfisc_orig']
        db.create_index('ade_ade_detail', ['cfisc_orig'])


    def backwards(self, orm):
        # Removing index on 'ADE_detail', fields ['cfisc_orig']
        db.delete_index('ade_ade_detail', ['cfisc_orig'])


    models = {
        'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ade.ADE_request']"}),
            'CAP_residenza': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'ordering': "['ADE_request', 'cfisc_orig']", 'object_name': 'ADE_detail'},
            'cc1': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'cc2': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cfisc_orig': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'civico_residenza': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'cod_belfiore_nascita': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cod_belfiore_residenza': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cognome_denominazione': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'comune_nascita': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'comune_residenza': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'data_decesso': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'data_fonte': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'data_nascita': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'fonte': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ind_conf_comune': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ind_decesso': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ind_norm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'nat_giurid': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'nome_acronimo': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'nome_via_residenza': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'prov_nascita': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'prov_residenza': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'sedime_residenza': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sesso': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sogg_valido': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'ade.ade_request': {
            'Meta': {'ordering': "['-insert_date']", 'object_name': 'ADE_request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ade']