# -*- coding: utf-8 -*-#
# !/usr/local/bin/python2.7
from collections import OrderedDict


def text_cleaning(text):
    text = text.replace("===", "~")
    text_list = text.split('==')
    stripped_list = map(str.strip, text_list)
    stripped_list[:0] = ['Summary']
    text_dict = list_to_dict(stripped_list)
    # Create sub dictionary if there are sub-sections present in the dictionary
    text_dict = sub_dictionary(text_dict,'~')
    text_dict = remove_reference_sections(text_dict)
    return text_dict


def remove_reference_sections(dictionary):
    check = ('Reference', 'reference', 'Link', 'link')
    for key, entry in dictionary.iteritems():
        if any(word in key for word in check):
            dictionary = del_dict_item(dictionary, key)
    return dictionary


def sub_dictionary(dictionary, searchFor):
    """Finds if split value exists in dictionary values
    and creates a sub-dictionary."""
    for key, dict_item in dictionary.iteritems():
        if searchFor in dict_item:
            dict_item = dict_item.split(searchFor)
            new_list = [key]+dict_item
            new_list = map(str.strip, new_list)
            sub_dict = list_to_dict(new_list)
            dictionary[key] = sub_dict
    return dictionary


def list_to_dict(text_list):
    i = iter(text_list)
    text_dict = OrderedDict(zip(i, i))
    # What if there are two blank entries?
    for key, entry in text_dict.iteritems():
        if len(entry) == 0:
            text_dict = del_dict_item(text_dict, key)
    return text_dict


def del_dict_item(text_dict, key):
    r = OrderedDict(text_dict)
    del r[key]
    return r


def clean_sorted(tupes):
    l = []
    for val in tupes:
        l.append(val[0].replace('_', ' ').replace('(', '').replace(')', ''))
    return l


def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"
