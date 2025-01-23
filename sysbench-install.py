import os
import subprocess

def install_dependencies():
    """Install required dependencies (Development Tools, cmake, and git)."""
    print("Installing required dependencies...")
    try:
        subprocess.run(["yum", "groupinstall", "Development Tools", "-y"], check=True)
        subprocess.run(["yum", "install", "cmake", "git", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        exit(1)

def install_sysbench():
    """Download and install Sysbench from source."""
    sysbench_dir = "/opt/sysbench"
    
    # Create /opt/sysbench directory if it does not exist
    if not os.path.exists(sysbench_dir):
        os.makedirs(sysbench_dir)

    print("Cloning Sysbench repository from GitHub...")
    try:
        subprocess.run(["git", "clone", "https://github.com/akopytov/sysbench.git", sysbench_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning Sysbench repository: {e}")
        exit(1)
    
    print("Building Sysbench...")
    try:
        subprocess.run(["cmake", ".", "-B", "build"], cwd=sysbench_dir, check=True)
        subprocess.run(["make", "-C", "build"], check=True)
        subprocess.run(["make", "install", "-C", "build"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building Sysbench: {e}")
        exit(1)

def verify_installation():
    """Verify the Sysbench installation."""
    print("Verifying Sysbench installation...")
    try:
        result = subprocess.run(["sysbench", "--version"], capture_output=True, check=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error verifying Sysbench installation: {e}")
        exit(1)

if __name__ == "__main__":
    install_dependencies()
    install_sysbench()
    verify_installation()
    print("Sysbench installation completed successfully!")
