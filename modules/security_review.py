def run_security_review():
    print("\n[Security Review]")
    print("Choose what you want to review:")
    print("1. Secrets handling")
    print("2. Input handling")
    print("3. Error handling")
    print("4. Authentication / authorization reminders")
    print("5. Dependency and update reminders")
    print("6. Back")

    choice = input("\nChoose an option (1-6): ").strip()

    if choice == "1":
        print("\nReview:")
        print("- Do not hardcode secrets, passwords, or tokens.")
        print("- Use environment variables for sensitive values.")
        print("- Confirm sensitive values are not committed to source control.")

    elif choice == "2":
        print("\nReview:")
        print("- Validate user input before using it.")
        print("- Use allow-lists where possible.")
        print("- Do not trust filenames, form fields, or uploaded content.")

    elif choice == "3":
        print("\nReview:")
        print("- Do not expose stack traces or internal details to users.")
        print("- Keep user-facing errors simple.")
        print("- Log only what is necessary and avoid sensitive data.")

    elif choice == "4":
        print("\nReview:")
        print("- Confirm access checks exist before sensitive actions.")
        print("- Do not assume a logged-in user is automatically authorized.")
        print("- Review whether role checks and scope checks are clear.")

    elif choice == "5":
        print("\nReview:")
        print("- Keep dependencies updated.")
        print("- Check for known vulnerable packages.")
        print("- Remove unused packages where possible.")

    elif choice == "6":
        return

    else:
        print("\nInvalid choice.")
