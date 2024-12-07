class Task:
    def __init__(self, name: str):
        self.name = name

    def execute(self) -> None:
        """Execute the task."""
        raise NotImplementedError("Subclasses must implement the execute method.")

class ScriptTask(Task):
    def __init__(self, name: str, script_path: str):
        super().__init__(name)
        self.script_path = script_path

    def execute(self) -> None:
        """Execute a script (Python or Bash)."""
        print(f"Executing script task: {self.name} at {self.script_path}")
        ...

class CommandTask(Task):
    def __init__(self, name: str, command: str):
        super().__init__(name)
        self.command = command

    def execute(self) -> None:
        """Execute a shell command."""
        print(f"Executing command task: {self.name} with command '{self.command}'")
