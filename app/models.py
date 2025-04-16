from . import db

# Contact Form Table
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<ContactMessage {self.name}>'

# Projects Table
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100))
    link = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Project {self.title}>'

class GalleryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(50), nullable=False)
    media_type = db.Column(db.String(10), nullable=False)  # 'image' or 'video'
    filename = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255))
    order = db.Column(db.Integer, default=0)