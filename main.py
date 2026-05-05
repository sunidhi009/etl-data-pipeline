import subprocess

def run_script(script_name):
    try:
        print(f"\nRunning {script_name}...")
        result = subprocess.run(["python", script_name], check=True)
        print(f"{script_name} completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}: {e}")
        exit()

# Run ETL steps
run_script("extract.py")
run_script("transform.py")
run_script("load.py")

print("\nETL Pipeline executed successfully!")