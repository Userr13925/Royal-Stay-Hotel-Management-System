class NotificationService:
    """Service for sending notifications to guests"""
    
    @staticmethod
    def send_booking_confirmation(guest, booking):
        """Send booking confirmation to guest"""
        subject = "Booking Confirmation"
        message = (f"Dear {guest.name},\n\n"
                  f"Your booking has been confirmed.\n"
                  f"Booking ID: {booking.booking_id}\n"
                  f"Room: {booking.room.room_number} ({booking.room.room_type.value})\n"
                  f"Check-in: {booking.check_in_date.strftime('%Y-%m-%d')}\n"
                  f"Check-out: {booking.check_out_date.strftime('%Y-%m-%d')}\n"
                  f"Total cost: ${booking.calculate_total_cost():.2f}\n\n"
                  f"Thank you for choosing Royal Stay Hotel!")
        
        # In a real implementation, this would send an email or push notification
        print(f"=== Email Notification ===\nTo: {guest.email}\nSubject: {subject}\n\n{message}\n")
    
    @staticmethod
    def send_payment_confirmation(guest, payment):
        """Send payment confirmation to guest"""
        subject = "Payment Confirmation"
        message = (f"Dear {guest.name},\n\n"
                  f"Your payment of ${payment.amount:.2f} has been received.\n"
                  f"Payment ID: {payment.payment_id}\n"
                  f"Method: {payment.payment_method.value}\n"
                  f"Date: {payment.payment_date.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                  f"Thank you for choosing Royal Stay Hotel!")
        
        print(f"=== Email Notification ===\nTo: {guest.email}\nSubject: {subject}\n\n{message}\n")
    
    @staticmethod
    def send_booking_cancellation(guest, booking, refund_amount=None):
        """Send booking cancellation notification to guest"""
        subject = "Booking Cancellation"
        message = (f"Dear {guest.name},\n\n"
                  f"Your booking (ID: {booking.booking_id}) has been cancelled.\n")
        
        if refund_amount is not None:
            message += f"A refund of ${refund_amount:.2f} will be processed.\n"
        
        message += "\nWe hope to serve you again in the future."
        
        print(f"=== Email Notification ===\nTo: {guest.email}\nSubject: {subject}\n\n{message}\n")