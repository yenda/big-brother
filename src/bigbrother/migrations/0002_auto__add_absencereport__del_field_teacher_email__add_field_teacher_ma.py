# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AbsenceReport'
        db.create_table(u'bigbrother_absencereport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='absence_reports', to=orm['bigbrother.Activity'])),
        ))
        db.send_create_signal(u'bigbrother', ['AbsenceReport'])

        # Adding M2M table for field students on 'AbsenceReport'
        m2m_table_name = db.shorten_name(u'bigbrother_absencereport_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('absencereport', models.ForeignKey(orm[u'bigbrother.absencereport'], null=False)),
            ('student', models.ForeignKey(orm[u'bigbrother.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['absencereport_id', 'student_id'])

        # Deleting field 'Teacher.email'
        db.delete_column(u'bigbrother_teacher', 'email')

        # Adding field 'Teacher.mail'
        db.add_column(u'bigbrother_teacher', 'mail',
                      self.gf('django.db.models.fields.CharField')(default='yenda1@gmail.com', max_length=100),
                      keep_default=False)

        # Adding M2M table for field students on 'Group'
        m2m_table_name = db.shorten_name(u'bigbrother_group_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'bigbrother.group'], null=False)),
            ('student', models.ForeignKey(orm[u'bigbrother.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'student_id'])

        # Adding field 'Student.mail'
        db.add_column(u'bigbrother_student', 'mail',
                      self.gf('django.db.models.fields.CharField')(default='yenda1@gmail.com', max_length=100),
                      keep_default=False)

        # Removing M2M table for field groups on 'Student'
        db.delete_table(db.shorten_name(u'bigbrother_student_groups'))


    def backwards(self, orm):
        # Deleting model 'AbsenceReport'
        db.delete_table(u'bigbrother_absencereport')

        # Removing M2M table for field students on 'AbsenceReport'
        db.delete_table(db.shorten_name(u'bigbrother_absencereport_students'))


        # User chose to not deal with backwards NULL issues for 'Teacher.email'
        raise RuntimeError("Cannot reverse this migration. 'Teacher.email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Teacher.email'
        db.add_column(u'bigbrother_teacher', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75),
                      keep_default=False)

        # Deleting field 'Teacher.mail'
        db.delete_column(u'bigbrother_teacher', 'mail')

        # Removing M2M table for field students on 'Group'
        db.delete_table(db.shorten_name(u'bigbrother_group_students'))

        # Deleting field 'Student.mail'
        db.delete_column(u'bigbrother_student', 'mail')

        # Adding M2M table for field groups on 'Student'
        m2m_table_name = db.shorten_name(u'bigbrother_student_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'bigbrother.student'], null=False)),
            ('group', models.ForeignKey(orm[u'bigbrother.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'group_id'])


    models = {
        u'bigbrother.absence': {
            'Meta': {'object_name': 'Absence'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'absences'", 'to': u"orm['bigbrother.Activity']"}),
            'excuse': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'absences'", 'to': u"orm['bigbrother.Student']"})
        },
        u'bigbrother.absencereport': {
            'Meta': {'object_name': 'AbsenceReport'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'absence_reports'", 'to': u"orm['bigbrother.Activity']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'absence_report'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Student']"})
        },
        u'bigbrother.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bigbrother.classroom': {
            'Meta': {'object_name': 'Classroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.event': {
            'Meta': {'object_name': 'Event'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['bigbrother.Activity']"}),
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            'classrooms': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Classroom']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'activities'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Teacher']"})
        },
        u'bigbrother.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Student']"})
        },
        u'bigbrother.student': {
            'Meta': {'object_name': 'Student'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'default': "'yenda1@gmail.com'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'default': "'yenda1@gmail.com'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bigbrother']