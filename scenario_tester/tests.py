import os

from unittest.mock                          import patch

from django.test                            import TestCase

from scenario_tester.management.commands                        import run_test_scenario
from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results
from scenario_tester.helpers.models import CommandError

from utils.test_helpers import TestJSONResponse

RUN_TEST_SCENARIO_RESULT = {'response_time': 5, 'response_json': "All fine"}

MANUAL_RETRO_RESPONSE = TestJSONResponse(
            content = ({
                'id': 294,
                'user': 2,
                'analysis': 348,
                'name': 'Test computation',
                'state': 'ERROR',
                'error_code': 'worker-http-error',
                'error_message': 'ManualRetrosynthesisComputation #294: Bad response status code 500',
                'progress_item': '',
                'parent_molecule': None,
                'parent_reaction_node': None,
                'latest_result': None,
                'created_at': '2017-12-21T15:12:39.293502Z',
                'updated_at': '2017-12-21T15:12:39.293531Z',
                'started_at': '2017-12-21T15:12:39.393386Z',
                'finished_at': '2017-12-21T15:13:29.537465Z',
                'computation_time': 50,
                'algorithm': 'MANUAL_RETROSYNTHESIS',
                'input': {
                    'smiles': 'CC',
                    'bases': {
                        'EXPERT_CHEMISTRY': {},
                        'ARENES': {},
                        'HETEROCYCLES': {}
                    },
                    'post_filters': {
                        'MARK_NON_SELECTIVE': {},
                        'MULTICUT': {},
                        'CUT_INTO_SMALLER_FRAGMENTS': {}
                    }
                }
            }),
            status_code = 200,
)


