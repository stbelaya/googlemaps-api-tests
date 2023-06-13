import json


class CheckResponse:
    """Methods for checking responses"""

    # @staticmethod
    # def check_status_code(result, status_code):
    #     """Method for checking status code"""
    #     assert status_code == result.status_code, \
    #         f"Failed. Received status code: '{result.status_code}' is not equal to expected '{status_code}'"
    #     print(f"Success! Status code is: '{result.status_code}'")

    # @staticmethod
    # def check_json_token(result, expected_value):
    #     """Method for checking mandatory fields in response"""
    #     token = list(json.loads(result.text))
    #     assert token == expected_value, f"Failed. Received fields: {token} are not equal to expected {expected_value}"
    #     print(f"Success! All fields are received: {token}")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Method for checking values of mandatory fields in response"""
        check = result.json()
        check_field = check.get(field_name)
        assert check_field == expected_value, \
            f"Failed. Value for received field '{field_name}': '{check_field}' is not equal to expected '{expected_value}'"
        print(f"Success! '{field_name}' field value is correct: '{check_field}'")

    @staticmethod
    def check_json_word_in_value(result, field_name, search_word):
        """Method for checking values of mandatory fields in response"""
        check = result.json()
        check_field = check.get(field_name)
        assert search_word in check_field, \
            f"Failed. Value for received field '{field_name}': '{check_field}' doesn't contain expected word '{search_word}'"
        print(f"Success! '{field_name}' field value contains word '{search_word}': {check_field}")
