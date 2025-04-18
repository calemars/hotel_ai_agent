def find_customer(email: str = "", phone: str = "") -> dict:
    """
    Find a customer by email or phone number.

    This function searches through a list of known customers to locate a match.
    It returns the full customer profile if found, or an error response if not.

    Args:
        email (str, optional): The guest's email address.
        phone (str, optional): The guest's phone number.

    Returns:
        dict: A dictionary containing the customer's profile if found.
            - customer_id (str)
            - guest_name (str)
            - email (str)
            - phone (str)

        If no match is found:
        {
            "success": False,
            "message": "Customer not found."
        }
    """
    # Simulated database of customer profiles
    customers = [
        {
            "customer_id": "CUST001",
            "guest_name": "Jessica Taylor",
            "email": "jessica.taylor@example.com",
            "phone": "+1-312-555-0198"
        },
        {
            "customer_id": "CUST002",
            "guest_name": "Mark Johnson",
            "email": "mark.johnson@example.com",
            "phone": "+1-646-555-8834"
        },
        {
            "customer_id": "CUST003",
            "guest_name": "Aisha Patel",
            "email": "aisha.patel@example.com",
            "phone": "+1-212-555-1923"
        }
    ]

    for customer in customers:
        if (email!="" and customer["email"] == email) or (phone!="" and customer["phone"] == phone):
            return customer

    return {
        "success": False,
        "message": "Customer not found."
    }


def get_reservations(customerId: str) -> dict:
    """Retrevies the current bookings for a customer. If there are no bookings for the customer, it will suggest that the customer be prompted to create a booking.
    When you are telling the customer their current reservations, give as much detail as possible. DO NOT TELL CUSTOMERS THAT ARE NOT ASSOCIATED TO THEIR CUSTOMER ID.

    Args:
        customerId (str): The unique id of the customer that you are going to be helping. 

    Returns:
        dict: status and list of reservations (empty if none exist) or error msg.
    """

    return {
        "status": "success",
        "reservations": [
            {
                "reservation_id": "RES12345",
                "customer_id":"CUST001",
                "guest_name": "Jessica Taylor",
                "email": "jessica.taylor@example.com",
                "phone": "+1-312-555-0198",
                "check_in": "2025-07-10",
                "check_out": "2025-07-14",
                "room_type": "King Suite",
                "num_guests": 2,
                "status": "confirmed",
                "total_cost": 1024.75
            },
            {
                "reservation_id": "RES67890",
                "customer_id":"CUST002",
                "guest_name": "Mark Johnson",
                "email": "mark.johnson@example.com",
                "phone": "+1-646-555-8834",
                "check_in": "2025-08-01",
                "check_out": "2025-08-05",
                "room_type": "Double Queen",
                "num_guests": 2,
                "status": "confirmed",
                "total_cost": 835.60
            },
            {
                "reservation_id": "RES54321",
                "customer_id":"CUST003",
                "guest_name": "Aisha Patel",
                "email": "aisha.patel@example.com",
                "phone": "+1-212-555-1923",
                "check_in": "2025-09-15",
                "check_out": "2025-09-18",
                "room_type": "Standard",
                "num_guests": 1,
                "status": "confirmed",
                "total_cost": 450.00
            }
        ],
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
                "hotel_id": "HOTEL001",
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


def cancel_reservation(reservationId: int) -> dict:
    """Cancel an existing reservation by reservation ID.

    This function marks the reservation as cancelled and optionally simulates a refund.
    It assumes a valid reservation ID is provided and that the reservation exists in the system.

    Args:
        reservation_id (str): The unique ID of the reservation to cancel.
            Example: "RES67890"

    Returns:
        dict: A dictionary indicating the cancellation result. Fields include:
            - reservation_id (str): The ID of the cancelled reservation.
            - status (str): The new status of the reservation ("cancelled").
            - refund_issued (bool): Whether a refund was issued.
            - success (bool): Whether the operation completed successfully.
    """

    return {
        "reservation_id": "RES67890",
        "status": "cancelled",
        "refund_issued": True,
        "success": True
    }


