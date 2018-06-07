from app import app
from flask_jwt_extended import JWTManager
app.config['SECRET_KEY'] = 'secretkey'
jwt = JWTManager(app)
app.run(debug=True)
