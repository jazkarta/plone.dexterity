from plone.testing import Layer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class PloneDexterityFixture(Layer):
    defaultBases = (PLONE_FIXTURE,)


PLONE_DEXTERITY_FIXTURE = PloneDexterityFixture()

PLONE_DEXTERITY_INTEGRATION_TESTING = IntegrationTesting(bases=(PLONE_DEXTERITY_FIXTURE,), name="PloneDexterityFixture:Integration")
PLONE_DEXTERITY_FUNCTIONAL_TESTING = FunctionalTesting(bases=(PLONE_DEXTERITY_FIXTURE,), name="PloneDexterityFixture:Functional")
