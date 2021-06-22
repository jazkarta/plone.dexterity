# -*- coding: utf-8 -*-
import unittest

from Products.GenericSetup.tests.common import DummyImportContext
from .layers import PLONE_DEXTERITY_INTEGRATION_TESTING


class ExportImportTests(unittest.TestCase):

    def test_export(self):
        # Make sure our exporter delegates to manage_FTPget()
        from plone.dexterity.content import Item
        from plone.dexterity.exportimport import \
            DexterityContentExporterImporter
        from Products.GenericSetup.tests.common import DummyExportContext

        class DummyItem(Item):
            def manage_FTPget(self):
                return 'title: Foo'
        item = DummyItem('test')

        export_context = DummyExportContext(None)
        exporter = DexterityContentExporterImporter(item)
        exporter.export(export_context, subdir=None, root=True)

        self.assertEqual(
            export_context._wrote[-1],
            ('.data', 'title: Foo', 'text/plain')
        )

    def test_import(self):
        # Make sure our importer delegates to PUT()
        from plone.dexterity.content import Item
        from plone.dexterity.exportimport import \
            DexterityContentExporterImporter

        class DummyItem(Item):
            def PUT(self, request, response):
                self.title = 'Foo'
        item = DummyItem('test')

        import_context = DummyImportContext(None)
        import_context._files['.data'] = 'title: Foo'
        importer = DexterityContentExporterImporter(item)
        importer.import_(import_context, None, root=True)

        self.assertEqual('Foo', item.Title())


class ExportImportIntegrationTests(unittest.TestCase):

    layer = PLONE_DEXTERITY_INTEGRATION_TESTING

    def test_import_py3(self):
        """In python 3 `.objects` is a byte array
        """
        from plone.dexterity.exportimport import \
            DexterityContentExporterImporter

        # Make sure import works in python 3
        import_context = DummyImportContext(None)
        import_context._files['.objects'] = b'Example1,Folder\nExample2,Folder\nPage1,Folder'
        importer = DexterityContentExporterImporter(self.layer["portal"])
        importer.import_(import_context, None, root=True)
