import allure

from utils.api import GoogleMapsApi
from utils.assertions import Assertions
from utils.base_case import BaseCase


@allure.epic("Test edit location cases")
class TestEditLocation(BaseCase):
    """Update of a new location"""

    @allure.description("Update of an existing location")
    def test_update_address_for_existing_location(self):

        # Creation
        response1 = GoogleMapsApi.create_new_place()

        place_id = self.get_json_value(response1, "place_id")

        # Update of the created location
        new_data = '100 Lenina street, RU'
        response2 = GoogleMapsApi.update_place(place_id, new_data)

        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_has_key(response2, 'msg')
        Assertions.assert_json_value_by_name(
            response2,
            'msg',
            'Address successfully updated',
            "'msg' field has incorrect value"
        )

        # Retrieving of the updated location
        response2 = GoogleMapsApi.get_new_place(place_id)
        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_has_keys(
            response2,
            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        )
        Assertions.assert_json_value_by_name(
            response2,
            'address', new_data,
            "'address' field has incorrect value"
        )

    @allure.description("Update of a non-existing location")
    def test_update_address_for_non_existing_location(self):
        place_id = "5555"

        # Update of the created location
        new_data = '100 Lenina street, RU'
        response2 = GoogleMapsApi.update_place(place_id, new_data)

        Assertions.assert_status_code(response2, 404)
        Assertions.assert_json_has_key(response2, 'msg')
        Assertions.assert_json_value_by_name(
            response2,
            'msg',
            "Update address operation failed, looks like the data doesn't exists",
            "'msg' field has incorrect value"
        )