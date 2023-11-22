<!---
HACKACITY 2023
-->

<h1 align="center">
  <img src="https://github.com/jotavare/hackacity-2023/blob/main/github_banner_hackacity_2023_v2.png">
</h1>

<p align="center">
	<img src="https://img.shields.io/badge/status-ongoing-success?color=%76B82A&style=flat-square" />
	<img src="https://img.shields.io/badge/place-1st-success?color=%76B82A&style=flat-square" />
	<img src="https://img.shields.io/github/last-commit/jotavare/42-resources?color=%76B82A&style=flat-square" />
</p>

<p align="center">
	<a href="#about">about</a> •
	<a href="#rules">rules</a> •
	<a href="#links">links</a> •
	<a href="#project-pipeline">project pipeline</a> •
	<a href="#tools">tools</a> •
	<a href="#data-quality">data quality</a> •
	<a href="#py-venv">py venv</a> •
	<a href="#team">team</a>
</p>

## ABOUT
Hackacity is a one-of-a-kind hackathon that explores the potential of city data to develop solutions that will impact the community.

This repository is a mix of ideas, tools and information used to complete the [**Hackacity 2023**](https://hackacity.eu/) event, in Porto. It contains code developed and graded by a jury on 24/11/2023.

There were already 5 previous editions in Porto, the last one was in 2022. In this edition, there were **34 Teams**, **151 Participants**, **13 Mentors** and **6 jury members** in total that participated and worked together at [**Museu do Carro Elétrico**](https://www.google.com/maps/place/Tram+Museum/@41.1488633,-8.6393806,16.64z/data=!4m6!3m5!1s0xd24650d6e5d4f6d:0xb0933e834cc8bbfc!8m2!3d41.1475668!4d-8.6329328!16s%2Fg%2F122vkwkb?entry=tts) in Porto, Portugal.

## RULES
- _"The event starts at 08h30, all the teams should arrive at the venue before 08h15."_
- _"All the participants should remain at the venue during the event."_
- _"All the participants must bring their own laptop or other necessary equipment."_
- _"Your team must deliver the presentation and the produced code by 18:00."_
- _"Presentations should be in .pptx or PDF format."_
- _"Produced code/jupyter notebooks should be sent in a .ZIP folder."_
- _"Deliverables will be uploaded to a One Drive. The link will be provided once the event starts."_
- _"Make sure your team send the deliverables on time. Any delay could result in disqualification."_

> [!NOTE]
> _"To be eligible for the Data Quality Award, participants must add an additional slide to their presentation to explicitly address its relevance to the evaluation criteria, namely the relevant external resources and feedback on data improvements."_

## LINKS
> Information and resources that may help with the project.
- [Import JSON Data Into Google Spreadsheets Fast](https://youtu.be/AS2IR6We4bY?feature=shared) `Youtube`
- [How To Create A Correlation Matrix In Excel (With Colors!)](https://youtu.be/TkNt8KFm0LQ?si=ip4ZI9LCP4-uVGAy) `Youtube`

> Necessary links for the Hackacity event progress.
- [Participants Guidebook](https://associacaoportodigital-my.sharepoint.com/:b:/g/personal/hi_hackacity_eu/EY7GK5ZFBwpAltyD4pmRYpcBwJmdTI__xsyZYBA3f_IGJA?e=4%3a0wTYsD&fromShare=true&at=9) `OneDrive` `PDF`
- [UrbanX Submission Folder](https://associacaoportodigital-my.sharepoint.com/:f:/g/personal/hi_hackacity_eu/EiZ6lAvUYIdBoXyDW9GCVJkBai7SE1ZC2dC2v-UCqK2XoQ?e=5%3acZqJc3&fromShare=true&at=9) `OneDrive`

> Past hackacity projects.
- [hackacity2019](https://github.com/msramalho/hackacity2019/tree/master)

## PROJECT PIPELINE
- Interact with API or download the database. If it's the first, we can use Python or Postman.
- Know what data we are working with. If necessary go to external sources.
- Sanitize data and remove noise data. Depends a lot on the problem.

## TOOLS
We should have these programs/tools installed and/or know about them (know they exist):
- Python
- Linux/Windows
- Office 365 (Excel)
- Visual Studio Code
- Jupyter Notebook
- Postman

## DATA QUALITY
> [!CAUTION]
> The questions below are case-to-case dependent. For example, some empty fields may be empty/null on purpose because they are optional. The information should be studied and taken with a grain of salt.
#### GOOD QUALITY DATA CHECK:
- [ ] **Is data missing? Is it blank? Is that blank because it's optional?**
```
C1 (Pedro) C2 (Tiago) C3 (NULL) C4 ()
```

- [ ] **Is the data conformed? What data is stored in a non-standard format?**
```
C1 (27-Out-96) C2 (19961027)
```

- [ ] **Is the data unique? Are there repeated/duplicated values? Is that necessary?**
```
C1 (01; Pedro; Oliviera; Portugal) C2 (02; Pedro; Oliviera; Portugal)
```

- [ ] **Is the data correct? Are certain values out of date?**
```
C1 (Pedro; 4000-100; Portugal) C2 (Tiago; 4350; Portugal)
```

- [ ] **Is the data valid? Spelling mistakes on standard names, roles, bad email well formulated?**
```
C1 (software engineer) C2 (soft engine)
```

- [ ] **Is the data consistent? Is there conflicting information?**
```
C1 (01; sonae; pay; 100$; 20:42) C2 (02; sonae; pay; 100$; 20:42)
```

- [ ] **Is the primary key (eg.: ID) valid? Is it missing or has an invalid format?**
```
C1 (01; sonae; pay; 100$; 20:42) C2 (NULL; sonae; pay; 100$; 20:42)
```

#### EXCEL PERCENTAGE FORMULA
We can calculate the percentage of valid data and do a correlation.
```
1 - (Total Rows / Invalid Rows)
```

#### POOR QUALITY DATA PROBLEMS:
- Waste of time and money;
- Incorrect information and decisions are misguided;
- Future opportunities missed;
- Negative image for the company;
- Lower customer satisfaction;

## PY VENV
Why create a virtual environment? We can easily share our requirement packages, so everyone can install and replicate the same environment for the program to work.
> Create a virtual environment.
```bash
python3 -m venv .venv
```

> Activate a virtual environment.
```bash
source .venv/bin/activate
```

> Deactivate a virtual environment.
```bash
deactivate
```

> Export all installed packages
```bash
python3 -m pip freeze
```

> Using a requirements.txt file to install packages
```bash
python3 -m pip install -r requirements.txt
```

## TEAM
| LinkedIn | GitHub |
| :--: | :--: |
| [Luiza Picoli Zilio](https://www.linkedin.com/in/luiza-zilio-4a7a14205/)	| [ziliolu](https://github.com/ziliolu)		|
| [Francisco Vieira](https://www.linkedin.com/in/fmotavieira/)		| [Xyckens](https://github.com/Xyckens)		|
| [Mário Henriques](https://www.linkedin.com/in/mario18/)		| [maricard18](https://github.com/maricard18)	|
| André Silva								| amenses-					|
- - - -
