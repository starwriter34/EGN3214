from django.contrib import admin
from django.http import request
from import_export.admin import ImportExportModelAdmin
from .models import MachineStatus, PermanentRecords, MachineDownReports
# Register your models here.

class MachineStatusAdmin(ImportExportModelAdmin):
    list_display=['machine_name', 'machine_e2name', 'machine_row', 'status','downtime']
    list_filter = ['status',]
    ordering = ['status', '-downtime']
class MachineDownReportsAdmin(ImportExportModelAdmin):
    list_display=['__str__', 'starttime', 'endtime', 'status','total']
    list_filter = ['status',]
    ordering = ['status',]

class PermanentRecordsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super(PermanentRecordsAdmin, self).get_queryset(request)
        queryset = queryset.prefetch_related('machine_names')
        return queryset

admin.site.register(MachineStatus, MachineStatusAdmin)
admin.site.register(PermanentRecords)
admin.site.register(MachineDownReports, MachineDownReportsAdmin)