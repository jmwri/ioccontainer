# py-container

## Retrieving the container
Accessing the container is as simple as `from py-container import container`. You can now use `container` to set up service providers and access services.

## Defining a service
```
from py-container import container

class MyService:
    def __init__(self, val: int=1):
        self.val = val

def provide_my_service():
    return MyService()

container.provide(MyService, provide_my_service)
```

You can also use the `@provider` decorator.
```
from py-container import container, provider

@provider(MyService)
def provide_my_service():
    return MyService()
```

## Using a service
```
from py-container import container

my_service = container.get(MyService)
```

You can also use the `@inject` decorator. You can specify which service to inject into a variable as an argument, or use annotations.
```
from py-container import container, inject

@inject(my_service=MyService)
def get_val_from_specified_service(my_service):
    return my_service.val

@inject('my_service')
def get_val_from_annotated_service(my_service: MyService):
    return my_service.val
```

You can specify as many injections as you want inside of the `@inject` decorator.

```
from py-container import inject
@inject('db', 'my_service', users=UserRepository)
def do_something(db: DatabaseAdapter, action, my_service: MyService, users):
    pass

do_something(action='some_action')
```

## Scopes
There are different scopes that you can apply to services:

### NO_SCOPE
A new instance of the service will be created each time it is resolved. This is the default scope.

```
from py-container import container, provider, NO_SCOPE

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
from py-container import container, provider, SINGLETON

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
from py-container import container, provider, THREAD

@provider(MyService, THREAD)
def provide_my_service():
    return MyService()
```