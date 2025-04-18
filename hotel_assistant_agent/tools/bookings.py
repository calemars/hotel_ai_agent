def get_reservations(customerId: str) -> dict:
    """Retrevies the current bookings for a customer. If there are no bookings for the customer, it will suggest that the customer be prompted to create a booking.

    Args:
        customerId (str): The unique id of the customer that you are going to be helping. 

    Returns:
        dict: status and list of reservations (empty if none exist) or error msg.
    """

    return {
        "status": "success",
        "reservations": (
            {
                "reservationId": 982034598,
                "startDate": "01/01/2026",
                "endDate": "01/08/2026"
            },
            {
                "reservationId": 23947029204,
                "startDate": "09/21/2026",
                "endDate": "09/28/2026"
            },
        ),
    }



def create_reservation(guest_info: dict, stay_info: dict) -> dict:
    """
    Create a new reservation using guest and stay information.

    Args:
        guest_info (dict): Dictionary with guest name, email, and phone number.
            Example: {
                "guest_name": "Mark Johnson",
                "email": "mark.johnson@example.com",
                "phone": "+1-646-555-8834"
            }

        stay_info (dict): Dictionary with reservation info.
            Example: {
                "check_in": "2025-08-01",
                "check_out": "2025-08-05",
                "room_type": "Double Queen",
                "num_guests": 2
            }

    Returns:
        dict: Dictionary including the reservation ID, status, total cost, and confirmation sent.
    """

    return {
    "reservation_id": "RES67890",
    "status": "confirmed",
    "total_cost": 835.60,
    "confirmation_sent": True
    }


def get_hotels() -> list[dict]:
    """
    Retrieve a list of available hotels with basic details.

    Returns:
        list[dict]: A list of hotels. Each hotel includes an ID, name, location, star rating, and amenities.
    """
    return [
        {
            "hotel_id": "HOTEL001",
            "name": "Seaside Resort",
            "location": "Miami Beach, FL",
            "rating": 4.5,
            "amenities": ["Pool", "Free WiFi", "Gym", "Beach Access"],
            "room_types": ["Standard", "Double Queen", "King Suite"]
        },
        {
            "hotel_id": "HOTEL002",
            "name": "Mountain View Lodge",
            "location": "Aspen, CO",
            "rating": 4.7,
            "amenities": ["Spa", "Free Breakfast", "Ski Shuttle", "Fireplace Rooms"],
            "room_types": ["Standard", "King Suite", "Family Suite"]
        },
        {
            "hotel_id": "HOTEL003",
            "name": "Urban Stay Central",
            "location": "Chicago, IL",
            "rating": 4.3,
            "amenities": ["Conference Room", "Pet Friendly", "Fitness Center", "Valet Parking"],
            "room_types": ["Standard", "Double Queen", "Executive Suite"]
        }
    ]


def get_rooms(hotel_id: str, check_in: str, check_out: str) -> list[dict]:
    """
    Retrieve available rooms for a specific hotel and date range.
    This simulates room availability with placeholder data.

    Args:
        hotel_id (str): The unique ID of the hotel
        check_in (str): Check-in date in YYYY-MM-DD format
        check_out (str): Check-out date in YYYY-MM-DD format

    Returns:
        list[dict]: A list of available rooms with type, price, and availability.
    """

    hotel_rooms = {
        "HOTEL001": [
            {"room_type": "Standard", "price_per_night": 150.00, "available": 5},
            {"room_type": "Double Queen", "price_per_night": 200.00, "available": 2},
            {"room_type": "King Suite", "price_per_night": 250.00, "available": 1},
        ],
        "HOTEL002": [
            {"room_type": "Standard", "price_per_night": 175.00, "available": 4},
            {"room_type": "King Suite", "price_per_night": 300.00, "available": 2},
            {"room_type": "Family Suite", "price_per_night": 350.00, "available": 0},  
        ],
        "HOTEL003": [
            {"room_type": "Standard", "price_per_night": 160.00, "available": 6},
            {"room_type": "Double Queen", "price_per_night": 210.00, "available": 3},
            {"room_type": "Executive Suite", "price_per_night": 275.00, "available": 1},
        ],
    }

    rooms = hotel_rooms.get(hotel_id, [])

    # Filter only rooms with availability > 0
    available_rooms = [room for room in rooms if room["available"] > 0]

    return available_rooms