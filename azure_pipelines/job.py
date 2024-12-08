from enum import Enum
from typing import List, Dict, Union


class WorkspaceCleanOptions(Enum):
    OUTPUTS = "outputs"
    RESOURCES = "resources"
    ALL = "all"


class Job:
    def __init__(
        self,
        name: str,
        display_name: str = None,
        depends_on: Union[str, List[str]] = None,
        condition: str = "succeeded()",
        strategy: Dict = None,
        continue_on_error: bool = False,
        pool: str = "Default",
        workspace_clean: WorkspaceCleanOptions = None,
        container: str = None,
        timeout_in_minutes: int = 60,
        cancel_timeout_in_minutes: int = None,
        variables: Union[Dict[str, str], List[Dict[str, str]]] = None,
        steps: List[Dict] = None,
        services: Dict[str, Union[str, Dict]] = None,
        uses: Dict[str, List[str]] = None,
    ):
        """
        Represents a job in an Azure DevOps pipeline.

        Args:
            name (str): Name of the job. Allowed characters: A-Z, a-z, 0-9, and underscore.
            display_name (str): Friendly name to display in the UI.
            depends_on (Union[str, List[str]]): Jobs that this job depends on.
            condition (str): The condition under which this job runs.
            strategy (Dict): Strategy for running the job (parallel or matrix).
            continue_on_error (bool): Whether to continue future jobs if this one fails.
            pool (str): Agent pool to run the job in.
            workspace_clean (WorkspaceCleanOptions): Workspace cleanup options before the job runs.
            container (str): Container to run the job inside.
            timeout_in_minutes (int): Timeout for the job in minutes.
            cancel_timeout_in_minutes (int): Time to wait before canceling a job, in minutes.
            variables (Union[Dict[str, str], List[Dict[str, str]]]): Variables for the job.
            steps (List[Dict]): Steps to execute in the job.
            services (Dict[str, Union[str, Dict]]): Container resources to run as service containers.
            uses (Dict[str, List[str]]): External resources required by the job.
        """
        self.name = name
        self.display_name = display_name
        self.depends_on = depends_on if depends_on else []
        self.condition = condition
        self.strategy = strategy
        self.continue_on_error = continue_on_error
        self.pool = pool
        self.workspace_clean = workspace_clean
        self.container = container
        self.timeout_in_minutes = timeout_in_minutes
        self.cancel_timeout_in_minutes = cancel_timeout_in_minutes
        self.variables = variables if variables else {}
        self.steps = steps if steps else []
        self.services = services if services else {}
        self.uses = uses if uses else {}

        self._validate()

    def _validate(self):
        """Validate job parameters."""
        if not self.name.isidentifier():
            raise ValueError(
                "Job name must contain only alphanumeric characters and underscores."
            )
        if self.strategy:
            if "parallel" in self.strategy and "matrix" in self.strategy:
                raise ValueError(
                    "The 'parallel' and 'matrix' strategies are mutually exclusive."
                )
            if "matrix" in self.strategy and "maxParallel" not in self.strategy:
                raise ValueError(
                    "'maxParallel' must be specified when using the 'matrix' strategy."
                )

    def add_step(self, step: Dict) -> None:
        """Add a step to the job."""
        self.steps.append(step)

    def to_dict(self) -> Dict:
        """Convert the job to a dictionary for YAML serialization."""
        job_dict = {
            "job": self.name,
            "displayName": self.display_name,
            "dependsOn": self.depends_on if self.depends_on else None,
            "condition": self.condition,
            "strategy": self.strategy if self.strategy else None,
            "continueOnError": self.continue_on_error,
            "pool": {"vmImage": self.pool} if self.pool else None,
            "workspace": (
                {"clean": self.workspace_clean.value} if self.workspace_clean else None
            ),
            "container": self.container,
            "timeoutInMinutes": self.timeout_in_minutes,
            "cancelTimeoutInMinutes": self.cancel_timeout_in_minutes,
            "variables": self.variables,
            "steps": self.steps,
            "services": self.services,
            "uses": self.uses,
        }
        # Remove None values for cleaner output
        return {k: v for k, v in job_dict.items() if v is not None}
