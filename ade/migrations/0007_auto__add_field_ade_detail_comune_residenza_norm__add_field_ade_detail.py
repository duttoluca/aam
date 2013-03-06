# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ADE_detail.comune_residenza_norm'
        db.add_column(u'ade_ade_detail', 'comune_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.CAP_residenza_norm'
        db.add_column(u'ade_ade_detail', 'CAP_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.prov_residenza_norm'
        db.add_column(u'ade_ade_detail', 'prov_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.sedime_residenza_norm'
        db.add_column(u'ade_ade_detail', 'sedime_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.nome_via_residenza_norm'
        db.add_column(u'ade_ade_detail', 'nome_via_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.civico_residenza_norm'
        db.add_column(u'ade_ade_detail', 'civico_residenza_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.esponente_norm'
        db.add_column(u'ade_ade_detail', 'esponente_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.cod_err1_norm'
        db.add_column(u'ade_ade_detail', 'cod_err1_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.cod_err2_norm'
        db.add_column(u'ade_ade_detail', 'cod_err2_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.indirizzo_breve_norm'
        db.add_column(u'ade_ade_detail', 'indirizzo_breve_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ADE_detail.comune_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'comune_residenza_norm')

        # Deleting field 'ADE_detail.CAP_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'CAP_residenza_norm')

        # Deleting field 'ADE_detail.prov_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'prov_residenza_norm')

        # Deleting field 'ADE_detail.sedime_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'sedime_residenza_norm')

        # Deleting field 'ADE_detail.nome_via_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'nome_via_residenza_norm')

        # Deleting field 'ADE_detail.civico_residenza_norm'
        db.delete_column(u'ade_ade_detail', 'civico_residenza_norm')

        # Deleting field 'ADE_detail.esponente_norm'
        db.delete_column(u'ade_ade_detail', 'esponente_norm')

        # Deleting field 'ADE_detail.cod_err1_norm'
        db.delete_column(u'ade_ade_detail', 'cod_err1_norm')

        # Deleting field 'ADE_detail.cod_err2_norm'
        db.delete_column(u'ade_ade_detail', 'cod_err2_norm')

        # Deleting field 'ADE_detail.indirizzo_breve_norm'
        db.delete_column(u'ade_ade_detail', 'indirizzo_breve_norm')


    models = {
        u'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ade.ADE_request']"}),
            'CAP_residenza': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'CAP_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'ordering': "['ADE_request', 'cfisc_orig']", 'object_name': 'ADE_detail'},
            'cc1': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'cc2': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cfisc_orig': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'civico_residenza': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'civico_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'cod_belfiore_nascita': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cod_belfiore_residenza': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cod_err1_norm': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cod_err2_norm': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'cognome_denominazione': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'comune_nascita': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'comune_residenza': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'comune_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'data_decesso': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'data_fonte': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'data_nascita': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'esponente_norm': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'fonte': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ind_conf_comune': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ind_decesso': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ind_norm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'indirizzo_breve_norm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nat_giurid': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'nome_acronimo': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'nome_via_residenza': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'nome_via_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'prov_nascita': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'prov_residenza': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'prov_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'sedime_residenza': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sedime_residenza_norm': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'sesso': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sogg_valido': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'ade.ade_request': {
            'Meta': {'ordering': "['-insert_date']", 'object_name': 'ADE_request'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ade']