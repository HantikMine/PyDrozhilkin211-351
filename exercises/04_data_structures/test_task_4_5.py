import sys

sys.path.append("C:\projectpython\PyDrozhilkin211-351\exercises")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_5

    words1 = task_4_5.command1.split()[-1].split(",")
    words2 = task_4_5.command2.split()[-1].split(",")
    result_set = set(words1).intersection(set(words2))
    task_4_5.result = sorted(list(result_set))
    print(task_4_5.result, file=sys.stdout)

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '8']"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_4_5

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_4_5) if not var.startswith("_")]

    correct_result = ["1", "3", "8"]
    assert (
        "result" in task_vars
    ), "Итоговый список должен быть записан в переменную result"
    assert (
        type(task_4_5.result) == list
    ), f"По заданию в переменной result должен быть список, а в ней {type(task_4_5.result).__name__}"
    assert (
        correct_result == task_4_5.result
    ), f"В переменной result должен быть список {correct_result}"
