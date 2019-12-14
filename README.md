# EC601-Project-Automated-Admission-System

### Team Members:
<ul>
  <li>Yu Liu U34066489</li>
  <li>Shengyao Shao U85552843</li>
  <li>Jing Song U65712216</li>
 </ul>

### <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/static/images/logo.png"></br>

### Product Definition: 
Our project is designed to help those graduate school admission officers to accelerate their admission process. Our web application will provide users with standardized summaries of applicant’s transcript, sentiment analysis of the applicant’s reference letter, and the predicted chance of admission.
</br>

### Target Users: 
<em><strong>Graduate school admission officers</strong></em> who used to spend a lot of time reading through each applicant's transcript.</br>

### MVP:
The product should provide users with a report that summarizes the useful information presented in each applicant's transcript.</br>

### User Stories:

<ul>
  
<li> I, as a grauduate school admission officer, should be able to see a report of sentimental analysis on the reference letters</li>
  
<li> I, as a graduate school admission officer, should be able to see the applicants’ chance of admission based on their application materials.</li>

<li> I, as a graduate school admission officer, should be able to log into the system.</li>

<li> I, as a grauduate school admission officer, should be able to see the applicant's undergrad university, its world ranking  and whether the applicant should take TOEFL test or not.</li>

<li> I, as a grauduate school admission officer, should be able to see the applicant's GPA (under 4.0 scale).</li>

<li> I, as a grauduate school admission officer, should be able to get a list of categories of the courses the student has taken.</li>

<li>I, as a grauduate school admission officer, should be able to see the student's ranking among all applicants from the same university.</li>

<li> I, as a grauduate school admission officer, should be able to get a list of honors and/or academic achievements the applicant gained during undergrad.</li>
  
<li> I, as a grauduate school admission officer, should be able to get a list of activities and/or internships the applicant has participated in.</li>
  
</ul>

## [Sprint 1](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Sprint%201%20Presentation.pdf) 
- ### [Industry (product and patent) review and analysis:](https://github.com/daisysj/EC601-Project-AAS/blob/master/Sprint%201_Industry%20Review.pdf)
  - Competitors
        - [Ellucian](https://www.ellucian.com/solutions/ellucian-crm-recruit)
        - [Salesforce](https://www.salesforce.org/highered/recruiting/)
        - [Kira Talent](https://www.kiratalent.com/product/)
 
  - Industry Debates
        - Bias
        - Dislike for AI algorithms
   
  - Our Advantages
        - Particularity
        - Fairness
 
  - Our Limitations
        - Limited Data Access
        - Limited Factors

- ### Technology selections and reasons:
  - JavaScript
        - It's supported by all major browsers
        - Similar syntax to C
        - Doesn't need complier 

  - Python
        - We are familiar with Python
        - Third-party modules to interact across platforms and languages
        - Large libraries make coding easier
 
  - PDF Converter API
 
  - Google Natural Language API
 
  - Mysql
        - Great for storing word documents 
        - Encrypted conncection
   
- ### Initial decisions on implementation path:
<img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/Architecture.png">

- ### Tasks for Sprint 2:
    - Crawl data from different university websites for course numbers and names
    - Processing transcripts texts, generate a dictionary for courses and grades; extract students' main info, GPA, etc.; show the         summary of results on a pdf for each individual student
    - Utilize database (mySQL) for pdfs, texts storage; mangoDB (?) for json results storage
    - Build an AI probability predictor for admission results based on UCLA admission data (weight on different parameters).
    - Recommendation letter sentiment analysis
    - Application name / logo design

- ### Tasks for Sprint 3:
    - Web application / PC Applicaiton: http://cs-people.bu.edu/liuyu529/EC601/UI.html

## [Sprint 2](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Sprint%202%20Presentation.pdf) 
- ### Project Components
    - Transcript Processing
    - Recommendation Letter Sentiment Analysis
    - Probability of admission
    - Generate a summary of all above parameters for each student 
- ### System Architecture

- ### Machine Learning Algorithm 

## Content:

#### 1. [Meeting with Professor Trachtenberg](https://github.com/daisysj/EC601-Project-AAS/blob/master/2019.9.24%20Meeting%20with%20Prof.%20Trachtenberg.pdf)

#### 2. User Stories & MVP

#### 3. [Industry Review](https://github.com/daisysj/EC601-Project-AAS/blob/master/Sprint%201_Industry%20Review.pdf)

