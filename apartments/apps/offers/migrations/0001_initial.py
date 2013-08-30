# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Offers'
        db.create_table(u'offers_offers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('tinymce.models.HTMLField')()),
            ('text_pl', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_de', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_ru', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'offers', ['Offers'])

        # Adding model 'Offer'
        db.create_table(u'offers_offer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('offers', self.gf('adminsortable.fields.SortableForeignKey')(related_name='offers', to=orm['offers.Offers'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('price_pl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price_ru', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('imageField', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('text', self.gf('tinymce.models.HTMLField')()),
            ('text_pl', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_de', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_ru', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'offers', ['Offer'])


    def backwards(self, orm):
        # Deleting model 'Offers'
        db.delete_table(u'offers_offers')

        # Deleting model 'Offer'
        db.delete_table(u'offers_offer')


    models = {
        u'offers.offer': {
            'Meta': {'ordering': "['order']", 'object_name': 'Offer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageField': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'offers': ('adminsortable.fields.SortableForeignKey', [], {'related_name': "'offers'", 'to': u"orm['offers.Offers']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'price_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price_pl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'text_de': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_pl': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'offers.offers': {
            'Meta': {'ordering': "['order']", 'object_name': 'Offers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'text_de': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_pl': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['offers']