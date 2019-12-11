# EC601-Project-Automated-Admission-System

### Team Members:
<ul>
  <li>Jing Song U65712216</li>
  <li>Shengyao Shao U85552843</li>
  <li>Yu Liu U34066489</li>
 </ul>

### Product Definition: 
Our project is designed to help students determine the chances of them getting accepted by Boston University graduate school. Our application will provide users with standardized summaries of transcripts, so that students' grades, courses taken, GPA are in the same scale. Also, the application will also give a report of sentimental analysis on the statement of purposes.

### Target Users: 
<em><strong>Graduate school applicants</strong></em> who wants to know his chances of getting accepted.</br>

### MVP:
The product should provide users with a report that summarizes the useful information presented in applicant's transcript.</br>

### User Stories:

<ul>
<li> I, as a grauduate school applicant, should be able to see my undergrad school's world ranking  and whether the I should take TOEFL test or not.</li>

<li> I, as a grauduate applicant, should be able to see my standardized GPA (under 4.0 scale).</li>

<li> <strong>I, as a grauduate school applicant, should be able to get a list of categories of the relevant courses taken. </strong></li>

<li> I, as a grauduate school applicant, should be able to see a report of sentimental analysis on the statement of purpose</li>

<li> I, as a grauduate school applicant, should be able to enter a list of honors and/or academic achievements the applicant gained during undergrad.</li>
  
<li> I, as a grauduate school applicant, should be able to enter a list of activities and/or internships the applicant has participated in.</li>
  
</ul>

### [Industry (product and patent) review and analysis:](https://github.com/daisysj/EC601-Project-Automated-Admission-System/blob/master/Sprint%201_Industry%20Review.pdf)
 - Competitors
   1. [Ellucian](https://www.ellucian.com/solutions/ellucian-crm-recruit)
   2. [Salesforce](https://www.salesforce.org/highered/recruiting/)
   3. [Kira Talent](https://www.kiratalent.com/product/)
 
 - Industry Debates
   1. Bias
   2. Dislike for AI algorithms
   
 - Our Advantages
   1. Particularity
   2. Fairness
 
 - Our Limitations
   1. Limited Data Access
   2. Limited Factors

### Technology selections and reasons:
 - JavaScript
   1. It's supported by all major browsers
   2. Similar syntax to C
   3. Doesn't need complier 

 - Python
   1. We are familiar with Python
   2. Third-party modules to interact across platforms and languages
   3. Large libraries make coding easier
 
 - PDF Converter API
 
 - Google Natural Language API
 
 - Mysql
   1. Great for storing word documents 
   2. Encrypted conncection
### Initial decisions on implementation path:
### <img src = "https://github.com/daisysj/EC601-Project-Automated-Admission-System/blob/master/Architecture.png"></br>

### Tasks for Sprint 2:
1. Crawl data from different university websites for course numbers and names
2. Processing transcripts texts, generate a dictionary for courses and grades; extract students' main info, GPA, etc.; show the summary     of results on a pdf for each individual student
3. Utilize database (mySQL) for pdfs, texts storage; mangoDB (?) for json results storage
4. Build an AI probability predictor for admission results based on UCLA admission data (weight on different parameters).
5. Recommendation letter sentiment analysis
6. Application name / logo design


### Tasks for Sprint 3:
1. Web application / PC Applicaiton: http://cs-people.bu.edu/liuyu529/EC601/UI.html

### Content:

#### 1. [Meeting with Professor Trachtenberg](https://github.com/daisysj/EC601-Project-Automated-Admission-System/blob/master/2019.9.24%20Meeting%20with%20Prof.%20Trachtenberg.pdf)

#### 2. User Stories & MVP

#### 3. [Industry Review](https://github.com/daisysj/EC601-Project-Automated-Admission-System/blob/master/Sprint%201_Industry%20Review.pdf)

