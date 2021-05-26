![aacbanner](https://i.pinimg.com/originals/72/f6/df/72f6dfa7856f808ba6ff9a2074c4cfa0.gif)

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

The open-sourced dataset we acquired from [Mapping Police Violence](https://mappingpoliceviolence.org/aboutthedata) has gathered over 9000 police killings from January 2013 to May 2021. Top drivers of civilian fatalities identified will shed light on changes to be made to save more lives. Then, we will use the features to apply to our classification models predicting the threat level of the victim (attacker or not).


<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/db/f8/d9/dbf8d911ea72d584177fac7b20735afc.png"/></h1>
### Goal: 
Identify top drivers of civilian fatalities in police altercations in the United States in order to shed light on changes to be made to save more lives. Dataset features will be used to build a classification model predicting whether the victim was indeed an attacker.

### Objectives for this project include:
- Identifying the drivers of civilian fatalities. 
- Documenting the process and analysis throughout the data science pipeline.
- Constructing a classification model that can predict what the victim's threat level is, given the features of the dataset.


### Initial Hypotheses:

> Hypothesis₁
>
> There is relationship between bodycam usage and threat.
    
> Hypothesis₂
>
> There is a difference between male and female fatalities.
    
> Hypothesis₃
>
> There is a difference between mental health factor fatalities and non-mental health fatalities.
    
> Hypothesis₄
>
> The cause of death and civilian fleeing are independent.
    
> Hypothesis₅
>
> Race is a factor.
    
> Hypothesis₆
>
> More killings occur in urban vs rural areas.
    


### Initial Hypotheses:
- How many fatalities happened as a result of an attack by the civilian? (alleged threat level)
- What are the fatalities by state: % killings vs pop
- Is race a factor?
- Does the police officer having a bodycam make a difference?
- Where and what areas result in more killings?
- What is happening in suburban fatalities?
- Do symptoms of mental illness play a role in threat level?


### Project Planning Initial Thoughts:
**First iteration:**
. 

**Second iteration:**
. 

- New features:
    - Encode features using `Multilabelbinarizer()`
    
    
**Deliverables:**
- A well-documented jupyter notebook detailing the data science pipeline process.
- README.md file containing overall project information.
- Python modules that automate the data acquisition, preparation, and exploration process.
- 10-15 minute presentation along with slide deck.

    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/cc/c6/68/ccc66826469848960e2babbba9a07c6e.png"/></h1>

## Exploration Key Findings:
### Univariate
- 

### Bivariate
- 
### Multivariate
- 




[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/ed/ad/49/edad4911bf29d36d0b542345f02eac0f.png"/></h1>


> #### Hypothesis₁
>
> H₀ = 
>
> H𝛼 = 
> - **We reject the null hypothesis: Breed and adoption rates are INDEPENDENT.**<br>
    **Therefore: There is a relationship between breed and if they get adopted.**

<details>
  <summary>Click to see full list. </summary>
    
> #### Hypothesis₂
>
> H₀ = 
>
> H𝛼 = 
> - **.**<br>
    **Therefore: .**
    
          
    
</details>


    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/66/e9/a5/66e9a50ef4fb3bed4bf122d18a56d56b.png"/></h1>

- 



[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/ba/e3/e5/bae3e50304dea6bd20e3f065f87b456c.png"/></h1>

| column_name  | description                                                           | key                          | dtype  |
|-------------|-----------------------------------------------------------------------|------------------------------|--------|
| age | Age of victim in years.  |  | object |
| gender | Gender of victim. |    | object |
| race|  Race of victim. |   | object |
| date  | Date of incident. |                        | datetime  |
| city | City where incident occurred.|      | object  |
| state |  State where incident occurred.    |    | float |
| zipcode | Zip code where incident occurred.  |  | object |
| county| County where incident occurred.                           |                              | object |
| agency_responsible  |  Identifies the agency represented at the incident (police department, sheriff's office, marshall's office, etc.).    |     | object  |
| cause_of_death | Victim's cause of death: (gunshot, taser, vehicle, physical restraint, beaten, baton, bomb, police dog, asphyxiation, pepper spray, chemical agent, other).         |                              | object  |
| description_of_circumstances |Brief description of the incident's offense and outcome.  | | object |
| official_disposition  |Indicates the status of charges, if they were filed against the officer.| | object |
| criminal_charges_filed|Indicates whether or not charges were filed against the officer for the killing.   | | object |
| mental_illness   |Indicates whether the victim was identified as having a mental illness. |                              | object  |
| armed_unarmed_status |A person was coded as 'unarmed' if there were not holding any objects or weapons when killed, if they were holding personal items that were not used to attack others (ex: cellphone, cane, etc.), if they were holding a toy weapon (ex. BB gun, pellet gun, air rifle, toy sword), if they were an innocent bystander or hostage, or a person or motorist killed after being intentionally hit by a police car or as a result of hitting police stop sticks during a pursuit. | | object |
| alleged_weapon |Alleged weapon of the victim. |         | object |
| alleged_threat_lvl | Indicates whether or not the officer was allegedly attacked by the victim.  |   | object |
| fleeing      | Indicates whether or not the victim was fleeing at the time of the incident.  |   | object |
| body_camera|Indicates whether or not police body camera footage of the event is available. |                              | object |
| geography  | The location of the incident is classified as either: suburban, urban, rural, undetermined. |                              | object |
| encounter_type| Classifies each incidence as: violent crime, person with a weapon, domestic disturbance, traffic stop, mental health/welfare check, other non-violent offense, other crimes again people, or unknown.     || object |
| initial_reported_reason_for_encounter| Reason for initial encounter with police.                   |                              | object |
|race_of_officers_involved  | Indicates race of the officer involved.   |                              | object |
| known_past_shootings_of_Officer | Indicates whether the officer involved has been involved in past shootings.             |                              | object  |
| call_for_service |Indicates whether or not police were responding to a call for service regarding the incidence. ||object|

<details>
  <summary>Click to see full list. </summary>

| column_name                      | description                        | key              | dtype |
|----------------------------------|------------------------------------|------------------|-------|
| `American Pit Bull Terrier Mix` | Indicates if animal is this breed. | 1 = yes, 0 = no  | int64 |
| `American Shorthair Mix`        | Indicates if animal is this breed. | 1 = yes, 0 = no  | int64 |

        
</details>

[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/48/73/ee/4873eebc981e262ed0fbde3a3a1d56fd.png"/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the Map Police Violence's data [here](https://mappingpoliceviolence.org/).
![mpvbanner](https://i.pinimg.com/originals/42/40/be/4240beaece83903f4f568f73a46723d8.png)    

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







