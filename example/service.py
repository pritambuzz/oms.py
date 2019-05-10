import micro
from uuid import uuid4

service = micro.Service(name='uuid')


@service.register(path='/uuid4', method='get')
def gen_uuid4(prefix: str) -> str:
    """Generates a UUID, with a given prefix."""
    return f'{prefix}{uuid4().hex}'


# Alternative Syntax:
# service.add(f=gen_uuid4)

if __name__ == '__main__':
    service.serve(ensure=True)
