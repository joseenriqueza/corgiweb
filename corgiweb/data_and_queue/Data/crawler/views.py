#https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables


from django.db import connection

from .models import websites_partition_model

cursor = connection.cursor()

def db_table_exists(db_table):
    return db_table in connection.introspection.table_names()

def get_or_create_table(model,db_table,partition):
    db_table_partition = db_table.replace("default", str(partition))
    model._meta.db_table = db_table_partition
    if not db_table_exists(db_table_partition):
        cursor.execute("CREATE TABLE " + db_table_partition + " AS SELECT * from " + db_table)

def find_partition_and_model(key):
    model = websites_partition_model(key)
    get_or_create_table(model,'crawler_websites_default', str(key).lower())
    return model

