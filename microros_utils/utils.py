import subprocess

def run_cmd(command, env=None):
    print("version")
    print(sys.version)
    print("---")
    return subprocess.run(command,
        capture_output = True,
        shell = True,
        env=env
    )
