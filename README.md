# WEBSCRAPPING #

# Introduction #

* For data scientists data is main key source before proceeding into the next step .Data can collected from different ways ,some of the ways are : <br>
                                            1. From Data Bases <br>
                                            2. From different online open source data sets <br>
                                            3. Through Web scrapping  <br>
                                            4. Some other Sources <br>
                                            
> ## RESOURCES ##
   * For web scrapping normally we are going proceed in different ways using different resources ,but now i'm using Selenium:
       ### Selenium : 
     Selenium is an automation testing framework for web applications/websites which can also control the browser to navigate the website just like a human. Selenium uses a web-driver package that can take control of the browser and mimic user-oriented actions to trigger desired events. 
# Setup  :
  **Selenium**: <br> To download selenium package, execute the below pip command in terminal:<br>
     `pip install selenium ` <br>
     **Selenium Drivers**: <br> Web drivers enable python to control the browser via OS-level interactions. Web drivers use the browser's built-in support for the automation process so, in order to control the browser, the web-driver must be installed and should be accessible via the PATH variable of the operating system (only required in case of manual installation). <br>
     **Driver Installation**: <br >
     Download the drivers from [official site](https://pypi.org/project/selenium/) for Chrome, Firefox, and Edge. Opera drivers can also be downloaded from the [Opera Chromium](https://github.com/operasoftware/operachromiumdriver/releases) project hosted on Github.
     
     
>> Safari 10 on OS X El Capitan and macOS Sierra have built-in support for the automation driver. This guide contains snippets to interact with popular web-drivers, though Safari is being used as a default browser throughout this guide.<br> Other browsers like UC, Netscape etc., cannot be used for automation. The Selenium-RC (remote-control) tool can control browsers via injecting its own JavaScript code and can be used for UI testing.
# Data Extraction  :
Let's get started by searching a sarees ,price , ratings  and downloading the CSV file(s) with the following steps:
 1. **Import Dependencies and Create Driver Instance**: The initial step is to create an object of webdriver for particular browser by importing it from selenium [click](https://github.com/Surekha-honey/WEB_SCRAPPING/blob/master/WEB-SCRAPPING%20ON%20AMAZON%20WEBSITE.py)
 # Locating WebElement :
 Selenium offers a wide variety of functions to locate an element on the web-page as:<br>
* **find_element_by_id**: Use id to find an element.
* **find_element_by_name**: Use name to find an element.
* **find_element_by_xpath**: Use xpath to find an elements.
* **find_element_by_link_text**: Use text value of a link to find element.
* **find_element_by_partial_link_text**: Find element by matching some part of a hyper link text(anchor tag).
* **find_element_by_tag_name**: Use tag name to find an element.
* **find_element_by_class_name**: Use value of class attribute to find an element.
* **find_element_by_css_selector**: Use CSS selector for id, class to find element. Or use find_element with BY locater as:
`images=driver.find_element_by_xpath("")`
>Use overloaded versions of functions to find all occurrences of a searched value. Just use elements instead of element as:<br>
`images=driver.find_elements_by_xpath("")`
 
