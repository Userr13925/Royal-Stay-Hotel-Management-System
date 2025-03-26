from enum import Enum

class RoomType(Enum):
    """Enumeration of room types"""
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"
    DELUXE = "Deluxe"
    PRESIDENTIAL = "Presidential"

class Room:
    """Class representing a hotel room"""
    
    def __init__(self, room_number: str, room_type: RoomType, price_per_night: float, 
                 amenities: list = None, max_occupancy: int = 2):
        """
        Initialize a Room object
        
        Args:
            room_number (str): Unique room number/identifier
            room_type (RoomType): Type of the room
            price_per_night (float): Base price per night
            amenities (list, optional): List of amenities. Defaults to None.
            max_occupancy (int, optional): Maximum number of guests. Defaults to 2.
        """
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._amenities = amenities if amenities else []
        self._max_occupancy = max_occupancy
        self._is_available = True
    
    @property
    def room_number(self):
        return self._room_number
    
    @property
    def room_type(self):
        return self._room_type
    
    @property
    def price_per_night(self):
        return self._price_per_night
    
    @price_per_night.setter
    def price_per_night(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price_per_night = value
    
    @property
    def amenities(self):
        return self._amenities
    
    def add_amenity(self, amenity: str):
        """Add an amenity to the room"""
        if amenity not in self._amenities:
            self._amenities.append(amenity)
    
    def remove_amenity(self, amenity: str):
        """Remove an amenity from the room"""
        if amenity in self._amenities:
            self._amenities.remove(amenity)
    
    @property
    def is_available(self):
        return self._is_available
    
    @is_available.setter
    def is_available(self, value: bool):
        self._is_available = value
    
    def __str__(self):
        return (f"Room(Number: {self._room_number}, Type: {self._room_type.value}, "
                f"Price: ${self._price_per_night:.2f}/night, Available: {self._is_available}, "
                f"Amenities: {', '.join(self._amenities)})")