# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ADE_request.return_date'
        db.alter_column('ade_ade_request', 'return_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ADE_request.return_date'
        raise RuntimeError("Cannot reverse this migration. 'ADE_request.return_date' and its values cannot be restored.")

    models = {
        'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ade.ADE_request']"}),
            'Meta': {'ordering': "['ADE_request', 'cfisc']", 'object_name': 'ADE_detail'},
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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