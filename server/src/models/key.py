from sqlalchemy import Column, VARCHAR, ForeignKey, String
from sqlalchemy.orm import relationship
from uuid import uuid4

from src.database import Base
from src.database.mixins import TimestampMixin


class Key(Base, TimestampMixin):
    __tablename__ = "keys"
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    userId = Column(String(36), ForeignKey("users.id"))
    publicKey = Column(VARCHAR(255), nullable=False)
    privateKey = Column(VARCHAR(255), nullable=False)
    user = relationship("User", back_populates="key")
