
"""
Module: shopapp.mixins
This module defines mixins for exporting data as CSV format.
"""

from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse
import csv

class ExportAsCSVMixin:
    """
    Mixin to export queryset data as CSV format.
    """
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        """
        Export the queryset data as CSV format.

        Args:
            request (HttpRequest): The HTTP request object.
            queryset (QuerySet): The queryset to export.

        Returns:
            HttpResponse: The HTTP response with CSV data.
        """
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'

        csv_writer = csv.writer(response)

        csv_writer.writerow(field_names)

        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv.short_description = 'Export as CSV'
