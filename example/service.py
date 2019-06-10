import omg
from uuid import uuid4

service = omg.Microservice(name='uuid')


@service.register()
def new(prefix: str) -> str:
    """Generates a UUID, with a given prefix."""
    return f'{prefix}{uuid4().hex}'


# Alternative Syntax:
# service.add(f=new)

if __name__ == '__main__':
    service.serve(ensure=True)
