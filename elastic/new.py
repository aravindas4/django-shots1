

def checker(function):
    def _checker(*args):
        if len(args) > 4:
            raise Exception(
                "Number of args shall be less than or equal to 4"
            )
        return function(*args)
    return _checker


@checker
def compute_sum(*args):
    return sum(args)

# print(compute_sum(1, 7, 7, 8, 9))


def generate_less_than(base):
    start = 0

    while start < base:
        yield start
        start += 1


class User:
    pass


class Org:
    pass

class CSVImport:
    file
    status: IN ,COM


class Profile:
    Org: FK
    User: OneToOne


class Product:
    Org: FK "products"




GET: "v1/org/products/?name="
POST: "v1/org/products/"

{"name": ""} 400

{"id": , name, }
200 OK refer:


201 created
refe:

SELECT org_name FROM org ORDER_BY org_name LIMIT 20;


Org.objects.annotate(
    num_of_product=Count("products")
).order_by("num_of_product").values("org_name")
