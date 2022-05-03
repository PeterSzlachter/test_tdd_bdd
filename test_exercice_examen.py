import logging

from behave import *
import pytest
from exercice_examen import get_grade, FmException, setup_logger
from pytest_bdd import scenario, given, when, then

setup_logger()


@scenario('tutorial.feature', 'run a simple test')
def step():
    pass


logging.info("Début des tests")


@given('we have behave installed')
def test_grade_integer():
    logging.info("Test des nombres entiers")
    assert get_grade(note_controle_continue=25, note_examen=75) == "A"
    assert get_grade(note_controle_continue=24, note_examen=75) == "A"
    assert get_grade(note_controle_continue=20, note_examen=31) == "B"
    assert get_grade(note_controle_continue=21, note_examen=29) == "B"
    assert get_grade(note_controle_continue=20, note_examen=29) == "C"
    assert get_grade(note_controle_continue=10, note_examen=21) == "C"
    assert get_grade(note_controle_continue=15, note_examen=15) == "C"
    assert get_grade(note_controle_continue=15, note_examen=14) == "D"
    assert get_grade(0, 0) == "D"
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=26, note_examen=75)
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=10, note_examen=76)
        get_grade(note_controle_continue=26, note_examen=45)


@when('we implement a test')
def test_grade_negative_numbers():
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=-1, note_examen=0)
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=-15, note_examen=-1)


@then('behave will test it for us!')
def test_grade_decimal():
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=3.2, note_examen=0.5)


def test_grade_whitespace():
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue="", note_examen="")


def test_grade_letter():
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue="A", note_examen="")
        get_grade(note_controle_continue="", note_examen="B")


def test_grade_boolean():
    with pytest.raises(FmException):
        logging.warning("Déclenchement d'une erreur, valeur d'entrée érronée")
        get_grade(note_controle_continue=True, note_examen=False)
        get_grade(note_controle_continue=False, note_examen=False)
        get_grade(note_controle_continue=True, note_examen=True)


logging.info("Fin des tests")
