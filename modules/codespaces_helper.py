import shutil
import subprocess


def _gh_installed():
    return shutil.which("gh") is not None


def _run_gh(*args):
    try:
        result = subprocess.run(
            ["gh"] + list(args),
            capture_output=True,
            text=True,
        )
        if result.stdout:
            print(result.stdout.rstrip())
        if result.returncode != 0 and result.stderr:
            print(result.stderr.rstrip())
        return result.returncode == 0
    except FileNotFoundError:
        print("Unexpected error: GitHub CLI (gh) was not found.")
        return False


def run_codespaces_helper():
    print("\n[GitHub Codespaces Helper]")

    if not _gh_installed():
        print("GitHub CLI (gh) is not installed.")
        print("Install it from: https://cli.github.com/")
        return

    print("1. Check authentication status")
    print("2. List codespaces")
    print("3. Create a codespace")
    print("4. Delete a codespace")
    print("5. Back")

    choice = input("\nChoose an option (1-5): ").strip()

    if choice == "1":
        print("\n[Authentication Status]")
        _run_gh("auth", "status")

    elif choice == "2":
        print("\n[Codespace List]")
        _run_gh("codespace", "list")

    elif choice == "3":
        print("\n[Create Codespace]")
        repo = input("Enter repository (owner/repo): ").strip()
        if not repo:
            print("Repository is required.")
            return
        branch = input("Enter branch (leave blank for default): ").strip()
        cmd = ["codespace", "create", "--repo", repo]
        if branch:
            cmd += ["--branch", branch]
        _run_gh(*cmd)

    elif choice == "4":
        print("\n[Delete Codespace]")
        print("Listing codespaces first...")
        _run_gh("codespace", "list")
        codespace_name = input("\nEnter codespace name to delete: ").strip()
        if not codespace_name:
            print("Codespace name is required.")
            return
        confirm = input(f"Delete codespace '{codespace_name}'? (yes/y/no): ").strip().lower()
        if confirm in {"yes", "y"}:
            _run_gh("codespace", "delete", "-c", codespace_name)
        else:
            print("Deletion cancelled.")

    elif choice == "5":
        return

    else:
        print("\nInvalid choice.")
