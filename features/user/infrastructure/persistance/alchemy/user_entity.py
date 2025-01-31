from datetime import datetime

from sqlalchemy import Column, String, UUID,  DateTime
from sqlalchemy.orm import relationship

from features.post.infrastructure.persistance.post_entity import PostEntity
from features.shared.infrastructure.alchemy_database import Base


class UserEntity( Base ):
	__tablename__ = "users"
	id = Column( UUID, primary_key=True, index=True )
	name = Column( String, nullable=False )
	email = Column( String, nullable=False, index=True, unique=True )
	created_at = Column( DateTime( timezone=True ), nullable=False, default=datetime.now() )
	posts = relationship( PostEntity, back_populates="user" )