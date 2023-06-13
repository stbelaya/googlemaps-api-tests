import allure

from utils.api import GoogleMapsApi
from utils.assertions import Assertions
from utils.base_case import BaseCase


@allure.epic("Test retrieve location cases")
class TestGetLocation(BaseCase):
    """Get of a location"""

    @allure.description("Retrieving of an existing location")
    def test_get_existing_location(self):

        # Creation
        response1 = GoogleMapsApi.create_new_place()

        place_id = self.get_json_value(response1, "place_id")

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
            "'address' field has incorrect value"
        )

    @allure.description("Retrieving of a non-existing location")
    def test_get_non_existing_location(self):
        place_id = "55555"

        response2 = GoogleMapsApi.get_new_place(place_id)

        Assertions.assert_status_code(response2, 404)
        Assertions.assert_json_has_key(
            response2,
            'msg'
        )
        Assertions.assert_json_value_by_name(
            response2,
            "msg",
            "Get operation failed, looks like place_id  doesn't exists",
            "'msg' field has incorrect value"
        )
        Assertions.assert_json_has_not_keys(
            response2,
            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        )

