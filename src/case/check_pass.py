# -*- coding:UTF-8 -*-
from src.common.get_elements import GetElements
from src.common.basic_info import d

class CheckPass:
    def __init__(self):
        pass

    def click_pass_item_1(self):
        d(description=GetElements().get_element_by_description("pass_item", "pass_item_2_1_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pass_item_2(self):
        d(description=GetElements().get_element_by_description("pass_item", "pass_item_2_1_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pass_item_3(self):
        d(description=GetElements().get_element_by_description("pass_item", "pass_item_2_2_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pass_item_4(self):
        d(description=GetElements().get_element_by_description("pass_item", "pass_item_2_2_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pass_item_more(self):
        d(description=GetElements().get_element_by_description("pass_item", "pass_item_more")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

if __name__ == '__main__':
    print CheckPass().click_pass_item_1()