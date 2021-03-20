from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.processors import PrintResult
from pprint import pprint

from processors import PrintProgress,SaveResultToDict,SaveResultToList

from napalm_tasks import my_napalm_get
from netmiko_tasks import my_netmiko_command


nr = InitNornir(config_file="config.yaml", dry_run=True)

#results_dict = {}
#results_list = {}

#nr_with_processors = nr.with_processors([SaveResultToDict(results_dict),
#                                         SaveResultToList(results_list),
#                                         PrintProgress()
#                                        ])

nr_with_processors = nr.with_processors([PrintResult()])

results = nr_with_processors.run(task=my_napalm_get)

print_result(results)

#pprint(results_list, depth=5)

#pprint(results_dict, depth=5)
