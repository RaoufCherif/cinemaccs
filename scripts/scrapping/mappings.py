def remap_keys(json, MAP, discard=False):
    """
    Remapping a JSON

    input:
        - json: json we want to remap
        - MAP: New mapping we want to apply to the json
        - discard (optional): we keep only the fields in the MAP
    output:
        - json remapped
    """
    if isinstance(json, dict):
        if discard:
            return {
                MAP[k]: remap_keys(v, MAP, discard) for k, v in json.items() if k in MAP
            }
        return {MAP.get(k, k): remap_keys(v, MAP, discard) for k, v in json.items()}
    elif isinstance(json, list):
        return [remap_keys(j, MAP, discard) for j in json]
    return json


MAP_THEATER = {
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

MAP_MOVIE = {
    "title": "title",
    "runTime": "duration",
    "graphicUrl": "poster",
    "openingDate": "release_date",
    "synopsis": "synopsis",
    "id": "id",  ## Id côté MK2
    "slug": "slug",  ## Nom de la page des infos du film côté MK2
}

MAP_SESSION = {
    "movieId": "movie_id",
    "id": "internal_session_id",
    "cinemaId": "theater_internal_id",
    "seatsAvailable": "seats_available",
    "language": "language",
    "session_time": "session_time"
}
