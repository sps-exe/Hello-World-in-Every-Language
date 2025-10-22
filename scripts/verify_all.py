#!/usr/bin/env python3
import subprocess
import glob
import os
import sys

LANG_MAP = {
    '.py': ('', 'python3 {file}'),
    '.js': ('', 'node {file}'),
    '.c': ('gcc {file} -o {base}', './{base}'),
    '.cpp': ('g++ {file} -o {base}', './{base}'),
    '.java': ('javac {file}', 'java {classname}'),
}

EXPECTED_OUTPUT = "Hello, World!"

def run_command(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def verify_program(path):
    ext = os.path.splitext(path)[1]
    base = os.path.splitext(path)[0]
    classname = os.path.basename(base)
    compile_cmd, run_cmd = LANG_MAP.get(ext, (None, None))
    if not run_cmd:
        print(f"Skipping unsupported file: {path}")
        return True
    if compile_cmd:
        res = run_command(compile_cmd.format(file=path, base=base, classname=classname))
        if res.returncode != 0:
            print(f"❌ Compile failed for {path}\n{res.stderr}")
            return False
    res = run_command(run_cmd.format(file=path, base=base, classname=classname))
    if res.returncode != 0:
        print(f"❌ Execution failed for {path}\n{res.stderr}")
        return False
    output = res.stdout.strip()
    if output == EXPECTED_OUTPUT:
        print(f"✅ Passed: {path}")
        return True
    print(f"❌ Failed: {path}\nExpected: '{EXPECTED_OUTPUT}'\nGot: '{output}'")
    return False

def main():
    files = []
    for ext in LANG_MAP:
        files += glob.glob(f'**/*{ext}', recursive=True)
    failed = [f for f in files if not verify_program(f)]
    if failed:
        print("\n=== Summary ===")
        for f in failed:
            print("❌ " + f)
        sys.exit(1)
    print("\n🎉 All programs passed successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
