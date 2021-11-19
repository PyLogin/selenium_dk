# -*- coding:UTF-8 -*-
import time
from src.common.basic_info import d
from src.common.get_elements import GetElements
from src.common.img_cmp import ImgCmp,IMG_PATH
class CheckAccount:
    def __int__(self):
        pass
    def click_account_item_3(self):
        d(description=GetElements().get_element_by_description("account_item", "account_item_3")).click_exists()
        time.sleep(1)
        img = IMG_PATH + "tiro.png"
        return ImgCmp().img_cmp(img, GetElements().get_element_by_description("account_item", "account_item_3"))

    def click_account_item_4(self):
        d(description=GetElements().get_element_by_description("account_item", "account_item_4")).click_exists()
        time.sleep(1)
        img = IMG_PATH + "loan.png"
        return ImgCmp().img_cmp(img, GetElements().get_element_by_description("account_item", "account_item_4"))

    def click_account_item_5(self):
        d(description=GetElements().get_element_by_description("account_item", "account_item_5")).click_exists()
        time.sleep(1)
        img = IMG_PATH + "service.png"
        return ImgCmp().img_cmp(img, GetElements().get_element_by_description("account_item", "account_item_5"))

if __name__ == '__main__':
    print CheckAccount().click_account_item_5()