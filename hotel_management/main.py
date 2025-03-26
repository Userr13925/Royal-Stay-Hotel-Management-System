from datetime import datetime, timedelta
from models.guest import Guest
from models.room import Room, RoomType
from models.booking import Booking
from models.payment import Payment, PaymentMethod
from models.service import Service, ServiceType
from models.review import Review
from services.notification_service import NotificationService
from services.loyalty_service import LoyaltyService

def main():
    # Create a guest
    guest1 = Guest("G001", "John Doe", "john.doe@email.com", "1234567890")
    print("Guest created:", guest1)
    
    # Create a room
    room1 = Room("101", RoomType.DOUBLE, 150.00, ["Wi-Fi", "TV", "Mini-Bar"])
    print("\nRoom created:", room1)
    
    # Create a booking
    check_in = datetime.now() + timedelta(days=7)
    check_out = check_in + timedelta(days=3)
    booking1 = Booking("B001", guest1, room1, check_in, check_out, num_guests=2)
    print("\nBooking created:", booking1)
    
    # Add a service to the booking
    service1 = Service("S001", ServiceType.ROOM_SERVICE, "Breakfast in bed", 25.00)
    booking1.add_service(service1)
    print("\nService added to booking:", service1)
    
    # Calculate total cost
    print(f"\nTotal booking cost: ${booking1.calculate_total_cost():.2f}")
    
    # Apply loyalty discount
    guest1.add_loyalty_points(5000)  # Add some points
    discount, points_used = LoyaltyService.apply_loyalty_discount(guest1, booking1)
    if discount > 0:
        print(f"\nApplied loyalty discount: ${discount:.2f} (using {points_used} points)")
        print(f"New booking total: ${booking1.calculate_total_cost():.2f}")
        print(f"Remaining loyalty points: {guest1.loyalty_points}")
    
    # Process payment
    payment1 = Payment("P001", booking1, booking1.calculate_total_cost(), PaymentMethod.CREDIT_CARD)
    print("\nPayment processed:", payment1)
    
    # Send notifications
    NotificationService.send_booking_confirmation(guest1, booking1)
    NotificationService.send_payment_confirmation(guest1, payment1)
    
    # Add a review after stay
    review1 = Review("R001", guest1, booking1, 5, "Excellent stay, would recommend!")
    print("\nReview submitted:", review1)
    
    # Cancel a booking example
    # booking1.cancel()
    # NotificationService.send_booking_cancellation(guest1, booking1, booking1.calculate_total_cost())

if __name__ == "__main__":
    main()