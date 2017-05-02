"""Tests for rdflib_pyld_compat."""
import unittest
from rdflib import Graph, URIRef, Literal, BNode
from rdflib_pyld_compat import pyld_jsonld_from_rdflib_graph, rdflib_graph_from_pyld_jsonld


class TestCompat(unittest.TestCase):
    """Test class for rdflib_pyld_compat."""

    def test01_pyld_jsonld_from_rdflib_graph(self):
        """Convert PyLD data to rdflib graphs."""
        g = Graph()
        g += [(URIRef(u's1'), URIRef(u'p1'), URIRef(u'o1'))]
        j = pyld_jsonld_from_rdflib_graph(g)
        self.assertEqual(len(j), 1)
        jj = j[0]
        self.assertEqual(jj['@id'], 's1')
        self.assertEqual(jj['p1'][0]['@id'], 'o1')
        #
        g = Graph()
        g += [(URIRef(u's2'), URIRef(u'p2'), Literal(u'algae'))]
        j = pyld_jsonld_from_rdflib_graph(g)
        self.assertEqual(len(j), 1)
        jj = j[0]
        self.assertEqual(jj['@id'], 's2')
        ss = jj['p2'][0]
        self.assertFalse('@type' in ss)
        self.assertEqual(ss['@value'], 'algae')

    def test02_rdflib_graph_from_pyld_jsonld(self):
        """Convert rdflib graphs to PyLD."""
        j = [{'@id': 'http://example.org/s1', 'http://example.org/p1': [{'@id': 'http://example.org/o1'}]}]
        g = rdflib_graph_from_pyld_jsonld(j)
        self.assertEqual(len(g), 1)
        for s, p, o in g:
            self.assertEqual(str(s), 'http://example.org/s1')
            self.assertTrue(isinstance(s, URIRef))
            self.assertEqual(str(p), 'http://example.org/p1')
            self.assertTrue(isinstance(p, URIRef))
            self.assertEqual(str(o), 'http://example.org/o1')
            self.assertTrue(isinstance(o, URIRef))
        #
        j = [{'@id': 'http://example.org/s1', 'http://example.org/p1': ['kangaroo']}]
        g = rdflib_graph_from_pyld_jsonld(j)
        self.assertEqual(len(g), 1)
        for s, p, o in g:
            self.assertEqual(str(s), 'http://example.org/s1')
            self.assertTrue(isinstance(s, URIRef))
            self.assertEqual(str(p), 'http://example.org/p1')
            self.assertTrue(isinstance(p, URIRef))
            self.assertEqual(str(o), 'kangaroo')
            self.assertTrue(isinstance(o, Literal))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompat)
    unittest.TextTestRunner().run(suite)
