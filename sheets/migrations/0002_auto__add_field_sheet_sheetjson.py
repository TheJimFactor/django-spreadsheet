# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sheet.sheetjson'
        db.add_column(u'sheets_sheet', 'sheetjson',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sheet.sheetjson'
        db.delete_column(u'sheets_sheet', 'sheetjson')


    models = {
        u'sheets.sheet': {
            'Meta': {'object_name': 'Sheet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sheetjson': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['sheets']