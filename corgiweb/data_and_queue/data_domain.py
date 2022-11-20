import uuid
from django.core.management import call_command
from corgiweb.data_and_queue.Data.settings.config import *
from corgiweb.data_and_queue.Data.crawler.views import *


class DataAccess:

    def __init__(self, ):
        self.db = {}

    def start_django(self, ):
        # Make Django migrations
        call_command("makemigrations", "crawler")
        call_command("migrate", "crawler")

    def save_data_on_partitions(self, partition_name, url):
        # Create partition or find existing partition
        self.db[str(partition_name)] = find_partition_and_model(str(partition_name))
        item = self.db[str(partition_name)](
            id=str(int(uuid.uuid4()))[:10],
            partition=str(partition_name),
            url=url)
        item.save()

    def print_all_partitions(self, ):
        for k, v in self.db.items():
            urls = v.objects.all()

            print("partition", k)
            for url in urls:
                print(url.url)


# if __name__ == "__main__":
#     data = Data()
#
#     data.start_django()
#
#     for x in range(0, 3):
#         data.create_partitions(x)
#
#     data.print_all_partitions()
