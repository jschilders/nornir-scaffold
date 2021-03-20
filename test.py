from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.processors import PrintResult
from pprint import pprint

from processors import PrintProgress,SaveResultToDict,SaveResultToList

from napalm_tasks import my_napalm_get

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


s=[d for d in results['sw01'] if d.name=='Show ARP'][0].result
print(s[1])
print(s[2
])
s=[d for d in results['sw01'] if d.name=='CDP Neighbors'][0].result

for neighbor in results:
    print('-----')
    print('Local interface:  ', neighbor['local_interface'])
    print('Remote interface: ', neighbor['neighbor_interface'])
    print('Neighbor name:    ', neighbor['neighbor'])
    print('Platform          ', neighbor['platform'])
    print('Capability        ', neighbor['capability'])
    print('-----')
