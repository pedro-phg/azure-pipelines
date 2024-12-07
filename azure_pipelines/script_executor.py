import subprocess

class ScriptExecutor:
    @staticmethod
    def execute_python(script_path: str) -> None:
        """Execute a Python script."""
        print(f"Executing Python script: {script_path}")
        subprocess.run(["python", script_path], check=True)

    @staticmethod
    def execute_bash(script_path: str) -> None:
        """Execute a Bash script."""
        print(f"Executing Bash script: {script_path}")
        subprocess.run(["bash", script_path], check=True)
