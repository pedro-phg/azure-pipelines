from azure_pipelines.task import Task

class Job:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a task to the job."""
        self.tasks.append(task)

    def run(self) -> None:
        """Run all tasks in the job."""
        print(f"Running job: {self.name}")
        for task in self.tasks:
            task.execute()
