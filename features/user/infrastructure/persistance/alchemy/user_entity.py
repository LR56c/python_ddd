from sqlalchemy import Column, DATETIME, String, UUID
from sqlalchemy.orm import relationship

from features.shared.infrastructure.alchemy_database import Base


class UserEntity( Base ):
	__tablename__ = "users"
	id = Column( UUID, primary_key=True, index=True )
	name = Column( String, nullable=False )
	email = Column( String, nullable=False, index=True, unique=True )
	created_at = Column( DATETIME( timezone=True ), nullable=False )
	posts = relationship( "PostEntity", back_populates="user" )