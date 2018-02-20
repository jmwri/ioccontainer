# ioccontainer

## Retrieving the container
Accessing the container is as simple as `from ioccontainer import c`. You can now use `c` to set up service providers and access services.

## Defining a service
```
from ioccontainer import c

class MyService:
    def __init__(self, val: int=1):
        self.val = val

def provide_my_service():
    return MyService()

c.provide(MyService, provide_my_service)
```

You can also use the `@provider` decorator.
```
from ioccontainer import c, provider

@provider(MyService)
def provide_my_service():
    return MyService()
```

## Using a service
```
from ioccontainer import c

my_service = c.get(MyService)
```

You can also use the `@inject` decorator. You can specify which service to inject into a variable as an argument, or use annotations.
```
from ioccontainer import inject

@inject(my_service=MyService)
def get_val_from_specified_service(my_service):
    return my_service.val

@inject('my_service')
def get_val_from_annotated_service(my_service: MyService):
    return my_service.val
```

You can specify as many injections as you want inside of the `@inject` decorator.

```
from ioccontainer import inject
@inject('db', 'my_service', users=UserRepository)
def do_something(db: DatabaseAdapter, action, my_service: MyService, users):
    pass

do_something(action='some_action')
```

## Scopes
There are different scopes that you can apply to services.

### NO_SCOPE
A new instance of the service will be created each time it is resolved. This is the default scope.

```
from ioccontainer import c, provider, scopes

@provider(MyService, scopes.NO_SCOPE)
def provide_my_service():
    return MyService()

first = c.get(MyService)
second = c.get(MyService)
print(first.val)  # 1
print(second.val)  # 1

first.val = 2
print(first.val)  # 2
print(second.val)  # 1
```

### SINGLETON
The same instance of the service will be created each time it is resolved

```
from ioccontainer import c, provider, scopes

@provider(MyService, scopes.SINGLETON)
def provide_my_service():
    return MyService()

first = c.get(MyService)
second = c.get(MyService)
print(first.val)  # 1
print(second.val)  # 1

first.val = 2
print(first.val)  # 2
print(second.val)  # 2
```

### THREAD
The same instance of the service will be created each time it is resolved within a thread.

```
from ioccontainer import provider, scopes

@provider(MyService, scopes.THREAD)
def provide_my_service():
    return MyService()
```

## Running tests
### Install the package with test dependencies
`pip install -e ".[test]"`

### Run tox
`tox`