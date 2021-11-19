# -*- coding:UTF-8 -*-
from src.common.basic_info import d
from src.common.get_elements import GetElements
from src.common.event_keyboard import EventKey

class CheckRecom:
    def __init__(self):
        pass

    def click_recom_item_1(self):
        d(description=GetElements().get_element_by_description("recom_item","recom_item_1_1_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False

    def click_recom_item_2(self):
        d(description=GetElements().get_element_by_description("recom_item","recom_item_1_1_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False

    def click_recom_item_3(self):
        d(description=GetElements().get_element_by_description("recom_item","recom_item_1_2_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False
    def click_recom_item_4(self):
        d(description=GetElements().get_element_by_description("recom_item","recom_item_1_2_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail","topic_detail_1")).exists:
            return True
        else:
            return False

    def click_recom_item_5(self):
        d(description=GetElements().get_element_by_description("recom_item", "recom_item_1_3_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_recom_item_5(self):
        d(description=GetElements().get_element_by_description("recom_item", "recom_item_1_3_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_recom_item_6(self):
        d(description=GetElements().get_element_by_description("recom_item", "recom_item_1_3_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

if __name__ == '__main__':
    CheckRecom().click_recom_item_6()