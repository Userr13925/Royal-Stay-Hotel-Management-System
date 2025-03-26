from datetime import datetime, timedelta
from typing import Optional

class Booking:
    """Class representing a room booking/reservation"""
    
    def __init__(self, booking_id: str, guest, room, check_in_date: datetime, 
                 check_out_date: datetime, num_guests: int = 1):
        """
        Initialize a Booking object
        
        Args:
            booking_id (str): Unique booking identifier
            guest (Guest): Guest making the booking
            room (Room): Room being booked
            check_in_date (datetime): Check-in date
            check_out_date (datetime): Check-out date
            num_guests (int, optional): Number of guests. Defaults to 1.
        """
        self._booking_id = booking_id
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._num_guests = num_guests
        self._booking_date = datetime.now()
        self._additional_services = []
        self._is_cancelled = False
        self._cancellation_date = None
        
        # Validate the booking
        self._validate_booking()
        
        # Mark room as unavailable
        self._room.is_available = False
        
        # Add to guest's reservation history
        self._guest.add_reservation(self)
    
    def _validate_booking(self):
        """Validate the booking parameters"""
        if self._check_in_date >= self._check_out_date:
            raise ValueError("Check-out date must be after check-in date")
        
        if self._num_guests > self._room._max_occupancy:
            raise ValueError(f"Room can only accommodate {self._room._max_occupancy} guests")
        
        if not self._room.is_available:
            raise ValueError("Room is not available for booking")
    
    @property
    def booking_id(self):
        return self._booking_id
    
    @property
    def guest(self):
        return self._guest
    
    @property
    def room(self):
        return self._room
    
    @property
    def check_in_date(self):
        return self._check_in_date
    
    @property
    def check_out_date(self):
        return self._check_out_date
    
    @property
    def num_nights(self):
        """Calculate number of nights for the stay"""
        return (self._check_out_date - self._check_in_date).days
    
    def add_service(self, service):
        """Add an additional service to the booking"""
        self._additional_services.append(service)
    
    def calculate_total_cost(self):
        """Calculate the total cost of the booking"""
        base_cost = self.num_nights * self._room.price_per_night
        services_cost = sum(service.price for service in self._additional_services)
        return base_cost + services_cost
    
    def cancel(self):
        """Cancel the booking"""
        if not self._is_cancelled:
            self._is_cancelled = True
            self._cancellation_date = datetime.now()
            self._room.is_available = True
            return True
        return False
    
    def __str__(self):
        status = "Cancelled" if self._is_cancelled else "Confirmed"
        return (f"Booking(ID: {self._booking_id}, Guest: {self._guest.name}, "
                f"Room: {self._room.room_number}, Status: {status}, "
                f"Dates: {self._check_in_date.strftime('%Y-%m-%d')} to "
                f"{self._check_out_date.strftime('%Y-%m-%d')}, "
                f"Nights: {self.num_nights}, Total: ${self.calculate_total_cost():.2f})")