def authorized_use_check() -> bool:
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