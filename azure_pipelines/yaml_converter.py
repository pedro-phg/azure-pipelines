import yaml
from azure_pipelines.pipeline import Pipeline
from azure_pipelines.stage import Stage
from azure_pipelines.job import Job
from azure_pipelines.task import Task

class YAMLConverter:
    @staticmethod
    def from_yaml(yaml_path: str) -> Pipeline:
        """Convert a YAML file to a Pipeline object."""
        with open(yaml_path, 'r') as file:
            data = yaml.safe_load(file)

        pipeline = Pipeline(name=data['name'])

        return pipeline
