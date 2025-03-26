class Guest:
    """Class representing a hotel guest"""
    
    def __init__(self, guest_id: str, name: str, email: str, phone: str, address: str = None):
        """
        Initialize a Guest object
        
        Args:
            guest_id (str): Unique identifier for the guest
            name (str): Full name of the guest
            email (str): Email address of the guest
            phone (str): Contact phone number
            address (str, optional): Physical address. Defaults to None.
        """
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
        self._loyalty_points = 0
        self._reservations = []
    
    @property
    def guest_id(self):
        return self._guest_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("Phone number must be at least 7 digits")
        self._phone = value
    
    @property
    def loyalty_points(self):
        return self._loyalty_points
    
    def add_loyalty_points(self, points: int):
        """Add loyalty points to the guest's account"""
        if points <= 0:
            raise ValueError("Points must be positive")
        self._loyalty_points += points
    
    def redeem_loyalty_points(self, points: int):
        """Redeem loyalty points from the guest's account"""
        if points <= 0:
            raise ValueError("Points must be positive")
        if points > self._loyalty_points:
            raise ValueError("Not enough points to redeem")
        self._loyalty_points -= points
    
    def add_reservation(self, reservation):
        """Add a reservation to the guest's history"""
        self._reservations.append(reservation)
    
    def get_reservation_history(self):
        """Return the guest's reservation history"""
        return self._reservations
    
    def __str__(self):
        return (f"Guest(ID: {self._guest_id}, Name: {self._name}, Email: {self._email}, "
                f"Phone: {self._phone}, Loyalty Points: {self._loyalty_points})")