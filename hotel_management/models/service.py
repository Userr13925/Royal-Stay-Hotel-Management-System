from enum import Enum

class ServiceType(Enum):
    """Enumeration of service types"""
    ROOM_SERVICE = "Room Service"
    HOUSEKEEPING = "Housekeeping"
    LAUNDRY = "Laundry"
    TRANSPORTATION = "Transportation"
    SPA = "Spa"
    OTHER = "Other"

class Service:
    """Class representing an additional service request"""
    
    def __init__(self, service_id: str, service_type: ServiceType, description: str, 
                 price: float, request_time: str = None):
        """
        Initialize a Service object
        
        Args:
            service_id (str): Unique service identifier
            service_type (ServiceType): Type of service
            description (str): Description of the service
            price (float): Price of the service
            request_time (str, optional): Time the service is requested. Defaults to None.
        """
        self._service_id = service_id
        self._service_type = service_type
        self._description = description
        self._price = price
        self._request_time = request_time
        self._is_fulfilled = False
    
    @property
    def service_id(self):
        return self._service_id
    
    @property
    def service_type(self):
        return self._service_type
    
    @property
    def description(self):
        return self._description
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @property
    def is_fulfilled(self):
        return self._is_fulfilled
    
    def fulfill(self):
        """Mark the service as fulfilled"""
        self._is_fulfilled = True
    
    def __str__(self):
        status = "Fulfilled" if self._is_fulfilled else "Pending"
        return (f"Service(ID: {self._service_id}, Type: {self._service_type.value}, "
                f"Description: {self._description}, Price: ${self._price:.2f}, "
                f"Status: {status})")