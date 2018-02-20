import pytest

from ioccontainer import c, provider, inject, scopes, exceptions


class MyService:
    def __init__(self, val: int=1):
        self.val = val


@provider(MyService)
def provide_my_service():
    return MyService()


@inject(my_service='my_service_singleton')
def increment_val(my_service):
    my_service.val = my_service.val + 1


def provide_my_service_singleton():
    return MyService(1)


c.singleton('my_service_singleton', provide_my_service_singleton)


@inject('my_service')
def test_injection(my_service: MyService):
    assert my_service.val is 1


@inject(my_service='my_service_singleton')
def test_singleton(my_service: MyService):
    assert my_service.val is 1
    increment_val()
    assert my_service.val is 2
    increment_val()
    assert my_service.val is 3


def test_invalid_scope():
    def provide():
        pass

    with pytest.raises(exceptions.ScopeError):
        c.provide('invalid_scope', provide, -1)


def test_duplicate_provider():
    def provide():
        pass

    with pytest.raises(exceptions.ProviderError):
        c.provide('duplicate_provider', provide)
        c.provide('duplicate_provider', provide)


def test_invalid_provider():
    with pytest.raises(exceptions.ProviderError):
        c.get('provider_doesnt_exist')


def test_invalid_service_name():
    with pytest.raises(exceptions.ProviderError):
        c.get({})


def test_no_provider_specified():
    @inject('my_param')
    def my_fn(my_param):
        pass

    with pytest.raises(exceptions.ParameterError):
        my_fn()


def test_multiple_params():
    @inject('ms1', ms2=MyService)
    def my_fn(one, two, three, four, ms1: MyService, ms2=None, five=None):
        assert one == 'one'
        assert two == 'two'
        assert three == 'three'
        assert four == 'four'
        assert five == 'five'
        assert isinstance(ms1, MyService)
        assert isinstance(ms2, MyService)

    my_fn('one', 'two', 'three', 'four', five='five')


def test_default_provided():
    @inject('ms')
    def my_fn(ms: MyService='default'):
        pass

    with pytest.raises(exceptions.ParameterError):
        my_fn()


def test_argument_provided():
    @inject('ms')
    def my_fn(ms: MyService):
        assert ms.val is 2

    ms = MyService(2)
    my_fn(ms)
