![aacbanner](https://i.pinimg.com/originals/72/f6/df/72f6dfa7856f808ba6ff9a2074c4cfa0.gif)
<p>
  <a href="https://github.com/aliciag92" target="_blank">
    <img alt="Alicia" src="https://img.shields.io/github/followers/aliciag92?label=Follow_Alicia&style=social" />
  </a> 
  <a href="https://github.com/o0amandagomez0o" target="_blank">
    <img alt="Amanda" src="https://img.shields.io/github/followers/o0amandagomez0o?label=Follow_Amanda&style=social" />
  </a>
    <a href="https://github.com/barbmarques" target="_blank">
    <img alt="Barbara" src="https://img.shields.io/github/followers/barbmarques?label=Follow_Barbara&style=social" />
  </a>
      <a href="https://github.com/mdalton87" target="_blank">
    <img alt="Matthew" src="https://img.shields.io/github/followers/mdalton87?label=Follow_Matt&style=social" />
  </a>
    <a href="https://github.com/MG-Squared" target="_blank">
    <img alt="Matthew" src="https://img.shields.io/github/followers/MG-Squared?label=Follow_MG-Squared&style=social" />
  </a>


</p>

**Tools & Technologies Used:** 

![](https://img.shields.io/static/v1?message=Python&logo=python&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Pandas&logo=pandas&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciKit-Learn&logo=scikit-learn&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciPy&logo=scipy&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Yellowbrick&logo=scikit-learn&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=NLTK&logo=python&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=NumPy&logo=numpy&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=MatPlotLib&logo=python&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Seaborn&logo=python&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Tableau&logo=tableau&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Canva&logo=canva&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Markdown&logo=markdown&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=GitHub&logo=github&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=JupyterLab&logo=jupyter&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=DeepNote&logo=deepnote&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Trello&logo=trello&labelColor=5c5c5c&color=2f5f98&logoColor=white&label=%20)




___

<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___
<a name="project-summary"></a><h1><img src="https://i.pinimg.com/originals/f9/f0/89/f9f0892a1a7249eeadffa3800e034cd2.png"/></h1>

Across the United States, there are altercations that result in killings by police officers, whether on-duty or off-duty. Each case is considered as a person dying from being shot, beaten, restrained, intentionally hit by a police vehicle, pepper sprayed, tasered, or otherwise harmed by police. 

For our capstone, we are addressing the issue of police violence that has become a heated topic throughout the country in the recent years. As a team, we will be attempting to help law enforcement agencies spot risk factors so they may step in before risk transforms into actual harm.  

The dataset we acquired from [Mapping Police Violence](https://mappingpoliceviolence.org/aboutthedata) has gathered over 9,000 police killings from January 2013 to May 2021. Analyzing the features surrounding fatal encounters will shed light on changes to be made to save more lives. After creating a classification model to predict the threat level of the victim, we've cast a larger net and acquired the 30,000+ [Fatal Encounters](https://fatalencounters.org/tools-for-journalists/) dataset that was originally used to create the Mapping Police Violence dataset used in the first iteration. The final classification model we have created beat the baseline model by 20%.


<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/db/f8/d9/dbf8d911ea72d584177fac7b20735afc.png"/></h1>
### Goal: 
Analyze attributes of civilian fatalities in police altercations in the United States in order to shed light on changes to be made to save more lives. Dataset features will be used to build a classification model predicting whether the victim was indeed an attacker.


### Initial Hypotheses:

> Hypothesis₁
>
> There is relationship between bodycam usage and threat.
    
> Hypothesis₂
>
> There is a difference between male and female fatalities.
<details>
  <summary>Click to see full list. </summary>    
> Hypothesis₃
>
> There is a difference between mental health factor fatalities and non-mental health fatalities.
    
> Hypothesis₄
>
> The cause of death and civilian fleeing are independent.
    
> Hypothesis0
>
> Race is a factor.
    
> Hypothesis₆
>
> More killings occur in urban vs rural areas.
</details>    



### Project Planning Initial Thoughts:
**Initial Questions:**
- How many fatalities happened as a result of an attack by the civilian? (alleged threat level)
- What are the fatalities by state: % killings vs pop
- Is race a factor?
- Does the police officer having a bodycam make a difference?
- Where and what areas result in more killings?
- What is happening in suburban fatalities?
- Do symptoms of mental illness play a role in threat level?

**First iteration:**
- Clean datatset
- Explore questions & hypotheses visually 
- Encode attributes for ML ease
- Run statistical test on hypothese
- Fill in as many blank/ambiguous observations of our target variable `alleged_threat_lvl`
- Use feature importance to narrow down list of features to feed into our ML model
- Use various classification models on split data to create the best model

**Second iteration:**
- Bring in more data via [Fatal Encounters](https://fatalencounters.org/tools-for-journalists/)!
- RE-clean
- Analyze lesser features available 
    - use feature importance to identify useful attributes
- Create a better model, we have the technology!
   
    
**Deliverables:**
- A well-documented jupyter notebook detailing the data science pipeline process.
- README.md file containing overall project information.
- Python modules that automate the data acquisition, preparation, and exploration process.
- 10-15 minute presentation along with slide deck.

    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/cc/c6/68/ccc66826469848960e2babbba9a07c6e.png"/></h1>

## Exploration Key Findings:
### Univariate
- Most fatalities are male
- Mode of **dataset**:
    - Race is white
    - Symptoms of mental illness: No
    - Were allegedly armed
    - Had attempted to attack the police or others
    - Did not have survelliance footage 
    - Occurred with an **Off-Duty** officer


### Bivariate
- Male fatalities were 68% likely to be an attacker
    - only 20% of men had known mental illness
- Female fatalities were 59% likely to be an attacker
    - only 27% of women had known mental illness
- There is not much variation in the attack threat level and non-attack threat level among the mental illness categories.
    - Highest percentage of non-attacks are people under the influence of drugs/alcohol.
- The highest occurrence of attacks are seen in White races. Second highest appears to be Black races.
    - The highest occurrence of non-attacks are seen in Native Americans. Second highest is Hispanics.
- There seems to be more attacks than non-attacks overall, regardless if body camera is on or off.
    - When bodycam is on, there is a higher chance of a non-attack threat level, than when the body camera is off.
    - In contrast, when the body camera is off, there is a higher chance of an attack threat level, than when the body camera is on.
    

### Multivariate
- 




[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/ed/ad/49/edad4911bf29d36d0b542345f02eac0f.png"/></h1>


> #### Hypothesis₁
>
> H₀ = There is not a difference between male attackers and the remaining population.
>
> H𝛼 = Attacker status for males & total population are different.
> - **We reject the null hypothesis: There is not a difference between male attackers and the remaining population.**<br>
    **Therefore, we can move forward with alternative hypothesis: Attacker status for males & total population are different.**

<details>
  <summary>Click to see full list. </summary>
    
> #### Hypothesis₂
>
> H₀ = Mental status is independent on alleged threat level.
>
> H𝛼 = Mental status is dependent on alleged threat level.
> - **We reject the null hypothesis: Mental status is independent of alleged threat level.**<br>
    **Therefore: Mental status is dependent on alleged threat level.**
    
> #### Hypothesis₃
>
> H₀ = There is independence between the cause of death and civilian threat level.
>
> H𝛼 = There is a dependent relationship between the cause of death and civilian threat level.
> - **We reject the null hypothesis: There is independence between the cause of death and civilian threat level.**<br>
    **Therefore: There is a dependent relationship between the cause of death and civilian threat level.**
           
    
> #### Hypothesis₄
>
> H₀ = There is independence between the use of bodycams and civilian threat level.
>
> H𝛼 = There is a dependent relationship between the the use of bodycams and civilian threat level.
> - **We reject the null hypothesis: There is independence between the use of bodycams and civilian threat level.**<br>
    **Therefore: There is a dependent relationship between the the use of bodycams and civilian threat level.**
               
</details>


    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/66/e9/a5/66e9a50ef4fb3bed4bf122d18a56d56b.png"/></h1>

- 



[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/ba/e3/e5/bae3e50304dea6bd20e3f065f87b456c.png"/></h1>

| column_name  | description                                                           | key                          | dtype  |
|-------------|-----------------------------------------------------------------------|------------------------------|--------|
| age | Age of victim in years.   |  |int64 |
| age bins | This category consists of the following bins: age unknown, under 12, 12-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+ | |uint8|
| agency_responsible  |  Identifies the agency represented at the incident (police department, sheriff's office, marshall's office, etc.).    |     | object  |
| alleged_threat_lvl | Indicates whether or not the officer was allegedly attacked by the victim.  | 0 = No, 1 = Yes  | float64 |
| alleged_weapon |Alleged weapon of the victim. |         | object |
| armed_unarmed_status|A person was coded as 'unarmed' if there were not holding any objects or weapons when killed, if they were holding personal items that were not used to attack others (ex: cellphone, cane, etc.), if they were holding a toy weapon (ex. BB gun, pellet gun, air rifle, toy sword), if they were an innocent bystander or hostage, or a person or motorist killed after being intentionally hit by a police car or as a result of hitting police stop sticks during a pursuit. This category is further broken down using dummy variables in the categories of was_allegedly_armed, was_unarmed, was_vehicle| 0 = No, 1 = Yes (float64)| object |
| body_camera|Indicates whether or not police body camera footage of the event is available. |    0: No Body Cam / 1: Body Cam | float64 |
| cause_of_death | Victim's cause of death: (gunshot, taser, vehicle, physical restraint, beaten, baton, bomb, police dog, asphyxiation, pepper spray, chemical agent, other).  | | object  |
| city | City where incident occurred.|      | object  |
| county| County where incident occurred. | | object |
| criminal_charges_filed|Indicates whether or not charges were filed against the officer for the killing.   | | object |
| date  | Date of incident. |                        | datetime64[ns]  |
| description_of_circumstances |Brief description of the incident's offense and outcome.  | | object |
| encounter_type_draft| Classifies each incidence as: violent crime, person with a weapon, domestic disturbance, traffic stop, mental health/welfare check, other non-violent offense, other crimes again people, or unknown. This is further broken down into dummy variables: was_domestic_disturbance, was_mental_health_walfare_check, was_person_with_a_weapon, was_traffic_stop, was_violent_crime_part_1    |0 = No, 1 = Yes (uint8) | object |
| fleeing      | Indicates whether or not the victim was fleeing (on foot, by car or other vehicle) at the time of the incident. Further broken down into was_fleeing, was_not_fleeing | 0 = No / 1 = Yes (float64) | object |
| gender | Gender of victim: is_male, is_female or is_transgender. | 0 = No, 1 = Yes (uint8)   | object |
| geography  | The location of the incident is classified as either: suburban, urban, rural. These were further broken down into dummy variables: rural, suburban,and urban. |   0 = No, 1 = Yes (float)                            | object |
| initial_reported_reason_for_encounter_draft| Reason for initial encounter with police.                   |                              | object |
| known_past_shootings_of_officer_draft | Indicates whether the officer involved has been involved in past shootings.             |    | object  |
| mental_illness   |Indicates whether the victim was identified as having a mental illness. Broken down into the following categories: mntlill_drug or alcohol use (reported that victim had symptoms of drug or alcohol use), mntlill_no (reported that victim had no symptoms of mental illness ), mntlill_unknown (unknown whether victim had symptoms of mental illness), mntlill_yes (reported that victim had symptoms of mental illness)| 0 = No, 1 = Yes (uint8) | object  |
| official_disposition  |Indicates the status of charges, if they were filed against the officer.| | object |
| race|  Race of victim: is_white, is_black, is_hispanic, is_asian/pacific islander, is_native american, or is_unknown race. |  0 = No, 1 = Yes (uint8) | object |
| state |  State where incident occurred.    |    |object |
| zipcode | Zip code where incident occurred.  |  | float64 |





















<details>
  <summary>Click to see full list. 
      
   </summary>

    
    Data Dictionary of Fatal Encounters Data Set

 
| column_name                      | description                        | key              | dtype |
|----------------------------------|------------------------------------|------------------|-------|
| age | Age of victim in years.   |  |int64 |   
| age bins | This category consists of the following bins: under 12, 12-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+ | |float64|
| agency_or_agencies_involved |  Identifies the agency represented at the incident (police department, sheriff's office, marshall's office, etc.).    |     | object  |
| alleged_threat_lvl | Indicates type of threat alleged: threat, no threat, ambiguous threat  |  | object |
| alleged_weapon |Alleged weapon of the victim. This is further broken down into dummy variables: is_unarmed, had_blunt object, had_edged weapon, had_firearm, had_no_weapon, had_other_weapon |  0 = No / 1 = Yes (uint8)       | object |
| armed_unarmed|A person was coded as 'unarmed' if there were not holding any objects or weapons when killed, if they were holding personal items that were not used to attack others (ex: cellphone, cane, etc.), if they were holding a toy weapon (ex. BB gun, pellet gun, air rifle, toy sword), if they were an innocent bystander or hostage, or a person or motorist killed after being intentionally hit by a police car or as a result of hitting police stop sticks during a pursuit. |  (float64)| object |
| brief_description |Brief description of the incident's circumstances, offense and outcome.  | | object |
| date_of_injury_resulting_in_death  | Date of incident. |                        | datetime64[ns]  |
|fleeing | Indicates whether the victim was fleeing at the time of injury causing death | 0 = No / 1 = Yes | float64|
|fleeing_not_fleeing | Indicates whether or not victim was fleeing at the time of injury causing death | | object |
| gender | Gender of victim: male,female or transgender. | | object |
|intended_use_of_force_developing | deadly force, suicide, vehicle/pursuit, pursuit, less than lethal force, no force, vehicle,or undetermined | | object |
| location_of_death_zipcode | Zip code where incident occurred.  |  | float64 |
| race|  Race of victim: white, black, hispanic, unknown race, asian/pacific islander, native_american, middle eastern. Further broken down into dummy variables: is_asian/pacific islander, is_white, is_black, is_hispanic, is_middle_eastern, is_native american, or is_unknown race.| 0 = No, 1 = Yes uint8 | object |
| unique_id | Encounter identification number assigned by Fatal Encounters data set | | float64|
</details>

[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/48/73/ee/4873eebc981e262ed0fbde3a3a1d56fd.png"/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the Map Police Violence's data [here](https://mappingpoliceviolence.org/).
![mpvbanner](https://i.pinimg.com/originals/42/40/be/4240beaece83903f4f568f73a46723d8.png)

As well as our second dataset from [Fatal Encounters](https://fatalencounters.org)

![FEbanner](https://i.pinimg.com/originals/3a/31/e0/3a31e035a9f1b01a2b05169e3a266e4f.png)

2. Recover your downloaded file.

**Prep your repo.**

3. Clone our repository to your local computer by selecting "Code" and clone it into your terminal by copying (`Cmd+C`) the SSH link:
    ![prep your repo](https://i.pinimg.com/originals/02/fc/22/02fc222b566f9766712c9658d67759a1.png)
> <code>git clone </code> (Cmd+V)
    

4. Create a `.gitignore` that includes any files you dont want shared on the internet and **push it**! 
    
    - (This can include your newly downloaded .xlsx file)
> <code>code .gitignore</code>



5. Create a `README.md` file to begin notating steps taken so far.
    
><code>code README.md</code>


6. Transfer your .xlsx file into your newly established folder.


7. Create a Jupyter Lab environment to continue working in.
> <code>jupyter lab</code>


8. Create Jupyter Notebook to begin the data pipeline. 

![jlablauncher](https://i.pinimg.com/originals/98/92/c5/9892c5042934750b5ba073f2d49f6184.png)
    




[Jump to Navigation](#navigation)







