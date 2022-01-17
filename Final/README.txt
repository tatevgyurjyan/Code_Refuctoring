Application URL to work with:   https://courses.ultimateqa.com/

DESIGNED TEST SCENARIOS -->

test_search_existing_course:            Login to page
                                        Search for an existing course
                                        Check that the titles of the found courses contain the searched data


test_search_non_existing_course:        Login to page
                                        Search for a non-existing course
                                        Check that "No Result Found" message is visible                                


TODO:                           pip install pytest

Impotred Libraries:             webdriver_manager.chrome, selenium, selenium.webdriver.support,
                                selenium.webdriver.common.keys, selenium.webdriver.support.wait, 
                                selenium.webdriver.common.by, pytest, logging, string, random,
                                json, time  

Design Pattern:                 Page Object Model (modular structure running by pytest) 

Selector:                       XPATH

Project Modules:        Helper --> helpers.py  (includes all common methods which are used in 'Pages')
                                        Designed Methods: -->  
                                                'go_to_page'
                                                'find_and_click'
                                                'find_and_send_keys'
                                                'find' 
                                                'find_all'  
                                                'email_generator'
                                                'password_generator'                                
                        Pages --> 

                                sign_up.py
                                        Designed Methods: --> 
                                                'registration'     
                                                                                                                           
                                sign_in.py 
                                        Designed Methods: -->
                                                'login_user'   

                                search.py
                                        Designed Methods: -->
                                                                       
                        Testdata --> 
                                config.json (includes configuration data)

                        conftest.py (includes methods 'logger' and 'driver')
                        
Test Cases:                               
                        Tests: --> 
                               
                                'test_search_existing_course.py'
                                'test_search_non_existing_course.py'
                                                          
Log                     test_log.txt
