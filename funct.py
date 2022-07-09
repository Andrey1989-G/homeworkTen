import json

file = 'candidates.json'


def load_candidates(file):
    """
    load data from file
    :param file: filename in type = str
    :return:list with data
    """
    with open(file) as f:
        return json.load(f)


def get_all(func):
    """
    print all candidates
    :param dict: dict with data about candidates
    :return: print views all candidates
    """
    print(*[x['name'] + '\n' for x in func])


def get_by_pk(pk):
    """
    return name candidates by pk
    :param pk: int
    :return: name candidates(type name)
    """
    for i in load_candidates(file):
        if i['pk'] == pk:
            return i['name']


def get_by_skill(skill_name):
    """
    return name candidates with the right skills
    :param skill_name: name skill
    :return: list with name candidates
    """
    res = []
    for i in load_candidates(file):
        if skill_name in i['skills']:
             res.append(i['name'])
    return res

