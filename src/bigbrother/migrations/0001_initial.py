# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'bigbrother_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('activity_id', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('classroom', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Activity'])

        # Adding model 'Teacher'
        db.create_table(u'bigbrother_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('teacher_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bigbrother', ['Teacher'])

        # Adding model 'Groups'
        db.create_table(u'bigbrother_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Groups'])

        # Adding model 'Student'
        db.create_table(u'bigbrother_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('student_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bigbrother', ['Student'])

        # Adding M2M table for field groups on 'Student'
        m2m_table_name = db.shorten_name(u'bigbrother_student_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'bigbrother.student'], null=False)),
            ('groups', models.ForeignKey(orm[u'bigbrother.groups'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'groups_id'])

        # Adding model 'Absences'
        db.create_table(u'bigbrother_absences', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigbrother.Activity'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigbrother.Student'])),
            ('excuse', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bigbrother', ['Absences'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'bigbrother_activity')

        # Deleting model 'Teacher'
        db.delete_table(u'bigbrother_teacher')

        # Deleting model 'Groups'
        db.delete_table(u'bigbrother_groups')

        # Deleting model 'Student'
        db.delete_table(u'bigbrother_student')

        # Removing M2M table for field groups on 'Student'
        db.delete_table(db.shorten_name(u'bigbrother_student_groups'))

        # Deleting model 'Absences'
        db.delete_table(u'bigbrother_absences')


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
        u'bigbrother.groups': {
            'Meta': {'object_name': 'Groups'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.student': {
            'Meta': {'object_name': 'Student'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bigbrother.Groups']", 'symmetrical': 'False'}),
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