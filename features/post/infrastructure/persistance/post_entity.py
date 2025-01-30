from sqlalchemy import Column, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from features.shared.infrastructure.alchemy_database import Base


class PostEntity( Base ):
	__tablename__ = "posts"
	id = Column( UUID, primary_key=True, index=True )
	title = Column( String, nullable=False )
	content = Column( String, nullable=False )
	user_id = Column( UUID, ForeignKey( 'users.id' ) )
	user = relationship( "UserEntity", back_populates="posts" )
