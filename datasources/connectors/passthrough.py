import typing

from datasources.connectors.base import DataSetConnector


class HyperCatDataSetConnector(DataSetConnector):
    """
    Data connector for retrieving data from a source contained within a HyperCat catalogue.

    Metadata is assumed to be given by the parent catalogue.
    """
    def __init__(self, location: str,
                 api_key: typing.Optional[str] = None,
                 auth: typing.Optional[typing.Callable] = None,
                 metadata: typing.Optional[typing.Mapping] = None):
        super().__init__(location, api_key, auth=auth)

        self._metadata = metadata

    def get_metadata(self,
                     params: typing.Optional[typing.Mapping[str, str]] = None):
        """
        Retrieve the metadata for this source.

        The metadata must have been given when this data source was looked up in the
        parent catalogue.

        :param params: Ignored
        :return: Data source metadata
        """
        if self._metadata is None:
            raise NotImplementedError

        return self._metadata

    def get_data(self,
                 params: typing.Optional[typing.Mapping[str, str]] = None) -> typing.Union[str, dict]:
        """
        Retrieve the data from this source.

        If the data is JSON formatted it will be parsed into a dictionary - otherwise it will
        be passed as plain text.

        :param params: Query parameters to be passed through to the data source API
        :return: Data source data
        """
        response = self.get_response(params)

        if 'json' in response.headers['Content-Type']:
            return response.json()

        return response.text
