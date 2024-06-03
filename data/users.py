import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    address: str
    permanent_address: str


student = User(full_name='Vasya Pupkin', email='vsya@gmail.com', address='sovet union', permanent_address='ne dom i ne ulitsa')