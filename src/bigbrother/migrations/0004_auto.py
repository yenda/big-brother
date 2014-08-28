# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field classroom on 'Activity'
        db.delete_table(db.shorten_name(u'bigbrother_activity_classroom'))

        # Adding M2M table for field classrooms on 'Activity'
        m2m_table_name = db.shorten_name(u'bigbrother_activity_classrooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'bigbrother.activity'], null=False)),
            ('classroom', models.ForeignKey(orm[u'bigbrother.classroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'classroom_id'])

        # Adding M2M table for field groups on 'Activity'
        m2m_table_name = db.shorten_name(u'bigbrother_activity_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'bigbrother.activity'], null=False)),
            ('group', models.ForeignKey(orm[u'bigbrother.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'group_id'])

        # Adding M2M table for field teachers on 'Activity'
        m2m_table_name = db.shorten_name(u'bigbrother_activity_teachers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'bigbrother.activity'], null=False)),
            ('teacher', models.ForeignKey(orm[u'bigbrother.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'teacher_id'])


    def backwards(self, orm):
        # Adding M2M table for field classroom on 'Activity'
        m2m_table_name = db.shorten_name(u'bigbrother_activity_classroom')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'bigbrother.activity'], null=False)),
            ('classroom', models.ForeignKey(orm[u'bigbrother.classroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'classroom_id'])

        # Removing M2M table for field classrooms on 'Activity'
        db.delete_table(db.shorten_name(u'bigbrother_activity_classrooms'))

        # Removing M2M table for field groups on 'Activity'
        db.delete_table(db.shorten_name(u'bigbrother_activity_groups'))

        # Removing M2M table for field teachers on 'Activity'
        db.delete_table(db.shorten_name(u'bigbrother_activity_teachers'))


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
            'classrooms': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Classroom']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Teacher']"}),
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