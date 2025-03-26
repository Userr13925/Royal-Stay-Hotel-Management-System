import unittest
from models.room import Room, RoomType

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("201", RoomType.SUITE, 250.00, ["Wi-Fi", "TV", "Mini-Bar", "Jacuzzi"])
    
    def test_room_creation(self):
        self.assertEqual(self.room.room_number, "201")
        self.assertEqual(self.room.room_type, RoomType.SUITE)
        self.assertEqual(self.room.price_per_night, 250.00)
        self.assertEqual(len(self.room.amenities), 4)
        self.assertTrue(self.room.is_available)
    
    def test_amenity_management(self):
        self.room.add_amenity("Safe")
        self.assertIn("Safe", self.room.amenities)
        
        self.room.remove_amenity("TV")
        self.assertNotIn("TV", self.room.amenities)
    
    def test_price_validation(self):
        with self.assertRaises(ValueError):
            self.room.price_per_night = -100.00
    
    def test_availability(self):
        self.room.is_available = False
        self.assertFalse(self.room.is_available)

if __name__ == "__main__":
    unittest.main()