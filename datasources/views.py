from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from profiles.permissions import OwnerPermissionRequiredMixin
from datasources import models


class DataSourceListView(ListView):
    model = models.DataSource
    template_name = 'datasources/datasource/list.html'
    context_object_name = 'datasources'


class DataSourceDetailView(DetailView):
    model = models.DataSource
    template_name = 'datasources/datasource/detail.html'
    context_object_name = 'datasource'

    def get_template_names(self):
        if not self.object.has_view_permission(self.request.user):
            return ['datasources/datasource/detail-no-access.html']
        return super().get_template_names()


class DataSourceManageAccessView(OwnerPermissionRequiredMixin, DetailView):
    model = models.DataSource
    template_name = 'datasources/datasource/manage_access.html'
    context_object_name = 'datasource'

    permission_required = 'datasources.change_datasource'


class DataSourceQueryView(DetailView):
    model = models.DataSource
    template_name = 'datasources/datasource/query.html'
    context_object_name = 'datasource'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['results'] = self.object.data_connector.get_data(
            query_params={'year': 2018}
        )

        return context


class DataSourceMetadataView(DetailView):
    model = models.DataSource
    template_name = 'datasources/datasource/metadata.html'
    context_object_name = 'datasource'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Using data connector context manager saves API queries
        with self.object.data_connector as dc:
            context['metadata'] = dc.get_metadata()
            context['datasets'] = {
                dataset: dc.get_metadata(dataset)
                for dataset in dc.get_datasets()
            }

        return context