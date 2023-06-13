from utils.http_methods import HttpMethods
from environment import ENV_OBJECT


class GoogleMapsApi:
    """Methods for Google Maps API testing"""

    @staticmethod
    def create_new_place():
        """Method for new location creation"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }
        # resource for POST method
        post_resource = "/maps/api/place/add/json"
        post_url = post_resource + ENV_OBJECT.KEY
        # print("Response: ", HttpMethods.post(post_url, json_for_create_new_place))
        return HttpMethods.post(post_url, json_for_create_new_place)

    @staticmethod
    def get_new_place(place_id):
        """Method for new location check"""

        get_resource = "/maps/api/place/get/json"
        get_url = get_resource + ENV_OBJECT.KEY + "&place_id=" + place_id

        return HttpMethods.get(get_url)

    @staticmethod
    def update_place(place_id, address="100 Lenina street, RU"):
        """Method for update location"""

        json_for_update_location = {
            "place_id": place_id,
            "address": address,
            "key": "qaclick123"
        }

        put_resource = "/maps/api/place/update/json"
        put_url = put_resource + ENV_OBJECT.KEY + "&place_id=" + place_id

        return HttpMethods.put(put_url, json_for_update_location)

    @staticmethod
    def delete_place(place_id):
        """Method for delete location"""

        json_for_delete_location = {
            "place_id": place_id
        }

        delete_resource = "/maps/api/place/delete/json"
        delete_url = delete_resource + ENV_OBJECT.KEY

        return HttpMethods.delete(delete_url, json_for_delete_location)
