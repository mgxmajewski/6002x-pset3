import pytest
from assertpy import assert_that
import random
from ps3b import SimpleVirus


class TestSimpleVirus:

    @pytest.fixture(autouse=True)
    def prepare_simple_virus(self, maxBirthProb, clearProb):
        self.simple_virus = SimpleVirus(maxBirthProb, clearProb)

    @pytest.mark.parametrize('maxBirthProb, clearProb', [(0.1, 0.2)])
    def test_get_max_birth_prob(self, maxBirthProb, clearProb):
        #Given
        virus = self.simple_virus
        #When
        result = virus.getMaxBirthProb()
        #Then
        assert_that(result).is_close_to(0.1, 3)

    @pytest.mark.parametrize('maxBirthProb, clearProb', [(0.1, 0.3)])
    def test_get_clear_prob(self):
        #Given
        virus = self.simple_virus
        #When
        result = virus.getClearProb()
        #Then
        assert_that(result).is_close_to(0.3, 3)

    def test_does_clear(self):
        assert False

    def test_reproduce(self):
        assert False
