import simplejson as json

from uuid import uuid4

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend
from scenario_tester.logging import SCENARIO_LOGGER as logger

def create_syntaurus(url, scenario_args):

    bases = []
    for db_number in ['1','2','3','4']:
        if db_number in scenario_args.get('db', 'None'):
            if db_number == '1':
                bases.append(0)
            elif db_number == '2':
                bases.append(1)
            elif db_number == '3':
                bases.append(2)
            elif db_number == '4':
                bases.append(3)

    options = {
    "allow_strategies": False,
    "multicut": False,
    "strain": False,
    "macrocycles": False,
    "cut_all_heterocycles": False,
    }

    assert [number not in scenario_args.get('options', 'None') for number in ['1','2']] != [False, False]
    for filter_number in ['1','2','3','4','5']:
        if filter_number in scenario_args.get('options', 'None'):
            if filter_number == '1':
                options['allow_strategies'] = True
            elif filter_number == '2':
                options['multicut'] = True
            elif filter_number == '3':
                options['strain'] = True
            elif filter_number == '4':
                options['macrocycles'] = True
            elif filter_number == '5':
                options['cut_all_heterocycles'] = True

    logger.info('DB: {}'.format(bases))
    logger.info('Options: {}'.format(options))
    uuid = uuid4()

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/auto-retro/new-task'.format(url, scenario_args['port']),
        data = json.dumps({
                "uid": "{}".format(uuid),
                "request": json.dumps({
                    "max_mass_buy": 1000,
                    "additional_params": "%%EXTENDED_MOLFILE%%%",
                    "retro_timeout": 120,
                    "max_reactions_per_product": 20,
                    "graph_depth": 0,
                    "price": 1000,
                    "allow_strategies": options['allow_strategies'],
                    "multicut": options['multicut'],
                    "macrocycles": options['macrocycles'],
                    "popularity": 5,
                    "reaction_cost_formula": "20+40*PROTECT+5000*(CONFLICT+NON_SELECTIVITY+FILTERS)",
                    "beam_width": 100,
                    "depth": 0,
                    "heteroatoms_stop_condition": options['cut_all_heterocycles'],
                    "smiles": scenario_args.get('smiles', "COc1cccc(C2(O)CCCCC2CN(C)C)c1"),
                    "returned_paths": 50,
                    "heur_fun_by_mol": "SMALLER**2+100*RINGS+100*STEREO,SMALLER**1.4+50*RINGS+50*STEREO",
                    "bases": bases,
                    "strain": options['strain'],
                    "exclude_diastereoselective_reactions": False,
                    "max_mass": 1000,
                }),
                #"method": "new_syntaurus_task",
            }),
    )}
