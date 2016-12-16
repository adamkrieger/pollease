import unittest
import parsing

class TestParsing(unittest.TestCase):

    def test_sample_slack_form_data(self):

        sample = "token=TOKENNNNNN&team_id=T3F55CL14&team_domain=swedishchefs&channel_id=C3F55CNDC&channel_name=general&user_id=U3DQ62P5X&user_name=adam.rehill&command=%2Fpollease&text=what+up+bjorkerz&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT3GARBAGEFJuO0taWFevCp"

        res = parsing.parse_form_to_dict(sample)

        self.assertEqual(
            res,
            {
                "token":"TOKENNNNNN",
                "team_id":"T3F55CL14",
                "team_domain":"swedishchefs",
                "channel_id":"C3F55CNDC",
                "channel_name":"general",
                "user_id":"U3DQ62P5X",
                "user_name":"adam.rehill",
                "command":"%2Fpollease",
                "text":"what+up+bjorkerz",
                "response_url":"https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT3GARBAGEFJuO0taWFevCp"
            }
        )

if __name__ == '__main__':
    unittest.main()
