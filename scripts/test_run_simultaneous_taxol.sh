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
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 1' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 2' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 3' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 4' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 5' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 6' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 7' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 8' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 9' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&
./manage.py \
	run_test_scenario \
	run-syntaurus-and-wait-for-success \
	--name		       'AUTO RETRO 5 - taxol basic (simultaneous) - instance 10' \
	--instance-type	   BACKEND \
	--worker-url 	   munechem02.chematica.net \
	--scenario-args    smiles='CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C',db=1,timeout=5400,snapshot=5400,poll_interval=9 \
	--log-level 	   INFO \
	--log-file 		   ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_"$timestamp".log \
	--summary-log-file ./scenario_tester/logs/backend/trial_run/trial_run_auto_retro_simultaneous_taxol_summary_"$timestamp".csv \
&