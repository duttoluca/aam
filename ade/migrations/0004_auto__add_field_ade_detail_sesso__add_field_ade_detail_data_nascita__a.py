# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ADE_detail.sesso'
        db.add_column('ade_ade_detail', 'sesso',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.data_nascita'
        db.add_column('ade_ade_detail', 'data_nascita',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.cod_belfiore_nascita'
        db.add_column('ade_ade_detail', 'cod_belfiore_nascita',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.comune_nascita'
        db.add_column('ade_ade_detail', 'comune_nascita',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.prov_nascita'
        db.add_column('ade_ade_detail', 'prov_nascita',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.cod_belfiore_residenza'
        db.add_column('ade_ade_detail', 'cod_belfiore_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.comune_residenza'
        db.add_column('ade_ade_detail', 'comune_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.prov_residenza'
        db.add_column('ade_ade_detail', 'prov_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.CAP_residenza'
        db.add_column('ade_ade_detail', 'CAP_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.fonte'
        db.add_column('ade_ade_detail', 'fonte',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.data_fonte'
        db.add_column('ade_ade_detail', 'data_fonte',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.sedime_residenza'
        db.add_column('ade_ade_detail', 'sedime_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.nome_via_residenza'
        db.add_column('ade_ade_detail', 'nome_via_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.civico_residenza'
        db.add_column('ade_ade_detail', 'civico_residenza',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.ind_norm'
        db.add_column('ade_ade_detail', 'ind_norm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.ind_decesso'
        db.add_column('ade_ade_detail', 'ind_decesso',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.data_decesso'
        db.add_column('ade_ade_detail', 'data_decesso',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.ind_conf_comune'
        db.add_column('ade_ade_detail', 'ind_conf_comune',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'ADE_detail.nat_giurid'
        db.add_column('ade_ade_detail', 'nat_giurid',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ADE_detail.sesso'
        db.delete_column('ade_ade_detail', 'sesso')

        # Deleting field 'ADE_detail.data_nascita'
        db.delete_column('ade_ade_detail', 'data_nascita')

        # Deleting field 'ADE_detail.cod_belfiore_nascita'
        db.delete_column('ade_ade_detail', 'cod_belfiore_nascita')

        # Deleting field 'ADE_detail.comune_nascita'
        db.delete_column('ade_ade_detail', 'comune_nascita')

        # Deleting field 'ADE_detail.prov_nascita'
        db.delete_column('ade_ade_detail', 'prov_nascita')

        # Deleting field 'ADE_detail.cod_belfiore_residenza'
        db.delete_column('ade_ade_detail', 'cod_belfiore_residenza')

        # Deleting field 'ADE_detail.comune_residenza'
        db.delete_column('ade_ade_detail', 'comune_residenza')

        # Deleting field 'ADE_detail.prov_residenza'
        db.delete_column('ade_ade_detail', 'prov_residenza')

        # Deleting field 'ADE_detail.CAP_residenza'
        db.delete_column('ade_ade_detail', 'CAP_residenza')

        # Deleting field 'ADE_detail.fonte'
        db.delete_column('ade_ade_detail', 'fonte')

        # Deleting field 'ADE_detail.data_fonte'
        db.delete_column('ade_ade_detail', 'data_fonte')

        # Deleting field 'ADE_detail.sedime_residenza'
        db.delete_column('ade_ade_detail', 'sedime_residenza')

        # Deleting field 'ADE_detail.nome_via_residenza'
        db.delete_column('ade_ade_detail', 'nome_via_residenza')

        # Deleting field 'ADE_detail.civico_residenza'
        db.delete_column('ade_ade_detail', 'civico_residenza')

        # Deleting field 'ADE_detail.ind_norm'
        db.delete_column('ade_ade_detail', 'ind_norm')

        # Deleting field 'ADE_detail.ind_decesso'
        db.delete_column('ade_ade_detail', 'ind_decesso')

        # Deleting field 'ADE_detail.data_decesso'
        db.delete_column('ade_ade_detail', 'data_decesso')

        # Deleting field 'ADE_detail.ind_conf_comune'
        db.delete_column('ade_ade_detail', 'ind_conf_comune')

        # Deleting field 'ADE_detail.nat_giurid'
        db.delete_column('ade_ade_detail', 'nat_giurid')


    models = {
        'ade.ade_detail': {
            'ADE_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ade.ADE_request']"}),
            'CAP_residenza': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'Meta': {'ordering': "['ADE_request', 'cfisc_orig']", 'object_name': 'ADE_detail'},
            'cfisc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cfisc_orig': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
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
            'sesso': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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