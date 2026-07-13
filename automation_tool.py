"""
🟨 Micro Automation Tool
A simple Python tool that runs small, repeatable automation tasks.
Useful for workflow automation, evaluation pipelines, and micro‑task operations.

Part of the Catatonix AI Evaluation Toolkit.
Author: Thomas Moore (Catatonix)
"""

import sys
import time
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "automation.log"

def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.write_text(LOG_FILE.read_text() + line + "\n" if LOG_FILE.exists() else line + "\n")

def task_hello():
    log("Hello from micro-automation-tool!")

def task_health_check():
    log("Running health check...")
    log("All systems nominal.")

TASKS = {
    "hello": task_hello,
    "health_check": task_health_check,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python automation_tool.py [list|run <task_name>]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "list":
        print("Available tasks:")
        for t in TASKS: print(" -", t)
    elif cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: python automation_tool.py run <task_name>")
            sys.exit(1)
        TASKS.get(sys.argv[2], lambda: print("Unknown task"))()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
