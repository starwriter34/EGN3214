from django.urls import path
from .views import (
    MachineStatusCharts,
    MachineStatusList,
    MachineStatusUpdate,
    MachineStatusCreate,
    MachineStatusDetail,
    PermanentRecordsCreate,
    PermanentRecordsUpdate,
    PermanentRecordsList,
    PermanentRecordsDelete,
    MachineDownReportsList,
    MachineDownReportsUpdate,
    MachineDownReportsDelete,
    MachineDownReportsCreate,
    # MachineDownReportDetail,
    )

from . import views

urlpatterns = [
    path('mm/', MachineStatusList.as_view(), name='machinestatuslist'),
    path('mm/delete/<int:pk>/', PermanentRecordsDelete.as_view(), name='permanentrecord-delete'),
    path('mm/update/<int:pk>/', MachineStatusUpdate.as_view(), name='machinestatusupdate'),
    path('mm/create/', MachineStatusCreate.as_view(), name='machinestatuscreate'),
    path('mm/detail/<int:pk>/', MachineStatusDetail.as_view(), name='machinestatusdetail'),
    path('mm/<path:operation>/<int:pk>/', views.MachineStatusOperations, name='machinestatus-operation'),
    path('mm/<int:pk>/prcreate/', PermanentRecordsCreate.as_view(), name='permanentrecord-create'),
    path('mm/<int:pk>/prupdate/', PermanentRecordsUpdate.as_view(), name='permanentrecord-update'),
    path('mm/<int:pk>/repairaction/', PermanentRecordsList.as_view(), name='permanentrecord-list'),
    path('mm/<int:pk>/downreports/', MachineDownReportsList.as_view(), name='machinedownreport-list'),
    path('mm/<int:pk>/downreports-create/', MachineDownReportsCreate.as_view(), name='machinedownreport-create'),
    path('mm/<int:pk>/downreports-update/', MachineDownReportsUpdate.as_view(), name='machinedownreport_update'),
    path('mm/<int:pk>/downreports-delete/', MachineDownReportsDelete.as_view(), name='machinedownreport_delete'),

####################################################################################################
#                                       Reporting Views
####################################################################################################
####################################################################################################
#                                            Chart
####################################################################################################
    path('mm/report/<str:chartType>/', MachineStatusCharts.as_view(), name='mmaint-charts'),


]