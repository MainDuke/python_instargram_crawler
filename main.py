import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main_fun():
    baseUrl = 'https://instagram.com/'
    targetUrl = 'geonwoolee_art'
    chromeDriver = 'C:/test_insta/chromedriver_win32/chromedriver.exe'

    user_id = ''
    user_pwd = ''

    # To-Do : 크롬드라이버를 자동화 할순 없을까?
    # To-Do : try-catch 를 통해서 버그 잡아서, 리턴 줘야함.
    driver = webdriver.Chrome(chromeDriver)

    # To-Do : try-catch , 접속 실패시 캐치.
    driver.get(targetUrl)
    driver.implicitly_wait(5)  # seconds

    # To-Do : try-catch , 속성값 못 찾았을 때 캐치해야함.
    user_form = driver.find_element_by_name('username')
    user_form.send_keys(user_id)
    pass_form = driver.find_element_by_name('password')
    pass_form.send_keys(user_pwd)
    pass_form.send_keys(Keys.RETURN)
    sleep(2)  # 살짝, 기다려야 로그인을 인식함. 로그인 인식후, 페이지 이동해야, 다시 로그인 여부를 묻지 않는다.

    # To-Do : try-catch , 속성값 못 찾았을 때 캐치해야함.
    # To-Do : 기본 URL 과, 타켓 URL 을 분리해야함.
    driver.get(baseUrl + targetUrl)
    driver.implicitly_wait(5)  # seconds

    # To-Do : 현재는 클래스명이 저거지만, 나중에 바뀔수 있을때 어떻게 대처할래?
    get_post_count = driver.find_elements_by_css_selector('.g47SY')
    all_post_count = int(get_post_count[0].text)
    print("All Post COUNT =", get_post_count[0].text)

    result = set()
    try_count = 0
    # 비교 판단 후 스크롤링
    while all_post_count - len(result) > 0:
        # 안전장치, 스크롤 이후 파싱된 값이 10번이상 같은 경우 무한 루프에 빠지기 전에 빠져나간다.
        temp_count = all_post_count - len(result)
        if try_count == 10:
            break

        print("now Status =", all_post_count - len(result))
        get_temp = driver.find_element_by_xpath('//article')
        temp = get_temp.find_elements_by_tag_name('img')
        for i in temp:
            result.add(i.get_attribute('src'))

        driver.execute_script("window.scrollBy(0, 400)")
        randmized_sleep(1)

        if len(result) - temp_count == 0:
            try_count += 1
        else:
            try_count = 0

    print("result : Len = ", len(result))
    for i in result:
        print(i)


def scroll_down(driver, wait=0.3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    randmized_sleep(wait)


def scroll_up(driver, offset=-1, wait=2):
    if offset == -1:
        driver.execute_script("window.scrollTo(0, 0)")
    else:
        driver.execute_script("window.scrollBy(0, -%s)" % offset)
        randmized_sleep(wait)


def randmized_sleep(average=1):
    _min, _max = average * 1 / 2, average * 3 / 2
    sleep(random.uniform(_min, _max))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_fun()
