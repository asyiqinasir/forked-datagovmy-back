from django.core.management.base import BaseCommand
from data_catalogue.models import (
    DataCatalogue,
    DataCatalogueMeta,
    Dataviz,
    Field,
    RelatedDataset,
    SiteCategory,
)


class Command(BaseCommand):
    help = "Delete all entries in the DataCatalogue model"

    def handle(self, *args, **kwargs):
        DataCatalogue.objects.all().delete()
        self.stdout.write("Deleted DataCatalogue entries.")

        DataCatalogueMeta.objects.all().delete()
        self.stdout.write("Deleted DataCatalogueMeta entries.")

        Dataviz.objects.all().delete()
        self.stdout.write("Deleted Dataviz entries.")

        Field.objects.all().delete()
        self.stdout.write("Deleted Field entries.")

        RelatedDataset.objects.all().delete()
        self.stdout.write("Deleted RelatedDataset entries.")

        SiteCategory.objects.all().delete()
        self.stdout.write("Deleted SiteCategory entries.")

        self.stdout.write(self.style.SUCCESS("Successfully deleted all."))
