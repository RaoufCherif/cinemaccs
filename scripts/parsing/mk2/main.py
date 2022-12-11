import json
import httpx
from theater_parser import call_website, find_data_key

website = "https://www.mk2.com/"
MAP = {
    "name": "name",
    "id": "internal_id",
    "complexSlug": "complex_slug",
    "cinemaNationalId": "cinema_nation_id",
    "address1": "address_1",
    "address2": "address_2",
    "city": "city",
    "latitude": "latitude",
    "longitude": "longitude",
    "parkingInfo": "parking_info",
    "isGiftStore": "is_gift_store",
    "description": "description",
    "publicTransport": "public_transport",
    "currencyCode": "currency_code",
    "allowPrintAtHomeBookings": "allow_print_at_home_bookings",
    "allowOnlineVoucherValidation": "allow_on_line_voucher_validation",
    "displaySofaSeats": "display_sofa_seats",
    "timeZoneId": "time_zone_id",
}


def remap_keys(json, MAP, discard=False):
    if isinstance(json, dict):
        if discard:
            return {
                MAP[k]: remap_keys(v, MAP, discard) for k, v in json.items() if k in MAP
            }
        return {MAP.get(k, k): remap_keys(v, MAP, discard) for k, v in json.items()}
    elif isinstance(json, list):
        return [remap_keys(j, MAP, discard) for j in json]
    return json

if __name__ == "__main__":

    mk2_website = call_website(website)
    data_key = find_data_key(mk2_website)
    theater_json = json.loads(
        call_website(f"{website}_next/data/{data_key}/salles.json")
    )
    theaters = theater_json.get("pageProps").get("cinemaGroups")[0].get("cinemas")
    for i in range(len(theaters)):
        theater_post=remap_keys(theaters[i], MAP, discard=True)
        theater_post["company_name"]='MK2'
        print(theater_post)
        r = httpx.post('http://localhost:8000/api/theater/', data=theater_post)