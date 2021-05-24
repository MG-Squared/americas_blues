import pandas as pd 
import numpy as np 



def wrangle_data(cached=False):
    '''
    Description:
    -----------
    This function acquires and preps the Mapping Police Violence dataset
    for exploration and modeling, by performing the following tasks:
    - defaults cached setting from input to False to run prep
    - reads in original .xlsx dataset and 
    - drops unnamed columns
    - renames columns
    - specifies columns not needed/to be dropped
    - lowers string values in columns
    - fills in nulls in columns (body_camera, known_past_shootings_of_Officer_draft, fleeing)
    - groups variation of values in columns (encounter_type_draft, cause_of_death, initial_reported_reason_for_encounter_draft, mental_illness, gender, race, geography)
    - creates dummy variables for columns (mental_illness, encounter_type_draft, gender, fleeing, race, alleged_threat_lvl, armed_unarmed_status, geography, age)
    - cleans age column (replaces string and unknown values, makes col numeric, and creates bins)
    - saves doc as csv for ease of use 
    - and returns wrangled dataframe

    Parameters:
    ----------
    cached: bool,
        Default = False, True pulls from cached csv file if wrangle data has been run before.
    '''
    if cached == False:
        # convert excel file to pandas dataframe
        df = pd.read_excel('data.xlsx')
        # drop unnamed columns
        df.drop(columns=(list(df.columns[35:])), inplace=True)
        # Rename columns 
        columns = [
                    "name", "age", "gender", "race", 'img_url', 'date', 'address', \
                    'city', 'state', 'zipcode', 'county', 'agency_responsible', 'ori_agency_identifier', \
                    'cause_of_death', 'description_of_circumstances', 'official_disposition', 'criminal_charges_filed', \
                    'news_article_or_photo_of_official_document', 'mental_illness', 'armed_unarmed_status', 'alleged_weapon', \
                    'alleged_threat_lvl', 'fleeing', 'body_camera', 'wapo_id', 'off_duty_killing', 'geography', 'mpv_id', \
                    'fatal_encounters_id', 'encounter_type_draft', 'initial_reported_reason_for_encounter_draft', \
                    'names_of_officers_involved_draft', 'race_of_officers_involved_draft', 'known_past_shootings_of_officer_draft', \
                    'call_for_service_draft'
                    ]
        df.columns = columns
       
        # list of columns not needed
        dropcols = ['name', 'img_url', 'ori_agency_identifier', 'news_article_or_photo_of_official_document', 'off_duty_killing', 'wapo_id', \
        'mpv_id', 'fatal_encounters_id', 'names_of_officers_involved_draft', 'address', 'race_of_officers_involved_draft', 'call_for_service_draft', \
        'call_for_service_draft', 'race_of_officers_involved_draft']

        # dropcols dropped
        df.drop(columns=dropcols, inplace=True)
        
        # lower string values
        df['alleged_threat_lvl'] = df.alleged_threat_lvl.str.lower()
        df['race'] = df.race.str.lower().str.strip()
        df['gender'] = df.gender.str.lower().str.strip()
        df['city'] = df.city.str.lower()
        df['state'] = df.state.str.lower()
        df['county'] = df.county.str.lower()
        df['agency_responsible'] = df.agency_responsible.str.lower()
        df['cause_of_death'] = df.cause_of_death.str.lower()
        df['description_of_circumstances'] = df.description_of_circumstances.str.lower()
        df['official_disposition'] = df.official_disposition.str.lower()
        df['criminal_charges_filed'] = df.criminal_charges_filed.str.lower()
        df['mental_illness'] = df.mental_illness.str.lower()
        df['armed_unarmed_status'] = df.armed_unarmed_status.str.lower()
        df['alleged_weapon'] = df.alleged_weapon.str.lower()
        df['fleeing'] = df.fleeing.str.lower()
        df['body_camera'] = df.body_camera.str.lower()
        df['geography'] = df.geography.str.lower()
        df['encounter_type_draft'] = df.encounter_type_draft.str.lower()
        df['initial_reported_reason_for_encounter_draft'] = df.initial_reported_reason_for_encounter_draft.str.lower()

        # body cam nulls = no
        df.body_camera = df.body_camera.fillna('no')
        
        # body cam others into yes then into binary 
        df.body_camera = np.where(df['body_camera'].str.lower().str.contains('video'), "yes", df.body_camera)
        df.body_camera = df.body_camera.replace('yes', 1).replace('no', 0)
        
        # known_past_shootings_of_Officer_draft nulls, none, and no = 0
        df.known_past_shootings_of_officer_draft = df.known_past_shootings_of_officer_draft.fillna('0')
        df.known_past_shootings_of_officer_draft = df.known_past_shootings_of_officer_draft.replace('None', '0').replace('No', '0')

        # cleaned mental illness, fix unknown values and drug and alcohol values
        df.mental_illness = df.mental_illness.replace('unkown', 'unknown').replace('yes/drug or alcohol use','drug or alcohol use').replace('unknown ','unknown')
        mentalillness_dummies = pd.get_dummies(df.mental_illness, prefix="mntlill")

        # grouping encounter type 
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('part 1 violent crime'), "part 1 violent crime", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('domestic distu'), "domestic disturbance", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('person with '), "person with a weapon", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('traffic'), "traffic stop", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('other'), "other", df.encounter_type_draft)
        
        # cause of death grouping
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('gunshot'), "gunshot", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('taser'), "taser", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('asphyxiated'), "physical restraint", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('pepper spray'), "pepper spray", df.cause_of_death)

        # initial_reported_reason_for_encounter_draft grouping
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('traffic'), "traffic violation", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('domestic distu'), "domestic disturbance", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('warrant'), "warrant", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('assault'), "assault", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('domestic'), "domestic disturbance", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('shooting'), "shooting", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('public intox'), "public intoxication", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('suspicious'), "suspicious behavior", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('shoot'), "shooting", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('mental ill'), "mental illness", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('theft'), "theft", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('shots'), "shooting", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('911 hang'), "911 hang up call", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('murder'), "murder", df.initial_reported_reason_for_encounter_draft)
        df.initial_reported_reason_for_encounter_draft = np.where(df['initial_reported_reason_for_encounter_draft'].str.contains('burglary'), "burglary", df.initial_reported_reason_for_encounter_draft)

        # encounter_type_draft dummy variables
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('none'), "other", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('part 1'), "violent crime_part 1", df.encounter_type_draft)
        df.encounter_type_draft = df.encounter_type_draft.str.replace(' ', '_').str.replace('/', '_')

        # dummies variables created
        encounter_dummies = pd.get_dummies(df.encounter_type_draft, prefix='was').drop(columns='was_other')

        # fleeing or not fleeing
        df.fleeing.fillna('not fleeing')

        # clean gender column
        df['gender'] = np.where(df.gender =="unknown", "male", df.gender)

        # encode gender for ML
        gender_dummies = pd.get_dummies(df.gender, prefix='is')

        # clean race column
        df['race'] = np.where(df['race'].str.contains('asian|pacific islander'), "asian/pacific islander", df.race)
        race_dummies = pd.get_dummies(df.race, prefix='is')

        # drop alleged_threat_lvl 'undetermined' 'none'
        df = df[(df.alleged_threat_lvl != 'undetermined') & (df.alleged_threat_lvl != 'none')]
        df.alleged_threat_lvl = np.where(df.alleged_threat_lvl == "attack", 1, 0)

        # making fleeing - not fleeing dummy variables
        df.fleeing = np.where(df['fleeing'].str.contains('car'), "fleeing", df.fleeing)
        df.fleeing = np.where(df['fleeing'].str.contains('foot'), "fleeing", df.fleeing)
        df.fleeing = np.where(df['fleeing'].str.contains('other'), "not fleeing", df.fleeing)

        # drop is_not fleeing column
        flee_dummies = pd.get_dummies(df.fleeing, prefix='was')
        flee_dummies.drop(columns='was_not fleeing', inplace=True) 

        # armed_unarmed dummy columns
        df.armed_unarmed_status = df.armed_unarmed_status.str.lower().str.strip().str.replace(' ', '_').replace('unarmed/did_not_have_actual_weapon', 'unarmed')
        armed_dummies = pd.get_dummies(df.armed_unarmed_status, prefix='was').drop(columns='was_unclear')

        # clean geography
        df.loc[(df.agency_responsible.str.contains('county')) & (df.geography == "undetermined"), "geography"] = "rural"
        df.loc[(df.geography == "undetermined"), "geography"] = "urban"
        geography_dummies = pd.get_dummies(df.geography)
                
        # concat dummy feats to df
        df = pd.concat([df, gender_dummies, flee_dummies, armed_dummies, encounter_dummies, race_dummies, mentalillness_dummies, geography_dummies], axis=1)

        # cause of death lethal - not lethal
        df['cod_lethal'] = np.where(df.cause_of_death != "gunshot", 0, 1)

        # # set index to (to_datetime)'date'
        # df = df.set_index('date').sort_index()
        # df.index = pd.to_datetime(df.index)

        # drop nulls
        df.dropna(inplace=True)

        # cleaning age
        df.age = df.age.replace('40s', '40')
        df.age = df.age.replace('Unknown', '0')
        df.age = pd.to_numeric(df.age)

        # binning age
        cut_labels_a = ['unknown','under 12','12-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
        cut_bins = [-1, 0, 11, 17, 24, 34, 44, 54, 64, 130]
        df['age_bins'] = pd.cut(df['age'], bins=cut_bins, labels=cut_labels_a)

        # make dummy columns for age range
        age_dummies = pd.get_dummies(df.age_bins, drop_first=False)

        # concat age_dummies
        df = pd.concat([df, age_dummies], axis=1)

        # save doc as csv for ease of use 
        df.to_csv('prepped_data.csv')


    elif cached == True:
        # creates dataframe from cached csv file
        df = pd.read_csv('prepped_data.csv')
        
        


        
    return df


