import unittest

from followthemoney.types import registry


class UrlsTest(unittest.TestCase):

    def test_normalise_set(self):
        t = registry.name
        self.assertEqual(t.normalize_set(None), [])
        self.assertEqual(t.normalize_set('boban'), ['boban'])
        self.assertEqual(t.normalize_set(['boban']), ['boban'])

    def test_ref(self):
        t = registry.name
        self.assertEqual(t.ref(''), None)
        self.assertEqual(t.ref('banana'), 'n:banana')
        nt, v = registry.deref('n:banana')
        self.assertEqual(v, 'banana')
        self.assertEqual(t, nt)

    def test_funcs(self):
        t = registry.name
        self.assertEqual(t.country_hint('banana'), None)
        self.assertEqual(str(t), 'name')
        self.assertEqual(hash(t), hash('name'))
