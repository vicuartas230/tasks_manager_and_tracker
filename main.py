import argparse
from tasks.task_manager import TaskManager


def main():
    manager = TaskManager()
    
    parser = argparse.ArgumentParser(
        description="Task Manager Application",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
