import sys

sys.path.append("C:\projectpython\PyDrozhilkin211-351\exercises")

from pyneng_common_functions import check_pytest, unified_columns_output


check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_6


    task_4_6.ospf_route = task_4_6.ospf_route.replace(",", "").replace("[", "").replace("]", "")
    task_4_6.ospf_route = task_4_6.ospf_route.split()
    task_4_6.template = task_4_6.template.format(task_4_6.ospf_route[0], task_4_6.ospf_route[1], task_4_6.ospf_route[3], task_4_6.ospf_route[4], task_4_6.ospf_route[5])
    print(task_4_6.template, file=sys.stdout)
    

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
