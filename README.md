
0. file--->new project--->& just give desire project name
1. Open cmd as Admin cd project path & pip3 install seleniumbase
2. Type sbase to see version & verification
3. Download all drivers
   a. sbase install chromedriver latest
   b. seleniumbase install geckodriver latest
   c. seleniumbase install edgedriver latest
   d. seleniumbase install operadriver latest
   e. seleniumbase install iedriver
   it Auto install in this path :- C:\python38\Lib\site-packages\seleniumbase\drivers/chromedriver.exe
   
4. By default, CSS Selectors are used for finding page elements.
5. sbase mkdir ui_tests :- it will give project structure and sample test cases

6. cd ui_t + Tab will auto complete [cd ui_tests]
7. pytest TestCases\my_first_test.py {do write little + TAB AUTOCOMPLETE}
 yes Excillent it's done & all work perfectly

8. pytest my_first_test.py --browser=chrome
   pytest TestCases\Test_01_Login.py
   nosetests test_suite.py --browser=firefox & 
   chrome is the default browser if not specified.
   
9. To Run methods :- pytest LoginTest.py::LoginTest::test_login

10.For headless just add this at end --headless

11.FAILED:- It auto do 3 things , screenshot, logs, & pageSource.html & keep inside latest_logs

12. No More Flaky Tests:
   SeleniumBase methods automatically wait for page elements to finish loading before interacting with them (up to a timeout limit:- 6sec).
   This means you no longer need random time.sleep() statements in your scripts.

13. For Reports:- pytest Test_01_Login.py --dashboard -rs --headless  will give report inside test case

14.remote :- origin
