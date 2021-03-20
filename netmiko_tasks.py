from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from nornir.core.task import Task, Result


def my_netmiko_command(task: Task) -> Result:
    result = task.run(
        task=netmiko_send_command, 
        command_string = "show lldp neighbor", 
        use_textfsm=True
        )
    return Result(
        host=task.host,
        result=f'Task {task.name} on host {task.host} {"failed" if result.failed else "completed succesfully"}'
        )


nr = InitNornir(config_file="config.yaml", dry_run=True)
results = nr.run(task=my_netmiko_command)
print_result(results)

