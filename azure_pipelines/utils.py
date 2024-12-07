def validate_name(name: str) -> bool:
    """Validate that a name is non-empty and alphanumeric."""
    return bool(name and name.isalnum())
