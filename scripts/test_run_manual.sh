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
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 1 - taxol basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args	   db=1,steps=300 \
	--log-level        INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 2 - morphin basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,steps=300 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 3 - tramadol basic' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='COc1cccc(C2(O)CCCCC2CN(C)C)c1',db=1,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 4 - taxol all options' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,options=123,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 5 - morphin all options' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=1,options=123,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 6 - tramadol all options' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='COc1cccc(C2(O)CCCCC2CN(C)C)c1',db=1,options=123,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 7 - taxol multicut' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,options=1,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 8 - taxol cut into smaller fragments' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,options=2,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 9 - taxol mark non-selective' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,options=3,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 10 - morphin all options, all DB' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CN1CC[C@@]23c4c5c(O)ccc4C[C@@H]1[C@@H]2C=C[C@H](O)[C@@H]3O5',db=123,options=123,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
&&
./manage.py \
	run_test_scenario \
	run-manual-retro-and-wait-for-success \
	--name		       'MANUAL RETRO 11 - taxol all options, all DB' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--log-level 	   INFO \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=123,options=123,steps=300 \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_manual_retro_summary_"$timestamp".log \
	--repeat 5 \
