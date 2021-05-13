import pytest
from assertpy import assert_that
import random
from ps3b import SimpleVirus


class TestSimpleVirus:

    # @pytest.fixture(autouse=True)
    # def prepare_simple_virus(self, maxBirthProb, clearProb):
    #     # random.seed(1)
    #
    #     # self.clearProb = clearProb
    #     # maxBirthProb = None
    #     # clearProb = None
    #     return SimpleVirus(maxBirthProb.param, clearProb.param)

    @pytest.mark.parametrize('maxBirthProb, clearProb', [(0.1, 0.2), (0.2, 0.2)])
    def test_get_max_birth_prob(self, maxBirthProb, clearProb):
        #Given
        # self.maxBirthProb = maxBirthProb
        # self.clearProb = clearProb
        virus = SimpleVirus(maxBirthProb, clearProb)
        #When
        result = virus.getMaxBirthProb()
        #Then
        assert_that(result).is_equal_to(0.1)

    def test_get_clear_prob(self):
        assert False

    def test_does_clear(self):
        assert False

    def test_reproduce(self):
        assert False
