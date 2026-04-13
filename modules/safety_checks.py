"""
Safety and authorization checks module for the Wireless Toolkit.

Ensures the user confirms they are operating in an approved environment
before proceeding with any wireless assessment activities.
"""


def authorized_use_check() -> bool:
    """Prompt the user to confirm they are working in an authorized environment.

    Presents a numbered list of environment types and asks the user to
    select the one that matches their current context.  The function
    returns ``True`` only when the user selects a recognized, approved
    environment (options 1–4).

    Environment options:
        1. My own lab
        2. Company-approved environment
        3. Client-approved environment
        4. Training lab or sandbox
        5. I am not sure (returns ``False``)

    Returns:
        bool: ``True`` if the user confirms an approved environment,
        ``False`` otherwise.

    Example::

        >>> approved = authorized_use_check()
        [Authorization Check]
        Choose the environment type:
        ...
        >>> if approved:
        ...     print("Proceeding with assessment.")
    """
    print("\n[Authorization Check]")
    print("Choose the environment type:")
    print("1. My own lab")
    print("2. Company-approved environment")
    print("3. Client-approved environment")
    print("4. Training lab or sandbox")
    print("5. I am not sure")

    choice = input("\nChoose an option (1-5): ").strip()

    if choice in {"1", "2", "3", "4"}:
        print("\nAuthorization reminder accepted.")
        return True

    print("\nApproval not confirmed. Stop and verify first.")
    return False