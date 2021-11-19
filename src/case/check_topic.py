# -*- coding: UTF-8 -*-

from src.common.basic_info import d
from src.common.get_elements import GetElements

class CheckTopic:
    def __init__(self):
        pass

    def click_topic_tab_1(self):
        d(description=GetElements().get_element_by_description("topic_ico","topic_ico_1")).click_exists()
        if d(className=GetElements().get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False

    def click_topic_tab_2(self):
        d(description=GetElements().get_element_by_description("topic_ico", "topic_ico_2")).click_exists()
        if d(className=GetElements().get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_topic_tab_3(self):
        d(description=GetElements().get_element_by_description("topic_ico", "topic_ico_3")).click_exists()
        if d(className=GetElements().get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

if __name__ == '__main__':
    print CheckTopic().click_topic_tab_2()

