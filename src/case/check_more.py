# -*- coding:UTF-8 -*-
from src.common.basic_info import d
from src.common.get_elements import GetElements
from src.common.event_keyboard import EventKey

class CheckMore:
    def __init__(self):
        pass

    def click_more_item_1(self):
        d(description=GetElements().get_element_by_description("more_item","more_item_3_1_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_2(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_3_1_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_3(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_3_2_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_4(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_3_2_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_5(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_3_3_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_6(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_3_3_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_more_item_more(self):
        d(description=GetElements().get_element_by_description("more_item", "more_item_more")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False