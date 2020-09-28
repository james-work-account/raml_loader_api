import yaml
import os


class Loader(yaml.SafeLoader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename, part = os.path.join(
            self._root, "..", self.construct_scalar(node)).rsplit('.', 1)
        with open("%s.raml" % filename, 'r') as f:
            return yaml.load(f, Loader)[part]


Loader.add_constructor('!include', Loader.include)
