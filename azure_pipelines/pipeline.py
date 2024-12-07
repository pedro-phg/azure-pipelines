from azure_pipelines.stage import Stage

class Pipeline:
    def __init__(self, name: str):
        self.name = name
        self.stages = []

    def add_stage(self, stage: Stage) -> None:
        """Add a stage to the pipeline."""
        self.stages.append(stage)

    def to_yaml(self) -> str:
        """Export the pipeline to a YAML string."""
        # Logic to convert the pipeline to YAML
        return "YAML representation of the pipeline"

    def execute(self) -> None:
        """Simulate the pipeline execution."""
        print(f"Executing pipeline: {self.name}")
        for stage in self.stages:
            stage.run()
