# py-ioc

## Retrieving the container
Accessing the container is as simple as `from py-ioc import container`. You can now use `container` to set up service providers and access services.

## Defining a service
```
from py-ioc import container

class MyService:
    def __init__(self, val: int=1):
        self.val = val

def provide_my_service():
    return MyService()

container.provide(MyService, provide_my_service)
```

You can also use the `@provider` decorator.
```
from py-ioc import container, provider

@provider(MyService)
def provide_my_service():
    return MyService()
```

## Using a service
```
from py-ioc import container

def get_val(my_service):
    return my_service.val
my_service = container.get(MyService)
print(get_val(my_service))  # 1
```

You can also use the `@inject` decorator.
```
from py-ioc import container, inject

@inject(my_service=MyService)
def get_val(my_service):
    return my_service.val
print(get_val())  # 1

@inject('my_service')
def get_val2(my_service: MyService):
    return my_service.val
print(get_val2())  # 1
```

## Scopes
There are different scopes that you can apply to services:

### NO_SCOPE
A new instance of the service will be created each time it is resolved. This is the default scope.

```
from py-ioc import container, provider, NO_SCOPE

@provider(MyService, NO_SCOPE)
def provide_my_service():
    return MyService()

first = container.get(MyService)
second = container.get(MyService)
print(first.val)  # 1
print(second.val)  # 1
first.val = 2
print(first.val)  # 2
print(second.val)  # 1
```

### SINGLETON
The same instance of the service will be created each time it is resolved

```
from py-ioc import container, provider, SINGLETON

@provider(MyService, SINGLETON)
def provide_my_service():
    return MyService()

first = container.get(MyService)
second = container.get(MyService)
print(first.val)  # 1
print(second.val)  # 1
first.val = 2
print(first.val)  # 2
print(second.val)  # 2
```

### THREAD
The same instance of the service will be created each time it is resolved within a thread.

```
from py-ioc import container, provider, THREAD

@provider(MyService, THREAD)
def provide_my_service():
    return MyService()
```