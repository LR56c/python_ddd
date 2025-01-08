// db = db.getSiblingDB( 'admin' )
db.createUser( {
	user : 'user',
	pwd  : 'user',
	roles: [
		{ role: 'root', db: 'admin' }
	]
} )
