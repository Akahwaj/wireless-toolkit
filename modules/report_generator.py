from datetime import datetime

def generate_report():
    print("\n[Report Generator]")
    project_name = input("Enter project name: ").strip()
    assessor = input("Enter your name: ").strip()

    print("\nReport")
    print("=" * 25)
    print(f"Project: {project_name}")
    print(f"Assessor: {assessor}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Summary: Wireless review completed.")