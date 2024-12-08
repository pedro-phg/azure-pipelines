from enum import Enum

class Pool(Enum):
    DEFAULT = 'Default'
    AZURE_PIPELINES = 'Azure Pipelines'
    HOSTED_VS2017 = 'Hosted VS2017'

class Condition(Enum):
    SUCCEEDED = "succeeded()"
    FAILED = "failed()"
    ALWAYS = "always()"
    CUSTOM = "custom"
