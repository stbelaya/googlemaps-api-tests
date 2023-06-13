import allure

from utils.api import GoogleMapsApi
from utils.assertions import Assertions
from utils.base_case import BaseCase


@allure.epic("Test create location cases")
class TestCreateLocation(BaseCase):
    """Creation of new location"""

    @allure.description("Creation of new location")
    def test_create_new_place(self):

        # Creation
        response1 = GoogleMapsApi.create_new_place()

        place_id = self.get_json_value(response1, "place_id")

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_keys(
            response1,
            ['status', 'place_id', 'scope', 'reference', 'id']
        )
        Assertions.assert_json_value_by_name(
            response1,
            'status',
            'OK',
            "Failed. Value for received field is not equal to expected"
        )
        Assertions.assert_json_value_by_name(
            response1,
            'scope',
            'APP',
            "Failed. Value for received field is not equal to expected"
        )

        # Get created location
        response2 = GoogleMapsApi.get_new_place(place_id)

        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_has_keys(
            response2,
            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        )
        Assertions.assert_json_value_by_name(
            response2,
            'address', '29, side layout, cohen 09',
            "msg"
        )


