class LoyaltyService:
    """Service for managing guest loyalty points"""
    
    POINTS_PER_DOLLAR = 10  # 10 points for every $1 spent
    POINTS_REDEMPTION_RATE = 100  # 100 points = $1 discount
    
    @classmethod
    def calculate_points_earned(cls, amount_spent: float):
        """Calculate loyalty points earned based on amount spent"""
        return int(amount_spent * cls.POINTS_PER_DOLLAR)
    
    @classmethod
    def calculate_discount_from_points(cls, points: int):
        """Calculate discount amount from loyalty points"""
        return points / cls.POINTS_REDEMPTION_RATE
    
    @classmethod
    def apply_loyalty_discount(cls, guest, booking):
        """
        Apply loyalty discount to a booking if guest has enough points
        
        Returns:
            tuple: (discount_amount, points_used) if applied, (0, 0) otherwise
        """
        if guest.loyalty_points <= 0:
            return 0, 0
        
        # Calculate maximum possible discount
        max_discount = cls.calculate_discount_from_points(guest.loyalty_points)
        booking_total = booking.calculate_total_cost()
        
        # Can't discount more than the booking total
        discount_amount = min(max_discount, booking_total)
        points_used = int(discount_amount * cls.POINTS_REDEMPTION_RATE)
        
        # Apply the discount
        guest.redeem_loyalty_points(points_used)
        return discount_amount, points_used