from datetime import datetime

class Review:
    """Class representing a guest review/feedback"""
    
    def __init__(self, review_id: str, guest, booking, rating: int, 
                 comment: str = None, review_date: datetime = None):
        """
        Initialize a Review object
        
        Args:
            review_id (str): Unique review identifier
            guest (Guest): Guest making the review
            booking (Booking): Booking being reviewed
            rating (int): Rating (1-5)
            comment (str, optional): Review comment. Defaults to None.
            review_date (datetime, optional): Date of review. Defaults to current datetime.
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        
        self._review_id = review_id
        self._guest = guest
        self._booking = booking
        self._rating = rating
        self._comment = comment
        self._review_date = review_date if review_date else datetime.now()
    
    @property
    def review_id(self):
        return self._review_id
    
    @property
    def guest(self):
        return self._guest
    
    @property
    def booking(self):
        return self._booking
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        self._comment = value
    
    @property
    def review_date(self):
        return self._review_date
    
    def __str__(self):
        return (f"Review(ID: {self._review_id}, Guest: {self._guest.name}, "
                f"Rating: {self._rating}/5, Date: {self._review_date.strftime('%Y-%m-%d')}, "
                f"Comment: {self._comment[:30] + '...' if self._comment and len(self._comment) > 30 else self._comment})")