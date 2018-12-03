import csv

from django.contrib import admin
from django.http import HttpResponse

from . import models


class ExportCSV:
    def exportCSV(self, request, querySet):
        meta = self.model._meta
        fieldNames = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(fieldNames)
        for obj in querySet:
            writer.writerow([getattr(obj, field) for field in fieldNames])

        return response


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin, ExportCSV):
    actions = ["exportCSV"]
