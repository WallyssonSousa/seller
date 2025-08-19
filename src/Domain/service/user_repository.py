from abc import ABC, abstractmethod
from Domain.service.user_service import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User ):
        pass
    
    @abstractmethod
    def search_email(self, email: str) -> User:
        pass
    
    @abstractmethod
    def list_all(self) -> list[User]:
        pass
        