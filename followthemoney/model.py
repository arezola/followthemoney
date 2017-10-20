
class Model(object):
    """A collection of schemata."""

    def __init__(self, data):
        self.schemata = {}

        # for section in Schema.SECTIONS:
        #     for name, sconfig in data.get(section, {}).items():
        #         if name in self.schemata:
        #             raise TypeError("Duplicate schema name: %r" % name)
        #         self.schemata[name] = Schema(self, section, name, sconfig)

    def get(self, name):
        schema = self.schemata.get(name)
        if schema is None:
            raise TypeError("No such schema: %r" % name)
        return schema

    def merge_entity_schema(self, left, right):
        """Select the most narrow of two schemata.

        When indexing data from a dataset, an entity may be declared as a
        LegalEntity in one query, and as a Person in another. This function
        will select the most specific of two schemata offered. In the example,
        that would be Person.
        """
        if left == right:
            return left
        lefts = self.get(left)
        lefts = [s.name for s in lefts.schemata]
        if right in lefts:
            return left

        rights = self.get(right)
        rights = [s.name for s in rights.schemata]
        if left in rights:
            return right

        for left in lefts:
            for right in rights:
                if left == right:
                    return left

    def to_dict(self):
        data = {}
        for name, schema in self.schemata.items():
            if not schema.hidden:
                data[name] = schema
        return data

    def __iter__(self):
        return iter(self.schemata.values())

    def __repr__(self):
        return '<Model(%r)>' % self.schemata