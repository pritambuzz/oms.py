from uuid import uuid4
import pytest

# --------
# Fixtures
# --------


@pytest.fixture
def f():
    def work(prefix: str = ''):
        return f'{prefix}{uuid4().hex}'

    return work


@pytest.fixture
def micro():
    import micro

    return micro


@pytest.fixture
def service(micro):
    return micro.Service(name='service')


@pytest.fixture
def flask(f, service):
    service.add(f)
    return service._flask


# -----
# Tests
# -----


def test_basic_service_registation(f, service):
    service.add(f=f)

    assert 'work' in service.endpoints


def test_named_service_registation(f, service):
    service.add(f=f, name='test')

    assert 'test' in service.endpoints


def test_custom_uri_service_registation(f, service):
    service.add(f=f, name='test', path='/not-test')

    assert 'test' in service.endpoints
    assert service.endpoints['test']['path'] == '/not-test'


def test_argument_detection(f, service):
    service.add(f=f)

    assert 'work' in service.endpoints
    assert 'prefix' in service.endpoints['work']['f'].__annotations__


def test_yaml_generation(f, service):
    service.add(f=f, name='hi', path='/bye')

    data = service._render()
    assert 'oms' in data
    assert 'actions' in data

    assert data['actions']['hi']['http']['path'] == '/bye'
    assert data['actions']['hi']['http']['method'] == 'get'
