import os
import serpapi
from datetime import datetime
import pytz
# import json

timezone = pytz.timezone("Asia/Dhaka")

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

if not SERPAPI_API_KEY:
    raise ValueError(
        "No SERPAPI_API_KEY found in environment variables. Please set it before running the script."
    )


def fetch_jobs_from_serpapi():
    # client = serpapi.Client(api_key=SERPAPI_API_KEY)

    # params = {
    #     "engine": "google_jobs",
    #     "q": "data engineer",
    #     "location": "Dhaka",
    #     "api_key": SERPAPI_API_KEY,
    # }

    # results = client.search(params)

    # return results['jobs_results']

    return [
        {
            "title": "Senior Data Engineer",
            "company_name": "Noora Health",
            "location": "Dhaka, Bangladesh",
            "via": "RippleWorks Job Board",
            "share_link": "https://www.google.com/search?ibp=htl;jobs&q=data+engineer&htidocid=gtlTSZsrhk3C5-74AAAAAA%3D%3D&hl=en-US&shndl=-1&shem=vslcca&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=data+engineer&htidocid=gtlTSZsrhk3C5-74AAAAAA%3D%3D",
            "thumbnail": "https://serpapi.com/searches/66c8fbd069f8ec6845c68eca/images/0883f78020a3efd6ae642a9341baa6996513e858f0892d96ce8b6667881fbcd0.jpeg",
            "extensions": ["Full-time"],
            "detected_extensions": {"schedule_type": "Full-time"},
            "description": "Noora Health\u2019s mission is to improve outcomes and strengthen health systems by equipping family caregivers with the skills they need to care for their loved ones.\n\nFounded in 2014, Noora Health turns hospital hallways and waiting rooms into classrooms by tapping into the most compassionate resources available for the patient\u2019s care: their own family.\n\nWith support from governments and partners in India, Bangladesh, and Indonesia, Noora Health has trained more than 3.5 million caregivers across 460+ facilities using their flagship caregiver education and training curriculum, the Care Companion Program (CCP).\n\nIn a cohort of patients, the CCP reduced post-surgical cardiac complications by 71%, maternal complications by 12%, newborn complications by 16%, and newborn readmissions by 56%.\n\nNoora Health was honored as a TED 2022 Audacious Project Grantee and recipient of the 2022 Skoll Foundation Award for Social Innovation. Featuring Edith Elliott and Shahed Alam, our Co-Founders and Co-CEOs, Noora Health\u2019s mission took the spotlight at TED 2022 and was also featured in a 2022 Skoll video.\n\nABOUT SHARED PLATFORMS\n\nThe Shared Platforms team leads the strategy, development, and implementation of digital products and services across the different geographies that Noora operates in currently \u2013 India, Bangladesh, and Indonesia. We value being close to our users (patients and caregivers, as well as our internal team members) and using data and technology to solve for user needs - sustainably and at scale. We strive to become leaders and innovators in using cutting edge technology to improve outcomes in public health. We are a team of product managers, engineers, and data analysts.\n\nROLE SUMMARY\n\nData is integral to decision-making at Noora. However, data about our users and operations are scattered across multiple platforms and applications that are used to run our interventions. We recently started integrating data from these various sources into a centralized warehouse. You will be responsible for further extending and maintaining this central data system \u2013 including integrating new data sources, building robust pipelines and transformation models, and co-designing and implementing data governance policies across all the geographies we operate in.\n\nWHAT YOU WILL DO\n\u2022 Design, develop, and maintain scalable data pipelines, ETL processes, and data warehouse structures to ensure data quality and accessibility for analytics and reporting\n\u2022 Collaborate with program delivery, program design and platforms teams to gather requirements, develop data models, and design analytics solutions that address specific business needs\n\u2022 Implement data governance and security measures based on our respective regions of operation\n\u2022 Support data analysts and monitoring teams to build dashboards and communicate challenges and insights back to the larger team\n\u2022 Manage our data warehouse and ensure performant databases for querying and dashboarding purposes.\n\u2022 Develop and maintain data visualizations and dashboards to track key performance indicators (KPIs) and monitor business trends\n\u2022 Support the engineering team in refining schemas for our applications based on needs coming from internal and external stakeholder requirements.\n\nWHO WE ARE LOOKING FOR\n\u2022 Bachelor's or Master's degree in Computer Science, Data Science, Engineering, or a related field.\n\u2022 5+ years of proven experience in data analysis, engineering, data management or other equivalent fields\n\u2022 Knowledge of data warehousing, database design, and data modeling techniques.\n\u2022 Strong proficiency in SQL, Python, and data manipulation languages (DML)\n\u2022 Hands-on experience with data pipeline and ELT/ETL tools (e.g., Fivetran, Airbyte, dbt)\n\u2022 Familiarity with cloud-based data warehouse and data processing platforms (e.g., BigQuery, Snowflake, Databricks)\n\u2022 Proficiency in data visualization and reporting tools (e.g., Tableau, Metabase, Superset, PowerBI)\n\u2022 Strong analytical, problem-solving, and communication skills, with the ability to translate complex data into actionable insights for non-technical stakeholders.\n\u2022 Detail-oriented, self-motivated, and able to work independently as well as collaboratively within a team.\n\nAt Noora Health, we value diversity, equity, and inclusion, and we understand the value of developing a team with different perspectives, educational backgrounds, and life experiences. We prioritize diversity within our team, and we welcome candidates from all gender identities, castes, religious practices, sexual orientations, and abilities \u2013 among many others.\n\nWe encourage people from all backgrounds to apply for positions at Noora Health.",
            "apply_options": [
                {
                    "title": "RippleWorks Job Board",
                    "link": "https://careers.rippleworks.org/companies/noora-health/jobs/35076173-senior-data-engineer?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                },
                {
                    "title": "Devcareer.org",
                    "link": "https://devcareer.org/job/job-opportunity-for-senior-data-engineer-at-noora-health-in-bangalore-karnataka/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                },
            ],
            "job_id": "eyJqb2JfdGl0bGUiOiJTZW5pb3IgRGF0YSBFbmdpbmVlciIsImNvbXBhbnlfbmFtZSI6Ik5vb3JhIEhlYWx0aCIsImFkZHJlc3NfY2l0eSI6IkRoYWthLCBCYW5nbGFkZXNoIiwiaHRpZG9jaWQiOiJndGxUU1pzcmhrM0M1LTc0QUFBQUFBPT0iLCJ1dWxlIjoidytDQUlRSUNJWlJHaGhhMkVnUkdsMmFYTnBiMjRzUW1GdVoyeGhaR1Z6YUEifQ==",
        },
        {
            "title": "Senior Data Engineer (remote, Canada)",
            "company_name": "NearForm",
            "location": "Khulna Division, Bangladesh",
            "via": "The Org",
            "share_link": "https://www.google.com/search?ibp=htl;jobs&q=data+engineer&htidocid=x84rTbqGhyuhgHDnAAAAAA%3D%3D&hl=en-US&shndl=-1&shem=vslcca&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=data+engineer&htidocid=x84rTbqGhyuhgHDnAAAAAA%3D%3D",
            "thumbnail": "https://serpapi.com/searches/66c8fbd069f8ec6845c68eca/images/0883f78020a3efd67ef31488150a9da327b67c8957c07a6b94ce85edd5428a3a.jpeg",
            "extensions": ["28 days ago", "Full-time", "No degree mentioned"],
            "detected_extensions": {
                "posted_at": "28 days ago",
                "schedule_type": "Full-time",
            },
            "description": "This is a remote permanent position for those based in Canada.\n\nThe Role\n\nWe are looking for a Senior Data Engineer who can help our enterprise clients translate their requirements into functional and appealing interactive applications. You would be responsible for building server-side components of these applications. You will be outcome driven, and have a drive to deliver the best quality output for our clients within specific timeframes. You will be working in high performing software teams who are distributed across different locations.\n\u2022 Designing & building cloud-based applications using server-side technologies including Python, SQL, and data libraries\n\u2022 Supporting system design, development and maintenance and take responsibility for personal technical quality standards within the project team.\n\u2022 Assisting with defining structured practices, especially in source code management, building and deployment.\n\u2022 Designing and implementing data storage solutions.\n\u2022 Implementing security and data protection.\n\u2022 Troubleshooting and debugging applications.\n\u2022 Optimising applications for maximum speed and scalability.\n\u2022 Getting feedback from, and building solutions for, users and clients.\n\u2022 Working with and supporting Technical Leaders in project execution and timely delivery.\n\u2022 Collaborating with internal and client teams.\n\nEssential skills\n\nAs a Senior Data Engineer, you will be largely focused on the server side of the application development process. We are keen to hire people who can hit the ground running, as such, there are some skills and experience we really need you to have:\n\u2022 Proficient communication in English (oral and written) and excellent communication skills.\n\u2022 Experience delivering at a Senior Developer level in an enterprise and agile environment.\n\u2022 Proficient in Python, with demonstrated experience using data libraries such as Pandas, NumPy, or similar.\n\u2022 Strong proficiency in SQL, including query optimization and relational database management.\n\u2022 Hands-on experience with Apache Spark for large-scale data processing.\n\u2022 In-depth knowledge of AWS, particularly AWS Glue (jobs, data catalog, orchestration, connections, etc.), and a solid understanding of the broader AWS platform and services.\n\nNice to have\n\u2022 Previous experience with Data Lakes, including but not limited to non-AWS solutions.\n\u2022 Familiarity with open table formats such as DeltaLake, Apache Iceberg, or Apache Hudi.\n\u2022 Experience in designing and implementing robust data pipelines and data lakes.\n\u2022 Experience with Terraform for provisioning and managing cloud infrastructure.\n\u2022 Experience working as a consultant\n\nBenefits\n\u2022 Healthcare and RRSP;\n\u2022 Enjoy a comprehensive paid time off package, encompassing holidays, sick leave, and flexible vacation days. Take the time you need to recharge, care for yourself, and make the most of your moments outside of work.\n\u2022 Work remotely: we have a genuine dedication to work/life balance.\n\u2022 Work flexibility; we appreciate there are more important things in life than work so our flexible working culture allows you to work around what matters - school run, no problem!\n\u2022 Home Office Support: Receive a home office stipend to help you create a comfortable and productive workspace.\n\u2022 Investment in Growth: Access a generous professional development budget to support ongoing learning and career growth.\n\u2022 Positive Company Culture: Join a positive and collaborative company culture that places value on work-life balance.\n\u2022 The Wellness Hub: We have a genuine commitment to fostering/improving Nearformers\u2019 wellbeing; we offer resources and support, including a Nearform advice line which offers confidential support for anything from relationship issues to staying healthy.\n\nPlease get in touch to discuss remuneration.\n\nAbout Us\n\nAt NearForm, we value collaboration and a curious mindset that fuels our dynamic team. With a decade of experience, we've achieved meaningful results for our clients while maintaining the agile and transparent ethos of a startup.\n\nOur focus on digital transformation means creating practical, user-centric products that help enterprises enter markets quickly, enhance customer experiences, and reshape workflows. Bolstered by recent investment, NearForm is gearing up to extend its impact to more enterprises.\n\nDespite our global presence, NearFormers form a close-knit community built on trust and camaraderie. Join us at NearForm and be part of a journey marked by innovation and progress.\n\nRecruitment/Application process\n\u2022 A TalentCall with someone from the Talent team (30 mins approx.) to introduce to you NearForm and the role, and to make sure your experience is relevant for the position and to discuss life as a NearFormer\n\u2022 An assessment with a member of the hiring team (1 hr approx.), this session is carried out using a screen share. You will be given a challenge and asked to provide a working solution to a specified problem.\n\u2022 A video call with one of our Hiring Managers (45 mins approx.) which allows us to gain a better insight into what interests you, your technical background, and give you an overview of the work we do at NearForm.\n\nAlthough we are widely dispersed, NearFormers are a tightly-knit team. We trust one another and care about our colleagues. We all get together in person at our annual company retreat, of course when we\u2019re not faced with a global pandemic! Building on our open-source origins, we promote the sharing of thoughts, knowledge and ideas.\n\nNearForm is committed to shaping a better world in all that we do. Our global team is built based on respect, inclusivity, diversity and excellence.",
            "apply_options": [
                {
                    "title": "The Org",
                    "link": "https://theorg.com/org/nearform/jobs/senior-data-engineer-remo-a9c90068?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
                }
            ],
            "job_id": "eyJqb2JfdGl0bGUiOiJTZW5pb3IgRGF0YSBFbmdpbmVlciAocmVtb3RlLCBDYW5hZGEpIiwiY29tcGFueV9uYW1lIjoiTmVhckZvcm0iLCJhZGRyZXNzX2NpdHkiOiJLaHVsbmEgRGl2aXNpb24sIEJhbmdsYWRlc2giLCJodGlkb2NpZCI6Ing4NHJUYnFHaHl1aGdIRG5BQUFBQUE9PSIsInV1bGUiOiJ3K0NBSVFJQ0laUkdoaGEyRWdSR2wyYVhOcGIyNHNRbUZ1WjJ4aFpHVnphQSJ9",
        },
    ]

    # if results and isinstance(results, dict):
    #     if 'jobs_results' in results:
    #         return results['jobs_results']
    #     else:
    #         print(f"Error: 'jobs_results' not found in the response. Full Response: {results}")
    #     return None
    # else:
    #     print(f"Error fetching data from SerpApi: {results.get('error', 'Unknown error')}")
    #     return None


def scrape_jobs():
    job_data = fetch_jobs_from_serpapi()
    jobs = []

    if job_data:
        for job in job_data:
            title = job.get("title", "N/A")
            company = job.get("company_name", "N/A")
            location = job.get("location", "N/A")
            link = job.get("share_link", "N/A")
            posted_date_str = job.get("date_posted", "")

            try:
                posted_date = datetime.strptime(posted_date_str, "%Y-%m-%d")

                if posted_date.tzinfo is None:
                    posted_date = timezone.localize(posted_date)
                else:
                    posted_date = posted_date.astimezone(timezone)

            except ValueError:
                posted_date = timezone.localize(datetime.now())

            jobs.append(
                {
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link,
                    "posted_date": posted_date.isoformat(),
                }
            )
    return jobs
