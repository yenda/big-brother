# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'adeweb_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adeweb_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('isGroup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lastUpdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('creation', self.gf('django.db.models.fields.DateTimeField')()),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adeweb.Resource'])),
            ('members', self.gf('django.db.models.fields.related.ForeignKey')(related_name='memberships', to=orm['adeweb.Resource'])),
        ))
        db.send_create_signal(u'adeweb', ['Resource'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'adeweb_resource')


    models = {
        u'adeweb.resource': {
            'Meta': {'object_name': 'Resource'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'creation': ('django.db.models.fields.DateTimeField', [], {}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['adeweb.Resource']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isGroup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastUpdate': ('django.db.models.fields.DateTimeField', [], {}),
            'members': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': u"orm['adeweb.Resource']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['adeweb']