from selenium import webdriver
import time
from selenium.webdriver import ActionChains
bro=webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('https://uland.taobao.com/sem/tbsearch')
#如果定位的标签是存在于iframe标签之中则必须通过如下操作进行标签定位
bro.switch_to.frame('')#切换浏览器标签定位的作用域
div=bro.find_element_by_id('')
#动作链
action=ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)
for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(15,0).perform()
    time.sleep(0.3)
#释放动作链
action.release()
bro.quit()
'''定位iframe

1.有id，并且唯一，直接写id
driver.switch_to_frame("x-URS-iframe")
driver.switch_to.frame("x-URS-iframe")

2.csv.有name，并且唯一，直接写name
driver.switch_to_frame("xxxx")
driver.switch_to.frame("xxxx")

3.无id，无name,先定位iframe元素
iframe = driver.find_elements_by_tag_name("iframe")[0]
driver.switch_to_frame(iframe)
driver.switch_to.frame(iframe)

4.通常采用id和name就能够解决绝大多数问题。但有时候frame并无这两项属性，则可以用index和WebElement来定位：

index从0开始，传入整型参数即判定为用index定位，传入str参数则判定为用id/name定位
WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
举个栗子：

<iframe src="myframetest.html" />
1
用xpath定位，传入WebElement对象：

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'myframe')]"))


5.从frame中切回主文档(switch_to.default_content())
切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。

driver.switch_to.default_content()
1
6.嵌套frame的操作(switch_to.parent_frame())
有时候我们会遇到嵌套的frame，如下：

<html>
    <iframe id="frame1">
        <iframe id="frame2" / >
    </iframe>
</html>
1
2.csv
3
4
5
1.从主文档切到frame2，一层层切进去

driver.switch_to.frame("frame1")
driver.switch_to.frame("frame2")
1
2.csv
2.csv.从frame2再切回frame1，这里selenium给我们提供了一个方法能够从子frame切回到父frame，而不用我们切回主文档再切进来。

driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果
1
有了parent_frame()这个相当于后退的方法，我们可以随意切换不同的frame，随意的跳来跳去了。

所以只要善用以下三个方法，遇到frame分分钟搞定：

driver.switch_to.frame(reference)
driver.switch_to.parent_frame()
driver.switch_to.default_content()'''