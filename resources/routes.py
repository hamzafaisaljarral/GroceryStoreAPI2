from .auth import SignupApi, LoginApi
from .products import ADDProductAPI, ADDProductReviewAPI, ProductSearchAPI


def initialize_routes(api):
    api.add_resource(SignupApi, '/user/register')
    api.add_resource(LoginApi, '/user/login')
    api.add_resource(ADDProductAPI, '/product')
    api.add_resource(ADDProductReviewAPI, '/product/review')
    api.add_resource(ProductSearchAPI, '/product/search')