class ScriptTests(TestCase):

    @patch('scenario_tester.management.commands.run_test_scenario.run_scenario')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    def test_all_optional_arguments_should_be_usable_with_command(self, mock_login_response, mock_run_scenario_response):

        mock_login_response.return_value        = "dummy token"
        mock_run_scenario_response.return_value = RUN_TEST_SCENARIO_RESULT

        run_test_scenario.Command.handle(self,
            scenarios     = ['list-analyses'],
            user          = 'user',
            password      = 'passwordpassword',
            repeat        = 2,
            log_file      = '{}/test_log.log'.format(os.environ['HOME']),
            log_level     = "INFO",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        self.assertEqual(mock_login_response.call_count, 1)
        self.assertEqual(mock_run_scenario_response.call_count, 2)

    def test_command_should_raise_command_error_if_password_given_without_user(self):

        self.assertRaises(run_test_scenario.CommandError, run_test_scenario.Command.handle, self,
            scenarios     = ['list-analyses'],
            user          = None,
            password      = 'dummy',
            url           = 'wrongurl',
            log_file      = None,
            log_level     = "INFO",
            scenario_args = None,
            name          = 'anonymous_tester',
        )

    def test_command_should_raise_command_error_if_user_given_without_password(self):

        self.assertRaises(run_test_scenario.CommandError, run_test_scenario.Command.handle, self,
            scenarios     = ['list-analyses'],
            user          = 'dummy',
            password      = None,
            url           = 'wrongurl',
            log_file      = None,
            log_level     = "INFO",
            scenario_args = None,
            name          = 'anonymous_tester',
        )

    @patch('scenario_tester.management.commands.run_test_scenario.run_scenario')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    def test_command_should_accept_single_scenario(self, mock_login_response, mock_run_scenario_response):

        mock_login_response.return_value = "dummy token"
        mock_run_scenario_response.return_value = RUN_TEST_SCENARIO_RESULT

        run_test_scenario.Command.handle(self,
            scenarios     = ['list-analyses'],
            user          = 'user',
            password      = 'password',
            repeat        = 1,
            log_file      = None,
            log_level     = "INFO",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        self.assertEqual(mock_login_response.call_count, 1)
        self.assertEqual(mock_run_scenario_response.call_count, 1)

    @patch('scenario_tester.management.commands.run_test_scenario.run_scenario')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    def test_command_should_accept_multiple_scenarios(self, mock_login_response, mock_run_scenario_response):

        mock_login_response.return_value = "dummy token"
        mock_run_scenario_response.return_value = RUN_TEST_SCENARIO_RESULT

        run_test_scenario.Command.handle(self,
            scenarios     = ['list-analyses', 'list-analyses'],
            user          = 'user',
            password      = 'password',
            repeat        = 1,
            log_file      = None,
            log_level     = "INFO",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        self.assertEqual(mock_login_response.call_count, 1)
        self.assertEqual(mock_run_scenario_response.call_count, 2)

    def test_command_should_raise_command_error_if_wrong_scenario_name(self):

        token          = "dummy"
        scenario       = "wrongscenario"
        url            = 'dummy'
        scenario_args  = None

        self.assertRaises(run_test_scenario.CommandError, run_test_scenario.run_scenario, scenario, url, token, scenario_args)

    @patch('scenario_tester.management.commands.run_test_scenario.login')
    def test_command_should_raise_command_error_if_logging_unsuccessful(self, mock_login_response):

        mock_login_response.side_effect = ConnectionError("Cannot connect to host.")

        with self.assertRaises(CommandError):

            run_test_scenario.Command.handle(self,
                scenarios     = ['list-analyses'],
                user          = 'dummy',
                password      = 'dummy',
                url           = 'http://example.com/',
                log_file      = None,
                log_level     = "INFO",
                scenario_args = None,
                name          = 'anonymous_tester',
            )

    def test_command_should_raise_command_error_if_url_invalid(self):

        self.assertRaises(CommandError, run_test_scenario.Command.handle, self,
            scenarios     = ['list-analyses'],
            user          = 'dummy',
            password      = 'dummy',
            url           = 'wrongurl',
            log_file      = None,
            log_level     = "INFO",
            scenario_args = None,
            name          = 'anonymous_tester',
        )

    @patch('scenario_tester.management.commands.run_test_scenario.parse_json_from_response')
    @patch('scenario_tester.helpers.create_computation_and_get_results.parse_json_from_response')
    @patch('scenario_tester.helpers.send_requests.send_request_to_backend')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    @patch('scenario_tester.management.commands.run_test_scenario.logger')
    def test_command_should_log_computation_errors_from_algorithm_based_analysis(
        self,
        mock_logger,
        mock_login_response,
        mock_manual_retro_response,
        mock_parse_json_from_response,
        mock_parse_scenario_json_from_response
    ):
        mock_login_response.return_value        = "dummy token"

        mock_manual_retro_response.return_value    = MANUAL_RETRO_RESPONSE
        mock_parse_json_from_response.return_value = MANUAL_RETRO_RESPONSE.content
        mock_parse_scenario_json_from_response.return_value = MANUAL_RETRO_RESPONSE.content

        run_test_scenario.Command.handle(self,
            scenarios     = ['run-manual-retro-and-wait-for-success'],
            user          = 'user',
            password      = 'passwordpassword',
            repeat        = 1,
            log_file      = '{}/test_log.log'.format(os.environ['HOME']),
            log_level     = "DEBUG",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        mock_logger.info.assert_called_with("Additional information for scenario run-manual-retro-and-wait-for-success - iteration 1:\n        Computation 294 has encountered an error\n")

    @patch('scenario_tester.management.commands.run_test_scenario.parse_json_from_response')
    @patch('scenario_tester.helpers.create_computation_and_get_results.parse_json_from_response')
    @patch('scenario_tester.helpers.send_requests.send_request_to_backend')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    @patch('scenario_tester.management.commands.run_test_scenario.logger')
    def test_command_should_log_unknown_state_from_algorithm_based_analysis(
            self,
            mock_logger,
            mock_login_response,
            mock_manual_retro_response,
            mock_parse_json_from_response,
            mock_parse_scenario_json_from_response
    ):
        mock_login_response.return_value        = "dummy token"

        MANUAL_RETRO_RESPONSE.content['state'] = 'Weird-Al Stateovic'
        mock_manual_retro_response.return_value             = MANUAL_RETRO_RESPONSE
        mock_parse_json_from_response.return_value          = MANUAL_RETRO_RESPONSE.content
        mock_parse_scenario_json_from_response.return_value = MANUAL_RETRO_RESPONSE.content

        run_test_scenario.Command.handle(self,
            scenarios     = ['run-manual-retro-and-wait-for-success'],
            user          = 'user',
            password      = 'passwordpassword',
            repeat        = 1,
            log_file      = '{}/test_log.log'.format(os.environ['HOME']),
            log_level     = "DEBUG",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        mock_logger.info.assert_called_with("Additional information for scenario run-manual-retro-and-wait-for-success - iteration 1:\n        Computation 294 has an unknown state: Weird-Al Stateovic\n")

    @patch('scenario_tester.management.commands.run_test_scenario.parse_json_from_response')
    @patch('scenario_tester.helpers.create_computation_and_get_results.parse_json_from_response')
    @patch('scenario_tester.helpers.send_requests.send_request_to_backend')
    @patch('scenario_tester.management.commands.run_test_scenario.login')
    @patch('scenario_tester.management.commands.run_test_scenario.logger')
    def test_command_should_log_missing_state_from_algorithm_based_analysis(
        self,
        mock_logger,
        mock_login_response,
        mock_manual_retro_response,
        mock_parse_json_from_response,
        mock_parse_scenario_json_from_response,
    ):
        mock_login_response.return_value        = "dummy token"

        MANUAL_RETRO_RESPONSE.content.pop('state')
        mock_manual_retro_response.return_value             = MANUAL_RETRO_RESPONSE
        mock_parse_json_from_response.return_value          = MANUAL_RETRO_RESPONSE.content
        mock_parse_scenario_json_from_response.return_value = MANUAL_RETRO_RESPONSE.content

        run_test_scenario.Command.handle(self,
            scenarios     = ['run-manual-retro-and-wait-for-success'],
            user          = 'user',
            password      = 'passwordpassword',
            repeat        = 1,
            log_file      = '{}/test_log.log'.format(os.environ['HOME']),
            log_level     = "DEBUG",
            name          = 'test_user',
            url           = 'testing_url',
            scenario_args = None,
        )

        mock_logger.info.assert_called_with("Additional information for scenario run-manual-retro-and-wait-for-success - iteration 1:\n        Computation 294 has an unknown state: computation state is missing\n")

    def test_create_computation_template_should_raise_command_error_if_run_with_analysis_id_given_and_scenario_is_with_analysis_scenario(self):

        scenario = 'create-reaction-network-with-analysis'
        url      = 'test_url'
        token    = "dummy token"
        scenario_args = {
            'analysis-id': 1
        }

        self.assertRaises(CommandError, create_computation_and_get_results, scenario, url, token, scenario_args)

    @patch('scenario_tester.helpers.send_requests.send_request_to_backend')
    @patch('scenario_tester.helpers.create_computation_and_get_results.logger')
    def test_create_computation_template_should_log_error_if_computation_id_is_missing(
        self,
        mock_logger,
        mock_backend_response,
    ):  # pylint: disable=no-self-use

        MOCK_CREATE_ANALYSIS_RESPONSE = TestJSONResponse(
            content = ({
                'user': 2,
                'id': 1,
            }),
            status_code = 200
        )

        MOCK_REACTION_NETWORK_RESPONSE = TestJSONResponse(
            content = ({
                'user': 2,
                'analysis': 1,
                'status': 'SUCCESS'
            }),
            status_code = 200
        )

        mock_backend_response.side_effect = (MOCK_CREATE_ANALYSIS_RESPONSE, MOCK_REACTION_NETWORK_RESPONSE)

        scenario      = 'create-reaction-network'
        url           = 'test_url'
        token         = 'dummy'
        scenario_args = {}

        create_computation_and_get_results(scenario, url, token, scenario_args)

        self.assertEqual(mock_logger.error.call_count, 1)

    @patch('scenario_tester.helpers.create_computation_and_get_results.patch_name_to_analysis')
    @patch('scenario_tester.helpers.send_requests.send_request_to_backend')
    def test_create_computation_template_should_patch_name_if_name_arg_present_and_scenario_is_with_analysis_scenario(
        self,
        mock_backend_response,
        mock_patch,
    ):  # pylint: disable=no-self-use

        mock_backend_response.return_value = MANUAL_RETRO_RESPONSE

        scenario      = 'create-reaction-network-with-analysis'
        url           = 'test_url'
        token         = 'dummy'
        scenario_args = {'name': 'test_name'}

        create_computation_and_get_results(scenario, url, token, scenario_args)

        mock_patch.assert_called_with(url, token, {'computation-id': 294, 'analysis-id': 348, 'name': 'test_name'})
