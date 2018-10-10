from django.urls import include, path

from rest_framework import routers

from .views import datasources as datasource_views

app_name = 'api'

# Register ViewSets
router = routers.DefaultRouter()
router.register('datasources', datasource_views.DataSourceApiViewset)
router.register('datasources', datasource_views.DataSourceMetadataApiView)
router.register('datasources', datasource_views.DataSourceDataApiView)
router.register('datasources', datasource_views.DataSourceDataSetsListApiView)

urlpatterns = [
    path('',
         include(router.urls)),

    path('datasources/<int:pk>/datasets/<str:href>/metadata/',
         datasource_views.DataSourceDatasetMetadataApiView.as_view({
             'get': 'metadata',
         }),
         name='datasources-datasets-metadata')
]
