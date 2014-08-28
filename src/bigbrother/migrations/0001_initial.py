# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Classroom'
        db.create_table(u'bigbrother_classroom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Classroom'])

        # Adding model 'Teacher'
        db.create_table(u'bigbrother_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('adeweb_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bigbrother', ['Teacher'])

        # Adding model 'Group'
        db.create_table(u'bigbrother_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bigbrother', ['Group'])

        # Adding model 'Student'
        db.create_table(u'bigbrother_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('adeweb_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bigbrother', ['Student'])

        # Adding M2M table for field groups on 'Student'
        m2m_table_name = db.shorten_name(u'bigbrother_student_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'bigbrother.student'], null=False)),
            ('group', models.ForeignKey(orm[u'bigbrother.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'group_id'])

        # Adding model 'Activity'
        db.create_table(u'bigbrother_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'bigbrother', ['Activity'])

        # Adding model 'Event'
        db.create_table(u'bigbrother_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['bigbrother.Activity'])),
            ('adeweb_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'bigbrother', ['Event'])

        # Adding M2M table for field classrooms on 'Event'
        m2m_table_name = db.shorten_name(u'bigbrother_event_classrooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'bigbrother.event'], null=False)),
            ('classroom', models.ForeignKey(orm[u'bigbrother.classroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'classroom_id'])

        # Adding M2M table for field groups on 'Event'
        m2m_table_name = db.shorten_name(u'bigbrother_event_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'bigbrother.event'], null=False)),
            ('group', models.ForeignKey(orm[u'bigbrother.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'group_id'])

        # Adding M2M table for field teachers on 'Event'
        m2m_table_name = db.shorten_name(u'bigbrother_event_teachers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'bigbrother.event'], null=False)),
            ('teacher', models.ForeignKey(orm[u'bigbrother.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'teacher_id'])

        # Adding model 'Absence'
        db.create_table(u'bigbrother_absence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='absences', to=orm['bigbrother.Activity'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='absences', to=orm['bigbrother.Student'])),
            ('excuse', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bigbrother', ['Absence'])


    def backwards(self, orm):
        # Deleting model 'Classroom'
        db.delete_table(u'bigbrother_classroom')

        # Deleting model 'Teacher'
        db.delete_table(u'bigbrother_teacher')

        # Deleting model 'Group'
        db.delete_table(u'bigbrother_group')

        # Deleting model 'Student'
        db.delete_table(u'bigbrother_student')

        # Removing M2M table for field groups on 'Student'
        db.delete_table(db.shorten_name(u'bigbrother_student_groups'))

        # Deleting model 'Activity'
        db.delete_table(u'bigbrother_activity')

        # Deleting model 'Event'
        db.delete_table(u'bigbrother_event')

        # Removing M2M table for field classrooms on 'Event'
        db.delete_table(db.shorten_name(u'bigbrother_event_classrooms'))

        # Removing M2M table for field groups on 'Event'
        db.delete_table(db.shorten_name(u'bigbrother_event_groups'))

        # Removing M2M table for field teachers on 'Event'
        db.delete_table(db.shorten_name(u'bigbrother_event_teachers'))

        # Deleting model 'Absence'
        db.delete_table(u'bigbrother_absence')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.student': {
            'Meta': {'object_name': 'Student'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'students'", 'symmetrical': 'False', 'to': u"orm['bigbrother.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bigbrother.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bigbrother']