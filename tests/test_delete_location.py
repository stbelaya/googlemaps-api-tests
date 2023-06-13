import allure

from utils.api import GoogleMapsApi
from utils.assertions import Assertions
from utils.base_case import BaseCase


@allure.epic("Test delete location cases")
class TestDeleteLocation(BaseCase):
    """Deletion of a new location"""

    @allure.description("Deletion of an existing location")
    def test_delete_existing_location(self):

        # Creation
        response1 = GoogleMapsApi.create_new_place()

        place_id = self.get_json_value(response1, "place_id")

        # Deletion of a created location
        response2 = GoogleMapsApi.delete_place(place_id)

        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_has_key(response2, 'status')
        Assertions.assert_json_value_by_name(response2, 'status', 'OK', "'status' field has incorrect value")

        # Checking of a deleted location
        response3 = GoogleMapsApi.get_new_place(place_id)

        Assertions.assert_status_code(response3, 404)
        Assertions.assert_json_has_key(response3, 'msg')
        Assertions.assert_json_value_by_name(
            response3,
            'msg',
            "Get operation failed, looks like place_id  doesn't exists",
            "'msg' field has incorrect value"
        )

    @allure.description("Deletion of a non-existing location")
    def test_delete_non_existing_location(self):
        place_id = "55555"

        response2 = GoogleMapsApi.delete_place(place_id)

        Assertions.assert_status_code(response2, 404)
        Assertions.assert_json_has_key(response2, 'msg')
        Assertions.assert_json_value_by_name(
            response2,
            'msg',
            "Delete operation failed, looks like the data doesn't exists",
            "'msg' field has incorrect value"
        )
