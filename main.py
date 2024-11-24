import argparse
from tasks.task_manager import TaskManager
from utils.enums import Priority, Status


def main():
    manager = TaskManager()
    manager.reload()

    parser = argparse.ArgumentParser(
        description="Task Manager Application",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands"
    )

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("name", help="Task name")
    add_parser.add_argument("category", help="Task category")
    add_parser.add_argument("due_date", help="Due date (YYY-MM-DD)")
    add_parser.add_argument(
        "priority",
        help="Task priority (High, Medium, Low)"
    )
    add_parser.add_argument(
        "status",
        default="Pending",
        help="Task status (Pending, In Progress, Completed)"
    )

    update_parser = subparsers.add_parser(
        "update", help="Update an existing task"
    )
    update_parser.add_argument(
        "task_id", type=str, help="ID of the task to update"
    )
    update_parser.add_argument("--name", type=str, help="New task name")
    update_parser.add_argument(
        "--category", type=str, help="New task category"
    )
    update_parser.add_argument(
        "--due_date", type=str, help="New task due_date (YYY-MM-DD)"
    )
    update_parser.add_argument("--priority", type=str, help="New priority")
    update_parser.add_argument("--status", type=str, help="New status")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
        "task_id", type=str, help="ID of the task to delete"
    )

    subparsers.add_parser("view", help="View all tasks")

    filter_parser = subparsers.add_parser(
        "filter", help="Filter tasks by criteria"
    )
    filter_parser.add_argument("--status", help="Filter by status")
    filter_parser.add_argument("--category", help="Filter by category")
    filter_parser.add_argument("--priority", help="Filter by priority")

    sorter_parser = subparsers.add_parser(
        "sort", help="Sort tasks by criteria in either ASC or DES order"
    )
    sort_criteria_group = sorter_parser.add_mutually_exclusive_group()
    sorter_parser.add_argument("--name", action="store_true", help="Order by name")
    sorter_parser.add_argument("--due_date", action="store_true", help="Order by due_date")
    sorter_parser.add_argument("--status", action="store_true", help="Order by status")
    sorter_parser.add_argument("--priority", action="store_true", help="Order by priority")
    sorter_parser.add_argument("--reverse", action="store_true", help="Sort in descending order")

    args = parser.parse_args()

    if args.command == "add":
        task = manager.add_task(
            args.name, args.category, args.due_date,
            args.priority, args.status
        )
        manager.save()
        print(f"Task added: {task}")
        print(f"Current tasks: {[str(task) for task in manager.all_tasks()]}")

    elif args.command == "update":
        updates = {
            k: v for k, v in vars(args).items()
            if k not in ["command", "task_id"] and v is not None
        }
        success = manager.update_task(args.task_id, **updates)
        manager.save()
        print("Task updated successfully" if success else "Task not found.")

    elif args.command == "delete":
        success = manager.delete_task(args.task_id)
        manager.save()
        print("Task deleted successfully" if success else "Task not found.")

    elif args.command == "view":
        tasks = manager.all_tasks()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks available.")

    elif args.command == "filter":
        criteria = {
            k: v for k, v in vars(args).items()
            if k not in ["command"] and v is not None
        }
        tasks = manager.filter_tasks(**criteria)
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks match the criteria.")

    elif args.command == "sort":
        if args.name:
            key = "name"
        elif args.status:
            key = "status"
        elif args.priority:
            key = "priority"
        else:
            key = "due_date"
        
        tasks = manager.sort_tasks(key=key, reverse=args.reverse)
        
        for task in tasks:
            print(task)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
