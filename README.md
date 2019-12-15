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
  1. Competitors
  
     -[Ellucian](https://www.ellucian.com/solutions/ellucian-crm-recruit)
        
     -[Salesforce](https://www.salesforce.org/highered/recruiting/)
        
     -[Kira Talent](https://www.kiratalent.com/product/)
 
  2. Industry Debates
  
     -Bias
        
     -Dislike for AI algorithms
   
  3. Our Advantages
  
     -Particularity
        
     -Fairness
 
  4. Our Limitations
  
     -Limited Data Access
        
     -Limited Factors

- ### Technology selections and reasons:
  1. JavaScript
  
     -It's supported by all major browsers
        
     -Similar syntax to C
        
     -Doesn't need complier 

  2. Python
  
     -We are familiar with Python
        
     -Third-party modules to interact across platforms and languages
        
     -Large libraries make coding easier
 
  3. PDF Converter API
 
  4. Google Natural Language API
 
  5. Mysql
  
     -Great for storing word documents 
        
     -Encrypted conncection
   
- ### Initial decisions on implementation path:
<img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/Architecture.png">

- ### Tasks for Sprint 2:
    - Crawl data from different university websites for course numbers and names
    - Processing transcripts texts, generate a dictionary for courses and grades; extract students' main info, GPA, etc.; show the summary of results on a pdf for each individual student
    - Utilize database (mySQL) for pdfs, texts storage; mangoDB (?) for json results storage
    - Build an AI probability predictor for admission results based on UCLA admission data (weight on different parameters).
    - Recommendation letter sentiment analysis
    - Application name / logo design

- ### Tasks for Sprint 3:
    - Web application</br>

## [Sprint 2](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Sprint%202%20Presentation.pdf) 
- ### Project Components
    - Transcript Processing
    - Recommendation Letter Sentiment Analysis
    - Probability of admission
    - Generate a summary of all above parameters for each student 
- ### System Architecture
  <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/sprint%202_general%20architecture.png">
  <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/sprint%202_transcript%20processing.png">

- ### Machine Learning Algorithm
    - Random Forest Regression Model
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Machine%20Learning%20Algorithm_featureimportance.PNG">

- ### Tasks for Sprint 3
    - Utilize database (MySQL)
    - Expand data scraping scale, pass the module to Professor Trachtenberg for testing
    - Add score report processing
    - Add firewall protection to the file uploading process (utilize open-source security framework??)
    - Work on website design (file uploading system, etc.)</br>

## [Sprint 3](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/poster_final.pdf)
- ### Results Demonstration
    1. Log-in Page
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/UI/login.PNG">
    
    2. Transcript Upload Page
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/UI/transcript%20upload.PNG">
    
    3. Recommendation Letter Upload Page
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/UI/recommendation%20letter%20upload.PNG">
    
    4. Admission Probability Predictor Page
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/UI/probability%20predictor.PNG">
    
    5. Sample Report Page
    <img src = "https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/UI/report.PNG">

- ### Future Improvements
    - Expand data scraping scale (include university courses from other countries)
    - Add GRE, TOEFL score reports processing
    - Allow uploading multiple files (in zip)
    - Allow comparisons between different machine learning models 
    - Gather more data for system testing
    - Work on UI more 

- ### Reflections
    - Yu Liu: Through this project, we focused on a few aspects of machine learning algorithm design and web development. The part I  enjoyed the most is how we processed and analyzed the dataset, from which we could acquire useful information. After studying several different algorithms, we accomplished the machine learning module successfully. Neverthelss, what I found the most difficult is to integrate everything we've done into a product, since we had to adjust all the components so as to make the product work more smoothly. In a word, I learned a lot about agile software development from this project, which helps lay a solid foundation for future career.
    
    - Shengyao Shao: When trying to apply the database to this project, we had to face a number of obstacles. From small problems like having trouble downloading and installing the software required for MySQL database, to how we could make the database work more efficiently. After carefully going through the documentation MySQL provided and all kinds of tutorials available on the forums, we were able to save the file path to database and retrieve the file using this link. It was a great learning experience for us since none of use has used database before. 

    - Jing Song: The transcript processing part of the project was completely new to me, and I have learned a lot about data scraping and manually extracting information from txt files throughout the process. I have written a web application in python with Django before, and I think it is really interesting to try Flask this time, and I could feel the difference between the two modules. Though there is still a lot of room for improvements, I think we have done a great job realizing most of the expectations for the application that we had at the beginning of project. I feel very proud of this project. It is definitely a great experience that will also prepare me for my future career.

## Content:

  1. [Meeting with Professor Trachtenberg](https://github.com/daisysj/EC601-Project-AAS/blob/master/2019.9.24%20Meeting%20with%20Prof.%20Trachtenberg.pdf)

  2. [Industry Review](https://github.com/daisysj/EC601-Project-AAS/blob/master/Sprint%201_Industry%20Review.pdf)
  
  3. Application Main Program Files
  
     - [Convert PDF to TXT .py](https://github.com/daisysj/EC601-Project-AAS/blob/master/pdf_converter.py)
  
     - [Transcript Processing .py](https://github.com/daisysj/EC601-Project-AAS/blob/master/get_transcript_info.py)
     
     - [Recommendation Letter Sentiment Analysis .py](https://github.com/daisysj/EC601-Project-AAS/blob/master/recommlett_senti.py)
     
     - [Admission Probability Predictor .py](https://github.com/daisysj/EC601-Project-AAS/blob/master/predict_ver2.py)
     
     - [UI htmls](https://github.com/daisysj/EC601-Project-AAS/tree/master/templates)
  
  4. Sample Test Files
  
     - [Transcript Sample PDF](https://github.com/daisysj/EC601-Project-AAS/blob/master/Demo%20Transcript.pdf)
     
     - [Recommendation Letter Sample PDF](https://github.com/daisysj/EC601-Project-AAS/blob/master/Recommendation%20Letter%20Sample.pdf)
  
  5. [Presentations](https://github.com/daisysj/EC601-Project-AAS/tree/master/presentation)
  
     - [Sprint 1 Presentation Powerpoints](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Sprint%201%20Presentation.pdf)
     
     - [Sprint 2 Presentation Powerpoints](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/Sprint%202%20Presentation.pdf)
     
     - [Poster Presentation](https://github.com/daisysj/EC601-Project-AAS/blob/master/presentation/poster_final.pdf)
     

