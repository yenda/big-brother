# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Groups'
        db.delete_table(u'bigbrother_groups')

        # Adding model 'Group'
        db.create_table(u'bigbrother_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Group'])


    def backwards(self, orm):
        # Adding model 'Groups'
        db.create_table(u'bigbrother_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Groups'])

        # Deleting model 'Group'
        db.delete_table(u'bigbrother_group')


    models = {
        u'bigbrother.absences': {
            'Meta': {'object_name': 'Absences'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigbrother.Activity']"}),
            'excuse': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigbrother.Student']"})
        },
        u'bigbrother.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_id': ('django.db.models.fields.IntegerField', [], {}),
            'classroom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bigbrother.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.student': {
            'Meta': {'object_name': 'Student'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bigbrother.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'bigbrother.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacher_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['bigbrother']