# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Absences'
        db.delete_table(u'bigbrother_absences')

        # Adding model 'Classroom'
        db.create_table(u'bigbrother_classroom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Classroom'])

        # Adding model 'Absence'
        db.create_table(u'bigbrother_absence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='absences', to=orm['bigbrother.Activity'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='absences', to=orm['bigbrother.Student'])),
            ('excuse', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bigbrother', ['Absence'])

        # Deleting field 'Activity.classroom'
        db.delete_column(u'bigbrother_activity', 'classroom')

        # Adding M2M table for field classroom on 'Activity'
        m2m_table_name = db.shorten_name(u'bigbrother_activity_classroom')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'bigbrother.activity'], null=False)),
            ('classroom', models.ForeignKey(orm[u'bigbrother.classroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'classroom_id'])


    def backwards(self, orm):
        # Adding model 'Absences'
        db.create_table(u'bigbrother_absences', (
            ('excuse', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigbrother.Student'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigbrother.Activity'])),
        ))
        db.send_create_signal(u'bigbrother', ['Absences'])

        # Deleting model 'Classroom'
        db.delete_table(u'bigbrother_classroom')

        # Deleting model 'Absence'
        db.delete_table(u'bigbrother_absence')


        # User chose to not deal with backwards NULL issues for 'Activity.classroom'
        raise RuntimeError("Cannot reverse this migration. 'Activity.classroom' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Activity.classroom'
        db.add_column(u'bigbrother_activity', 'classroom',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Removing M2M table for field classroom on 'Activity'
        db.delete_table(db.shorten_name(u'bigbrother_activity_classroom'))


    models = {
        u'bigbrother.absence': {
            'Meta': {'object_name': 'Absence'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'absences'", 'to': u"orm['bigbrother.Activity']"}),
            'excuse': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'absences'", 'to': u"orm['bigbrother.Student']"})
        },
        u'bigbrother.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_id': ('django.db.models.fields.IntegerField', [], {}),
            'classroom': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Classroom']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bigbrother.classroom': {
            'Meta': {'object_name': 'Classroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.student': {
            'Meta': {'object_name': 'Student'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'students'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Group']"}),
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