import pytest
from assertpy import assert_that
import random
from ps3b import SimpleVirus, NoChildException, Patient, ResistantVirus


class TestSimpleVirus:

    @pytest.fixture(autouse=True)
    def prepare_simple_virus(self, maxBirthProb, clearProb):
        self.simple_virus = SimpleVirus(maxBirthProb, clearProb)

    @pytest.mark.parametrize('maxBirthProb, clearProb', [(0.1, 0.2)])
    def test_get_max_birth_prob(self):
        # Given
        virus = self.simple_virus
        # When
        result = virus.getMaxBirthProb()
        # Then
        assert_that(result).is_equal_to(0.1)

    @pytest.mark.parametrize('maxBirthProb, clearProb', [(0.1, 0.3)])
    def test_get_clear_prob(self):
        # Given
        virus = self.simple_virus
        # When
        result = virus.getClearProb()
        # Then
        assert_that(result).is_equal_to(0.3)

    @pytest.mark.parametrize(
        'maxBirthProb, clearProb, expected',
        [(0.1, 0.8, True), (0.1, 0.6, True), (0.1, 0.3, False)])
    def test_does_clear(self, expected):
        # Given
        virus = self.simple_virus
        # When
        result = virus.doesClear()
        # Then
        print(result)
        assert_that(result).is_equal_to(expected)

    @pytest.mark.parametrize('maxBirthProb, clearProb, popDensity',
                             [(0.9, 0.8, 0.2), (0.8, 0.6, 0.3)])
    def test_reproduce(self, popDensity):
        # Given
        virus = self.simple_virus
        # When
        result = virus.reproduce(popDensity)
        # Then
        assert_that(result).is_instance_of(SimpleVirus)

    @pytest.mark.parametrize('maxBirthProb, clearProb, popDensity',
                             [(0.2, 0.8, 0.2), (0.1, 0.6, 0.3)])
    def test_reproduce(self, popDensity):
        # Given
        virus = self.simple_virus
        # When
        result = virus.reproduce
        # Then
        assert_that(result).raises(NoChildException).when_called_with(popDensity)


class TestPatient:

    @pytest.fixture(autouse=True)
    def prepare_patient(self, viruses, maxPop):
        self.patient = Patient(viruses, maxPop)

    def test_get_viruses(self):
        assert False

    def test_get_max_pop(self):
        assert False

    def test_get_total_pop(self):
        assert False

    @pytest.mark.parametrize('viruses, maxPop, expected',
                             [([SimpleVirus(1.0, 1.0)], 100, 0),
                              ([SimpleVirus(0.04, 0.07), SimpleVirus(0.12, 0.16)], 6, 2)])
    def test_update(self, viruses, maxPop, expected):
        # Given
        patient = self.patient
        # When
        patient.update()
        # Then
        result = patient.getTotalPop()
        assert_that(result).is_equal_to(expected)


class TestResistantVirus:

    @pytest.fixture(autouse=True)
    def prepare_resistant_virus(self, maxBirthProb, clearProb, resistances, mutProb):
        self.resistant_virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)

    @pytest.mark.parametrize(
        'maxBirthProb, clearProb, resistances, mutProb',
        [(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)])
    def test_is_resistant_to(self):
        # Given
        virus = self.resistant_virus
        drug = 'drug1'
        # When
        result = virus.isResistantTo(drug)
        # Then
        assert_that(result).is_true()

    def test_reproduce(self):
        assert False
