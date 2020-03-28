'''
@Author: LEGEND
@Date: 2020-02-23 16:00:23
@LastEditTime: 2020-03-29 04:44:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \gauge-tests\step_impl\step_impl.py
'''
#!/usr/bin/env python
# -*-coding:utf8-*-

from getgauge.python import step, Messages, before_step, after_step, before_scenario, after_scenario, before_spec, after_spec, before_suite, after_suite
import pytest

vowels = ["a", "e", "i", "o", "u"]


def number_of_vowels(word):
    return len([elem for elem in list(word) if elem in vowels])


# --------------------------
# Gauge step implementations
# --------------------------

@step("The word <word> has <number> vowels.")
def assert_no_of_vowels_in(word, number):
    assert str(number) == str(number_of_vowels(word))


@step("Vowels in English language are <vowels>.")
def assert_default_vowels(given_vowels):
    Messages.write_message("Given vowels are {0}".format(given_vowels))
    assert given_vowels == "".join(vowels)


@step("Almost all words have vowels <table>")
def assert_words_vowel_count(table):
    actual = [str(number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
    expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
    assert expected == actual


"""
实现.spe的step with table
"""
@step("Create following <race> characters <table>")
def create_characters(race, table):
    actual = table.get_column_values_with_name("name")
    print(actual)
    assert race == "hobbit" and actual == ["frodo", "bilbo", "samwise"]


"""
实现.spe的step alias
"""
@step(["Create a user <user name>", "Create another user <user name>"])
def create_user(user_name):  # 同一场景
    print("create {}.".format(user_name))


@step(["A <email_type> email is sent to the user", "An email confirming the <email_type> is sent"])
def email(email_type):  # 不同场景
    print("create {}.".format(email_type))


'''
实现.spe重构
'''
@step("The word <word> has <number> vowels")
def the_word_has_vowels(word, number):
    print('word {}.'.format(word), 'number {}'.format(number))









"""
实现.sep的teardown实例
"""
@step("Logout user <name>")
def logout_user(name):
    assert name == 'mike'


@step("Delete user <name>")
def delete_user(name):
    assert name == 'mike'


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():  # hook函数
    assert "".join(vowels) == "aeiou"


@before_step("<tags>")  # 只执行"Tags"标签的step
def before_step_hook(context):  # hook函数
    print("我是step的师傅！\n", context)  # (当前hook执行信息)为了获得有关当前规范，场景和步骤执行的其他信息，可以将一个名为ExecutionContext的附加参数添加到hooks方法中。

@after_step()
def after_step_hook(context):  # hook函数
    print("我是step的徒弟!\n", context)
    print("断点结束！")
    