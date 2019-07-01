**STRUCTURE**
```
└── backend-automated-tests
    ├── scenario_tester
    │   ├── helpers
    │	│	└── ...
    │	├── logs
    │	│	└── ...
    │	├── scenarios
    │	│	└── ...
    │   ├── __init__.py
    │   ├── logging.py
    │   └── tests.py
    ├── scripts
    │   └── ...
    └── run_test_scenario.py
```

**SCENARIOS**

**(simple requests)**
- check_syntaurus_state.py
- create_cost_and_popularity
- create_greedy_popularity
- create_manual_retro
- create_minimal_cost
- create_syntaurus
- create_travel_as_product
- create_travel_as_reactant
- get_chemical_entries
- get_cross_reactivity
- get_molecular_strain
- get_similar_molecules
- get_similar_reactions
- pause_syntaurus
- stop_syntaurus

**(algorithms)**
- run_cost_and_popularity_and_wait_for_success
- run_greedy_popularity_and_wait_for_success
- run_manual_retro_and_wait_for_success
- run_minimal_cost_and_wait_for_success
- run_syntaurus_and_wait_for_success
- run_travel_as_product_and_wait_for_success
- run_travel_as_reactant_and_wait_for_success

**HELPERS**
- **create_computation_and_get_results**
provides polling for algorithms, currently only polls the auto-retro, the other algorithms are just treated as simple requests;  a 5 second sleep is currently set after each auto retro computation
- **json_parser**
accepts response content as json and deserializes it or returns as is if an instance of dict/list
- **kwargs_check**
works as an internal user input validator/converter and accepts two dicts, "required params" (e.g. {'timeout': 'digit', 'steps': 'digit', 'polling_interval': 'digit', 'snapshot_time': 'digit'}) and "received params" (e.g. {'timeout': '240', 'steps': '300', 'polling_interval': '3', 'snapshot_time': '120'})) - it validates whether the actual input has all the required keys and, if their values are defined as 'digit', attempts to convert them to int
- **models**
- **render_results**
builds a string out of received scenario data to be displayed and logged as summary

- **send_requests**
prepares the request to be sent to the chemical backend

**USAGE**
- **Required arguments**
a name of the scenario to run or multiple scenario names separated by space

- **Optional arguments**
```
--worker-url        type = str, default = 'munechem02.chematica.net'
	url of the instance to connect to
--worker-port       type = str, default = '443'
	port of the instance to connect to
--worker-user       type = str, default = same as for webapp
	user credentials for the instance
--worker-password'  type = str, default = same as for webapp
	password credentials for the instance
--log-level         type = str, default = 'INFO', choices = DEBUG, INFO, WARNING, ERROR
	defines logger specificity, e.g. DEBUG will print response content with graphml
--log-file          type = str
	requires {path}/{file} string, if present logger will create and write to a specified file in a specified path, relative to the main module location
--summary-log-file  type = str
	requires {path}/{file} string, if present logger will create and write to a specified file in a specified path, relative to the main module location (log-file argument must also be present)
--name              type = str, default = 'anonymous_tester'
	the name that appears in each log entry (e.g. could be a user name or a test name)
--repeat            type = int, default = 1
	runs all the scenarios given and then repeats n times
--scenario-args     type = str
	- creates a list of dictionaries to allow additional optional arguments to be used with scenarios
	- attempts to match each dictionary from the list with the scenario of the same index in the scenario list, surplus dictionaries are ignored
	- syntax: dict1_key1=dict1_value1,dict1_key2=dict1_value2 dict2_key1=dict2_value1,dict2_key2=dict2_value2 (etc.)
	- example: "--scenario-args db=1,options=123 db=2,options=13"
	 (would be parsed as [{'db':'1', 'options':'123'}, {'db':'2', 'options':'13'}])
	- defaults:
		poll_interval = 3 (the polling interval expressed in the number of seconds to elapse between check state requests in auto-retro computation)
	 	snapshot = 0 (the number of seconds after which a snapshot of the current number of paths and iterations in auto-retro computation should be taken)
	 	steps = 300 (the number of iterations after which the auto-retro computation will be stopped; is negated when snapshot is > 0)
```

**BASH SCRIPTS**
- `test_run_manual`
  runs 11 consecutive manual retro computations
- `test_run_simultaneous_morphin`
  runs 10 simultaneous manual retro computations for morphin
- `test_run_simultaneous_taxol`
  runs 10 simultaneous manual retro computations for taxol
- `test_run_syntaurus`
  runs 7 consecutive auto retro computations
