#!/bin/bash
get_timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}
timestamp=$(get_timestamp)
sudo killall ssh
sudo ssh -i /home/pandro/.ssh/id_rsa -fNL 443:munechem02.chematica.net:443 chematica-proxy -l pandro
#for i in $(seq $1)
#do
    #    wait $!
#done
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 1' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 2' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 3' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 4' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 5' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 6' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 7' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 8' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 9' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic (simultaneous) - instance 10' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_morphin_summary_"$timestamp".csv \
&