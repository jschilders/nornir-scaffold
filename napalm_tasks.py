from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.task import Task, Result


def my_napalm_get(task: Task) -> Result:
    result = task.run(
        task=napalm_get, 
        name='Facts', 
        getters=['facts']
        )
    return Result(
        host=task.host,
        result=f'Task {task.name} on host {task.host} {"failed" if result.failed else "completed succesfully"}'
        )


nr = InitNornir(config_file="config.yaml", dry_run=True)
results = nr.run(task=my_napalm_get)
print_result(results)

