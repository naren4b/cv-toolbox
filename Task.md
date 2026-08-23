I want to build a Personal Job Application Manager which will take these details from the /data directory 

Input:
1. Current CV
2. Personal Information: Email,Phone Number ,Address, DOB 
3. Current Employer: Name,Job Title,Employment Start Date, Location, Notice Period, CTC
4. Expected Salary
5. Reason for Change 
6. Company Info and JD
7. Email Communication - interview Schedule 

And can generate any of the below artifacts 
Output:
1. Company Profile
2. Financial,Domain, Locations, Salary range , Work life balance 
3. Tailored  CV
4. Email Reply
5. Cover Letter
6. Interview Preparation , Interview Questions


Create Agents 
 - Create an Agent which will generate a tailored CV at (jobs/[company]/cv-${date}.md) with given Job details in the jobs/[company]/jd.txt
 - Create an Agent which will compose email reply(jobs/[company]/email-reply.md) for a given jobs/[company]/jd.txt and jobs/[company]/email.txt
 - research a company before an interview — financials, culture, salary benchmarks, and strategic insights. Keywords: company research, salary range, work culture, Glassdoor, company profile, market study
Create SKILL
 - Ready-to-use email templates, recruiter reply strategies, and cover letter framework for job applications
 - Actionable guide to upgrade every LinkedIn section for recruiter visibility and inbound leads.
 - Master career profile and CV tailoring guide.When given a new Job Description (JD), use this file as the single source of truth to generate a targeted CV.

All input and asked input will be only stay in the data directory  




