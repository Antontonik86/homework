import requests
import inspect
import pprint


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = [attribute
                  for attribute in dir(obj)
                  if not callable(getattr(obj, attribute)) and not attribute.startswith('__')]
    info['attributes'] = attributes



    methods = [method
               for method in dir(obj)
               if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods
    info['module'] = getattr(obj, '__module__', 'N/A')

    return info


number_info = introspection_info(42)
print(number_info)


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        pass


example_instance = ExampleClass(10)
class_info = introspection_info(example_instance)
print(class_info)
