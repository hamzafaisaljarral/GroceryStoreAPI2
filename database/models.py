import datetime
from mongoengine import Document, EmailField, StringField, IntField, BooleanField, EmbeddedDocumentField, \
    EmbeddedDocument, DateTimeField, ObjectIdField, queryset_manager, DynamicEmbeddedDocument
from flask_bcrypt import generate_password_hash, check_password_hash


class Access(EmbeddedDocument):
    """
    Custom EmbeddedDocument to set user authorizations.
    :param user: boolean value to signify if user is a user
    :param admin: boolean value to signify if user is an admin
    """
    client = BooleanField(default=True)
    admin = BooleanField(default=False)


class User(Document):
    gender = {
        'M': 'Male',
        'F': 'Female'
    }

    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=25)
    gender = StringField(required=True, choices=gender.keys(), min_length=1)
    phone_number = StringField(required=True, min_length=5)
    role = EmbeddedDocumentField(Access, default=Access(client=True, admin=False))
    salt = StringField()

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    # Use documentation from BCrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)

    # Use documentation from BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        if self._created:
            self.generate_pw_hash()
        super(User, self).save(*args, **kwargs)


class ProductReview(EmbeddedDocument):
    userID = ObjectIdField(required=True)
    barcode = IntField(required=True)
    review = StringField(required=True)
    createdAt = DateTimeField(default=datetime.datetime.utcnow)

    @property
    def productserializer(self):
        user = User.objects.get(id=self.userID)
        return{
            'name': user.email,
            'review': self.review
        }


class Product(Document):
    name = StringField(min_length=2)
    barcode = IntField(min_length=1)
    brand = StringField(min_length=2)
    description = StringField(min_length=3)
    price = IntField(min_lenght=1)
    available = BooleanField()
    review = EmbeddedDocumentField(ProductReview, required=False)

    @property
    def serializer(self):
        reviews = []
        if self.review:
            reviews.append(self.review.productserializer)
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'available': self.available,
            'review': reviews[:2]

        }






