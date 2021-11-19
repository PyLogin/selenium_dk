# -*- coding:UTF-8 -*-
from src.common.basic_info import d
from src.common.get_elements import GetElements

class CheckProductItem:
    def __init__(self):
        pass

    def click_pdt_item_1(self):
        d(description=GetElements().get_element_by_description("pdt_item","pdt_item_1")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pdt_item_2(self):
        d(description=GetElements().get_element_by_description("pdt_item", "pdt_item_2")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pdt_item_3(self):
        d(description=GetElements().get_element_by_description("pdt_item", "pdt_item_3")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

    def click_pdt_item_4(self):
        d(description=GetElements().get_element_by_description("pdt_item", "pdt_item_4")).click_exists()
        if d(className=GetElements.get_element_by_classname("topic_detail", "topic_detail_1")).exists:
            return True
        else:
            return False

if __name__ == '__main__':
    print CheckProductItem().click_pdt_item_1()