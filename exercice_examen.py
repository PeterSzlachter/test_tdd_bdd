import logging


class FmException(Exception):
    pass


def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        filename="infos.log",
                        filemode="a",
                        format="%(asctime)s -- %(levelname)s -- %(message)s",
                        force=True)
    logging.info("Setup logger")


setup_logger()


def get_grade(note_controle_continue, note_examen):
    if type(note_examen) == bool or type(note_controle_continue) == bool:
        raise FmException("Pas de bool")

    check_ne = isinstance(note_examen, int)
    check_ncc = isinstance(note_controle_continue, int)

    if not check_ncc or not check_ne:
        raise FmException(f"Mauvais type de valeur,"
                          f" type note examen : {type(note_examen)} "
                          f"type note cc : {type(note_controle_continue)} "
                          f"Valeur attendu {type(int())}")

    if note_examen > 75 or note_examen < 0:
        raise FmException

    if note_controle_continue < 0 or note_controle_continue > 25:
        raise FmException

    total_note = note_examen + note_controle_continue

    if 0 <= total_note <= 100:
        if total_note < 30:
            return "D"
        elif 30 <= total_note < 50:
            return "C"
        elif 50 <= total_note < 70:
            return "B"
        elif 70 <= total_note <= 100:
            return "A"
        else:
            raise FmException("FM")
    else:
        raise FmException("FM")


def affichage_note():
    print(f"Vous avez eu la note"
          f" {get_grade(10, 10)}")


affichage_note()
