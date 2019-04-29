"""
This module contains classes required to build a data pipeline from a series of data connectors.
"""

import abc
import typing

from core import plugin
from .. import models


class BasePipelineStage(metaclass=plugin.Plugin):
    #: Help string to be shown when a user is building a pipeline
    description = None

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def __call__(self, data: typing.Mapping) -> typing.Mapping:
        raise NotImplementedError


class NullPipelineStage(BasePipelineStage):
    """
    Pipeline stage which does nothing.  For testing purposes.
    """
    #: Help string to be shown when a user is building a pipeline
    description = 'Does nothing'

    def __call__(self, data: typing.Mapping) -> typing.Mapping:
        return data


class JsonValidationPipelineStage(BasePipelineStage):
    """
    Always raises an error.
    """
    #: Help string to be shown when a user is building a pipeline
    description = 'Raise an error'

    def __call__(self, data: typing.Mapping) -> typing.Mapping:
        raise models.pipeline.PipelineValidationError('Data failed validation')
