from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    # Initialize the WebDriver
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
        
    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')
        
    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)
        
    url = f"https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword={keyword}&sc.keyword={keyword}&locT=&locId=&jobType="
    driver.get(url)

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    jobs = []

    # Function to close modal if it appears
    def close_modal():
        try:
            close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.CloseButton')))
            close_button.click()
        except (NoSuchElementException, TimeoutException):
            pass

    def load_new_job_list():
        # After processing all jobs on the current page, click the "Show more jobs" button if it exists
        try:
            show_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="load-more"]')))
            show_more_button.click()
            # Wait for new job listings to load
            wait.until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "JobsList_jobListItem")]')))
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Encountered an exception: {e}")

    # Get the list of all job listings
    job_listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "JobsList_jobListItem")]')))
    job_listings = [job for job in job_listings if job.text.strip()]

    job_index = 0

    while len(jobs) < num_jobs:
        if job_index >= len(job_listings):
            load_new_job_list()
            job_listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "JobsList_jobListItem")]')))
            job_listings = [job for job in job_listings if job.text.strip()]
            #job_index = 0

        if job_index < len(job_listings):
            job_listings[job_index].click()
        
        print("Progress: {} out of {}".format(len(jobs), num_jobs))
        if len(jobs) >= num_jobs:
            break
        
        # Close the modal if it appears
        close_modal()
        
        collected_successfully = False
        while not collected_successfully:
            try:
                company_name = driver.find_element(By.XPATH, './/h4[@class="heading_Heading__BqX5J heading_Subhead__Ip1aW"]').text
                location = driver.find_element(By.XPATH, './/div[@class="JobDetails_location__mSg5h"]').text
                job_title = driver.find_element(By.XPATH, './/h1[@class="heading_Heading__BqX5J heading_Level1__soLZs"]').text
                 #job_description = driver.find_element(By.XPATH, './/div[contains(@class, "JobDetails_jobDescription__uW_fK") and contains(@class, "JobDetails_showHidden__C_FOA")]').text
                #job_description = driver.find_element(By.XPATH, './/div[contains(@class, "JobDetails_jobDescriptionWrapper___tqxc JobDetails_jobDetailsSectionContainer__o_x6Z JobDetails_paddingTopReset__IIrci")]').text
                collected_successfully = True
            except Exception as e:
                print(f"Error collecting data: {e}")
                time.sleep(5)

        try:
            salary_estimate = driver.find_element(By.XPATH, './/div[@class="SalaryEstimate_salaryRange__brHFy"]').text
        except NoSuchElementException:
            salary_estimate = -1 
        
        try:
            rating = driver.find_element(By.XPATH, './/div[@class="EmployerProfile_ratingContainer__ul0Ef"]').text
        except NoSuchElementException:
            rating = -1

        jobs.append({
            "Job Title": job_title,
            "Salary Estimate": salary_estimate,
            #"Job Description": job_description,
            "Rating": rating,
            "Company Name": company_name,
            "Location": location,
        })

        # Going to the Company tab...
        try:
            element = driver.find_element(By.XPATH, '//section[contains(@class, "JobDetails_jobDetailsSectionContainer")]//h2/span[text()="Company overview"]')
            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()

            try:
                headquarters = driver.find_element(By.XPATH, './/div[@class="infoEntity"]//label[text()="Headquarters"]/following-sibling::span').text
            except NoSuchElementException:
                headquarters = -1

            try:
                size = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Size"]/following-sibling::div').text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Founded"]/following-sibling::div').text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Type"]/following-sibling::div').text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Industry"]/following-sibling::div').text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Sector"]/following-sibling::div').text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]//span[text()="Revenue"]/following-sibling::div').text
            except NoSuchElementException:
                revenue = -1

            try:
                competitors = driver.find_element(By.XPATH, './/div[@class="infoEntity"]//label[text()="Competitors"]/following-sibling::span').text
            except NoSuchElementException:
                competitors = -1

        except NoSuchElementException:  # Rarely, some job postings do not have the "Company" tab.
            headquarters = -1
            size = -1
            founded = -1
            type_of_ownership = -1
            industry = -1
            sector = -1
            revenue = -1
            competitors = -1

        jobs[-1].update({
            "Headquarters": headquarters,
            "Size": size,
            "Founded": founded,
            "Type of ownership": type_of_ownership,
            "Industry": industry,
            "Sector": sector,
            "Revenue": revenue,
            "Competitors": competitors
        })

        job_index += 1
    
    return pd.DataFrame(jobs)  # This line converts the dictionary object into a pandas DataFrame.
