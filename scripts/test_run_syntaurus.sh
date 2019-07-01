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
	--name		       'AUTO RETRO 1 - tramadol basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='COc1cccc(C2(O)CCCCC2CN(C)C)c1',db=1,steps=300 \
	--log-level        INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 2 - taxol basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 3 - morphin basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 4 - tramadol multicut' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='COc1cccc(C2(O)CCCCC2CN(C)C)c1',db=1,options=2,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol strategies' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,options=1,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 6 - morphin all options' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,options=345,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3 \
&&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 7 - taxol all databases' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1234,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_summary_"$timestamp".log \
	--repeat 3
