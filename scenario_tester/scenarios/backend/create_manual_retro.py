import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend
from scenario_tester.logging import SCENARIO_LOGGER as logger

def create_manual_retro(url, scenario_args):

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

    filter_names = []
    for filter_number in ['1','2','3']:
        if filter_number in scenario_args.get('options', 'None'):
            if filter_number == '1':
                filter_names.append("Multicut")
            elif filter_number == '2':
                filter_names.append("Cut into smaller fragments")
            elif filter_number == '3':
                filter_names.append("Mark non-selective")
    logger.info('DB: {}'.format(bases))
    logger.info('Options: {}'.format(filter_names))

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/manual-retro'.format(url, scenario_args['port']),
        data = json.dumps({
                "smiles":           scenario_args.get('smiles', "CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C"),
                "multicut":         False,
                "advanced_options": "%%EXTENDED_MOLFILE%%%",
                "bases": bases,
                "filter_names": filter_names,
            })
    )}
