import unittest
from datetime import datetime, timedelta
from models.guest import Guest
from models.room import Room, RoomType
from models.booking import Booking
from models.service import Service, ServiceType

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("G002", "Bob Johnson", "bob@example.com", "9876543210")
        self.room = Room("301", RoomType.DELUXE, 200.00)
        self.check_in = datetime.now() + timedelta(days=14)
        self.check_out = self.check_in + timedelta(days=5)
        self.booking = Booking("B002", self.guest, self.room, self.check_in, self.check_out, 2)
    
    def test_booking_creation(self):
        self.assertEqual(self.booking.guest.name, "Bob Johnson")
        self.assertEqual(self.booking.room.room_number, "301")
        self.assertEqual(self.booking.num_nights, 5)
        self.assertFalse(self.booking._is_cancelled)
    
    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            Booking("B003", self.guest, self.room, self.check_out, self.check_in)
    
    def test_room_availability(self):
        self.assertFalse(self.room.is_available)
    
    def test_service_addition(self):
        service = Service("S002", ServiceType.TRANSPORTATION, "Airport pickup", 50.00)
        self.booking.add_service(service)
        self.assertEqual(len(self.booking._additional_services), 1)
        self.assertEqual(self.booking.calculate_total_cost(), 200.00 * 5 + 50.00)
    
    def test_cancellation(self):
        self.assertTrue(self.booking.cancel())
        self.assertTrue(self.booking._is_cancelled)
        self.assertTrue(self.room.is_available)
        # Test duplicate cancellation
        self.assertFalse(self.booking.cancel())

if __name__ == "__main__":
    unittest.main()