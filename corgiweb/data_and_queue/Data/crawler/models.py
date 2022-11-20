# https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables
# https://baserow.io/blog/how-baserow-lets-users-generate-django-models
# https://dev.to/redhap/dynamically-create-orm-models-for-individual-table-partitions-416n
from django.db import models
from django.db.models.base import ModelBase


class websites_default(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    partition = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


def websites_partition_model(db_table):
    class CustomMetaClass(ModelBase):
        def __new__(cls, name, bases, attrs):
            model = super(CustomMetaClass, cls).__new__(cls, name, bases, attrs)
            model._meta.db_table = db_table
            return model

    class websites(models.Model):
        __metaclass__ = CustomMetaClass

        # define your fileds here
        id = models.AutoField(primary_key=True, db_column='id')
        partition = models.CharField(max_length=100)
        url = models.CharField(max_length=100)

    return websites
