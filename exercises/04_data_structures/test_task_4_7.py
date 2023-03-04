import sys

sys.path.append("C:\projectpython\PyDrozhilkin211-351\exercises")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_7

    task_4_7.mac = task_4_7.mac.replace(":", "")
    task_4_7.mac = bin(int(task_4_7.mac, 16))[2:]
    print(task_4_7.mac, file=sys.stdout)

    out, err = capsys.readouterr()
    correct_stdout = "101010101010101010111011101110111100110011001100"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
