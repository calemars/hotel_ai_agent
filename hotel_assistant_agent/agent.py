from google.adk.agents import Agent

from .tools.bookings import find_customer, get_reservations, create_reservation, get_hotels, get_rooms

root_agent = Agent(
    name="hotel_agent",
    model="gemini-2.0-flash",
    description=(
        "Root agent to answer guest questions or complete tasks to best support guests."
    ),
    instruction=(
        """You are a helpful customer service agent for a hotel chain. You will be interacting with customers and helping perform actions for them. 
        The optimal flow for booking a reservation is this:
        1. Guest identifies what hotel they are looking to stay at (use the get_hotels function to get the context for all of our hotels)
        2. Guest provides stay details: check-in/check-out dates and number of guests
        3. Check what room types are available for those dates (use the get_rooms function to get the context for all available rooms)
        4. Once a user selects a room type, the room is booked for the guest """
    ),
    tools=[find_customer, get_reservations, create_reservation, get_hotels, get_rooms]
)