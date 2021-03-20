from typing import Dict
from collections import defaultdict
from nornir.core import Nornir
from nornir.core.inventory import Host
from nornir.core.task import AggregatedResult, MultiResult, Result, Task


class PrintProgress:
    def task_started(self, task: Task) -> None:
        print(f"Nornir run {task.name} started")

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        print(f"Nornir run {task.name} completed")

    def task_instance_started(self, task: Task, host: Host) -> None:
        print(f"  Task {task.name} on host {host.name} started" )

    def task_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        print(f"  Task {task.name} on host {host.name} completed")

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        print(f"    Subtask {task.name} on host {host.name} started")

    def subtask_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        print(f"    Subtask {task.name} on host {host.name} completed")


class SaveResultToDict:
    def __init__(self, data: Dict[str, None]) -> None:
        self.data = data

    def task_started(self, task: Task) -> None:
        pass

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        pass

    def task_instance_started(self, task: Task, host: Host) -> None:
        self.data.setdefault(host.name, {})
        self.data[host.name][task.name] = {'status': 'Started'}

    def task_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        self.data[host.name][task.name]['status']  = 'Failed' if result.failed else 'Completed'
        if result.result:
            self.data[host.name][task.name]['result'] = result.result

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        self.data.setdefault(host.name, {})
        self.data[host.name][task.name] = {'status': 'Started'}
        
    def subtask_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        self.data[host.name][task.name]['status']  = 'Failed' if result.failed else 'Completed'
        if result.result:
            self.data[host.name][task.name]['result'] = result.result


class SaveResultToList:
    def __init__(self, data: Dict[str, None]) -> None:
        self.data = data

    def task_started(self, task: Task) -> None:
        pass

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        pass

    def task_instance_started(self, task: Task, host: Host) -> None:
        pass

    def task_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        self.data.setdefault(host.name, [])
        self.data[host.name].append(
            {
            'task':    task.name,
            'failed':  result.failed,
            'changed': result.changed,
            'result':  result.result
            }
        )

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        pass
        
    def subtask_instance_completed(self, task: Task, host: Host, result: MultiResult) -> None:
        self.data.setdefault(host.name, [])
        self.data[host.name].append(
            {
            'task':    task.name,
            'failed':  result.failed,
            'changed': result.changed,
            'result':  result.result
            }
        )
        