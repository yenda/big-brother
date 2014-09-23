# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'calendar_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lecture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['lecture.Lecture'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adeweb_id', self.gf('django.db.models.fields.IntegerField')()),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('report', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calendar', ['Event'])

        # Adding M2M table for field classrooms on 'Event'
        m2m_table_name = db.shorten_name(u'calendar_event_classrooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'calendar.event'], null=False)),
            ('classroom', models.ForeignKey(orm[u'institution.classroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'classroom_id'])

        # Adding M2M table for field memberships on 'Event'
        m2m_table_name = db.shorten_name(u'calendar_event_memberships')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'calendar.event'], null=False)),
            ('membership', models.ForeignKey(orm[u'institution.membership'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'membership_id'])

        # Adding M2M table for field teachers on 'Event'
        m2m_table_name = db.shorten_name(u'calendar_event_teachers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'calendar.event'], null=False)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'calendar_event')

        # Removing M2M table for field classrooms on 'Event'
        db.delete_table(db.shorten_name(u'calendar_event_classrooms'))

        # Removing M2M table for field memberships on 'Event'
        db.delete_table(db.shorten_name(u'calendar_event_memberships'))

        # Removing M2M table for field teachers on 'Event'
        db.delete_table(db.shorten_name(u'calendar_event_teachers'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'calendar.event': {
            'Meta': {'object_name': 'Event'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            'classrooms': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': u"orm['institution.Classroom']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['lecture.Lecture']"}),
            'memberships': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': u"orm['institution.Membership']"}),
            'report': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': u"orm['users.User']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'institution.classroom': {
            'Meta': {'object_name': 'Classroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'institution.membership': {
            'Meta': {'object_name': 'Membership'},
            'adeweb_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'memberships'", 'symmetrical': 'False', 'to': u"orm['users.User']"})
        },
        u'lecture.lecture': {
            'Meta': {'object_name': 'Lecture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.User']", 'through': u"orm['lecture.Teacher']", 'symmetrical': 'False'})
        },
        u'lecture.teacher': {
            'Meta': {'object_name': 'Teacher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lecture.Lecture']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'adeweb_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['calendar']