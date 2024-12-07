from azure_pipelines.job import Job

class Stage:
    def __init__(self, name: str):
        self.name = name
        self.jobs = []

    def add_job(self, job: Job) -> None:
        """Add a job to the stage."""
        self.jobs.append(job)

    def run(self) -> None:
        """Run all jobs in the stage."""
        print(f"Running stage: {self.name}")
        for job in self.jobs:
            job.run()
