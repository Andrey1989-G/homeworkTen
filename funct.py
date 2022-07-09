import json

from flask import Flask

#определям переменную для файла
file = 'candidates.json'


def load_candidates():
    """
    load data from file
    :param file: filename in type = str
    :return:list with data
    """
    global file
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_print(dct):
    """

    :param lst:
    :return:
    """
    res = f'Имя кандидата - {dct["name"]}\n' \
          f'Позиция кандидата - {dct["pk"]}\n' \
          f'Навыки - {dct["skills"]}\n\n'
    return res


def get_all():
    """
    print all candidates
    :param dict: dict with data about candidates
    :return: print views all candidates
    """
    res = '<pre>\n'
    for i in load_candidates():
        res += format_print(i)
    return res + '</pre>'


def get_by_pk(pk):
    """
    return name candidates by pk
    :param pk: int
    :return: name candidates(type str)
    """
    for i in load_candidates():
        if i['pk'] == pk:
            return f'{i["picture"]}\n<pre> {format_print(i)} </pre>'


def get_by_skill(skill_name):
    """
    return name candidates with the right skills
    :param skill_name: name skill type str
    :return: str with cadidates's data
    """
    res = ''
    for i in load_candidates():
        if skill_name[1:] in i['skills']:
             res += format_print(i)
    return f'<pre>{res}</pre>'

