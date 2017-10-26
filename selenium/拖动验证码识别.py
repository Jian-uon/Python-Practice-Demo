# -*- coding:utf-8 -*-
import unittest
import time
import random
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class IdentityCodeBreak(unittest.TestCase):
    target = 'http://www.gsxt.gov.cn/index.html'

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS(executable_path='D:\Data\code\python\phantomjs-1.9.7-windows\phantomjs.exe')

    def getCompanyName(self, companyName= ''):
        companyName = u'长虹'
        return companyName

    def cropArea(self, filename):
        img = Image.open(filename)
        #img.show()
        region = (490, 362, 750, 482) # 260 * 120
        cropImage = img.crop(region)
        cropImage.save('crop'+filename)

        reg2 = (555, 362, 750, 482) # 260 * 120
        cI = img.crop(reg2)
        cI.save('temp.jpg')
        return cropImage

    def is_similar(self, img1, img2, x, y):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        for i in range(0, 3):
            if abs(pixel1[i] - pixel2[i]) > 50:
                return False
        return True

    def get_different_location(self, img1, img2):
        for i in range(65, 260):
            for j in range(0, 120):
                if self.is_similar(img1, img2, i, j) == False:
                    print 'delta = %d' % i
                    return i


    def get_track(self, len):
        steps = []
        next = random.randint(1, 7)
        while next + 7 <= len:
            steps.append(next)
            len -= next
            next = random.randint(1, 7)
        steps.append(next)
        len -= next

        print 'len = %d'% len
        for i in range(len):
            steps.append(1)
        return steps

    def test(self):
        driver = self.driver
        driver.get(self.target)

        page = driver.page_source
        print(page)

        time.sleep(5)
        #self.assertIn(u"国家企业信用信息", driver.title)

        searchContent = driver.find_element_by_id("keyword")
        searchContent.send_keys(self.getCompanyName())
        searchContent.send_keys(Keys.RETURN)

        time.sleep(0.7)
        driver.get_screenshot_as_file('Origin.jpg')
        button = driver.find_element_by_class_name("gt_slider_knob")
        ActionChains(driver).click_and_hold(button).perform()
        time.sleep(0.7)
        driver.get_screenshot_as_file('Current.jpg') #260 * 116

        cropOri = self.cropArea('Origin.jpg')
        cropCur = self.cropArea('Current.jpg')
        delta = self.get_different_location(cropOri, cropCur)

        total = delta
        step_list = self.get_track(total)

        sum = 0
        print '需要移动的总长度 %d' % total
        ct = 0
        for step in step_list:
            print '(%d, %d, %d)' %(ct, step, sum)
            ct += 1
            if sum >= total:
                break
            #action = ActionChains(driver)
            #action.move_by_offset(step, 0).perform()
            #action._actions = []
            #ActionChains(driver).move_by_offset(step, 0).perform()
            #button = driver.find_element_by_class_name("gt_slider_knob")
            ActionChains(driver).move_to_element_with_offset(button, step+22, 22).perform()
            sum += step
            time.sleep(random.randint(10, 20) / 1000.0)


        #ActionChains(driver).move_to_element_with_offset(to_element=button, xoffset=19, yoffset=22).perform()
        #time.sleep(0.1)
        for i in range(7):
            time.sleep(0.08)
            #time.sleep(random.randint(10, 50) / 100)
            ActionChains(driver).move_to_element_with_offset(to_element=button, xoffset=21, yoffset= 22).perform()
        ActionChains(driver).release(button).perform()
        time.sleep(5)

        page = driver.page_source
        print(page)

    def tearDown(self):

        self.driver.close()


if __name__ == '__main__':
    unittest.main()

