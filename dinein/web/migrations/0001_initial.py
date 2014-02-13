# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'web_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'web', ['Ingredient'])

        # Adding model 'RecipeIngredient'
        db.create_table(u'web_recipeingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Ingredient'])),
            ('quantity', self.gf('django.db.models.fields.CharField')(default='1', max_length=20)),
        ))
        db.send_create_signal(u'web', ['RecipeIngredient'])

        # Adding model 'Recipe'
        db.create_table(u'web_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        m2m_table_name = db.shorten_name(u'web_recipe_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'web.recipe'], null=False)),
            ('recipeingredient', models.ForeignKey(orm[u'web.recipeingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'recipeingredient_id'])

        # Adding model 'UserRecipes'
        db.create_table(u'web_userrecipes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'web', ['UserRecipes'])

        # Adding M2M table for field recipes on 'UserRecipes'
        m2m_table_name = db.shorten_name(u'web_userrecipes_recipes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userrecipes', models.ForeignKey(orm[u'web.userrecipes'], null=False)),
            ('recipe', models.ForeignKey(orm[u'web.recipe'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userrecipes_id', 'recipe_id'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'web_ingredient')

        # Deleting model 'RecipeIngredient'
        db.delete_table(u'web_recipeingredient')

        # Deleting model 'Recipe'
        db.delete_table(u'web_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table(db.shorten_name(u'web_recipe_ingredients'))

        # Deleting model 'UserRecipes'
        db.delete_table(u'web_userrecipes')

        # Removing M2M table for field recipes on 'UserRecipes'
        db.delete_table(db.shorten_name(u'web_userrecipes_recipes'))


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
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
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['web.RecipeIngredient']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web.recipeingredient': {
            'Meta': {'object_name': 'RecipeIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Ingredient']"}),
            'quantity': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'})
        },
        u'web.userrecipes': {
            'Meta': {'object_name': 'UserRecipes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['web.Recipe']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['web']