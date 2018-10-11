import json

from rest_framework import serializers

from . import models
from provenance import models as prov_models


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = ['name', 'description', 'url']


class DataSourceProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve PROV records related to a data source.

        :param instance: DataSource object
        :return: PROV records related to the data source
        """
        return {
            # Get all ProvEntry's related to this instance and encode them as JSON
            'prov': [json.loads(record.to_json()) for record in prov_models.ProvWrapper.filter_model_instance(instance)]
        }


class DataSourceMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve metadata via query to data source's API.

        Query parameters will be passed on.

        :param instance: DataSource object
        :return: Metadata returned via data source's API
        """
        data_connector = instance.data_connector

        # Are there any query params to pass on?
        try:
            params = self.context['params']
        except KeyError:
            params = None

        return data_connector.get_metadata(params=params)


class DataSourceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve data via query to data source's API.

        Query parameters will be passed on.

        :param instance: DataSource object
        :return: Data returned via data source's API
        """
        data_connector = instance.data_connector

        # Are there any query params to pass on?
        try:
            params = self.context['params']
        except KeyError:
            params = None

        return data_connector.get_data(params=params)


class DataSourceDataSetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve list of data sets via query to data source's API.

        Query parameters will be passed on.

        :param instance: DataSource object
        :return: List of data sets returned via data source's API
        """
        data_connector = instance.data_connector

        # Are there any query params to pass on?
        try:
            params = self.context['params']
        except KeyError:
            params = None

        return data_connector.get_datasets(params=params)


class DataSourceDatasetMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve metadata via query to data source's API.

        Query parameters will be passed on.

        :param instance: DataSource object
        :return: Metadata returned via data source's API
        """
        data_connector = instance.data_connector

        # Are there any query params to pass on?
        try:
            params = self.context['params']
        except KeyError:
            params = None

        return data_connector.get_metadata(dataset=self.context['href'],
                                           params=params)


class DataSourceDatasetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = []

    def to_representation(self, instance: models.DataSource):
        """
        Retrieve data via query to data source's API.

        Query parameters will be passed on.

        :param instance: DataSource object
        :return: Data returned via data source's API
        """
        data_connector = instance.data_connector

        # Are there any query params to pass on?
        try:
            params = self.context['params']
        except KeyError:
            params = None

        data = data_connector.get_data(dataset=self.context['href'],
                                       params=params)

        return {
            'data': data
        }
