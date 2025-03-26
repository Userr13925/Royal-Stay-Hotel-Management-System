import unittest
from datetime import datetime, timedelta
from models.guest import Guest
from models.room import Room, RoomType
from models.booking import Booking

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("G001", "Alice Smith", "alice@example.com", "1234567890")
        self.room = Room("101", RoomType.DOUBLE, 150.00)
        check_in = datetime.now() + timedelta(days=7)
        check_out = check_in + timedelta(days=3)
        self.booking = Booking("B001", self.guest, self.room, check_in, check_out)
    
    def test_guest_creation(self):
        self.assertEqual(self.guest.name, "Alice Smith")
        self.assertEqual(self.guest.email, "alice@example.com")
        self.assertEqual(self.guest.phone, "1234567890")
        self.assertEqual(self.guest.loyalty_points, 0)
    
    def test_loyalty_points(self):
        self.guest.add_loyalty_points(1000)
        self.assertEqual(self.guest.loyalty_points, 1000)
        
        with self.assertRaises(ValueError):
            self.guest.add_loyalty_points(-50)
        
        self.guest.redeem_loyalty_points(500)
        self.assertEqual(self.guest.loyalty_points, 500)
        
        with self.assertRaises(ValueError):
            self.guest.redeem_loyalty_points(600)  # Not enough points
    
    def test_reservation_history(self):
        self.assertEqual(len(self.guest.get_reservation_history()), 1)
        self.assertIsInstance(self.guest.get_reservation_history()[0], Booking)
    
    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.guest.email = "invalid-email"
    
    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            self.guest.phone = "123"

if __name__ == "__main__":
    unittest.main()