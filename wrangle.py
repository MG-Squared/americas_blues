import pandas as pd 
import numpy as np 



def wrangle_data(cached=False):
    '''
    Description:
    -----------
    This function acquires and preps the police killings dataset
    for exploration and modeling.
    '''
    if cached == False:
        # convert excel file to pandas dataframe
        df = pd.read_excel('data.xlsx')
        # drop unamed columns
        df.drop(columns=(list(df.columns[35:])), inplace=True)
        # Rename columns 
        columns = [
                    "name", "age", "gender", "race", 'img_url', 'date', 'address', \
                    'city', 'state', 'zipcode', 'county', 'agency_responsible', 'ori_agency_identifier', \
                    'cause_of_death', 'description_of_circumstances', 'official_disposition', 'criminal_charges_filed', \
                    'news_article_or_photo_of_official_document', 'mental_illness', 'armed_unarmed_status', 'alleged_weapon', \
                    'alleged_threat_lvl', 'fleeing', 'body_camera_or_video', 'wapo_id', 'off_duty_killing', 'geography', 'mpv_id', \
                    'fatal_encounters_id', 'encounter_type_draft', 'initial_reported_reason_for_encounter_draft', \
                    'names_of_officers_involved_draft', 'race_of_officers_involved_draft', 'known_past_shootings_of_Officer_draft', \
                    'call_for_service_draft'
                    ]
        df.columns = columns
       
        # list of columns unusable
        dropcols = ['name', 'img_url', 'ori_agency_identifier', 'news_article_or_photo_of_official_document', 'off_duty_killing', 'wapo_id', \
        'mpv_id', 'fatal_encounters_id', 'names_of_officers_involved_draft', 'address']
        # dropcols dropped
        df.drop(columns=dropcols, inplace=True)

        # body cam nulls = no
        df.body_camera_or_video = df.body_camera_or_video.fillna('no').str.lower()
        # body cam others into yes 
        df.body_camera_or_video = np.where(df['body_camera_or_video'].str.lower().str.contains('video'), "yes", df.body_camera_or_video)
        
        # known_past_shootings_of_Officer_draft nulls, none, and no = 0
        df.known_past_shootings_of_Officer_draft = df.known_past_shootings_of_Officer_draft.fillna('0')
        df.known_past_shootings_of_Officer_draft = df.known_past_shootings_of_Officer_draft.replace('None', '0').replace('No', '0')

        # cleaned mental illness, fix unknown values and drug and alcohol values
        df.mental_illness = df.mental_illness.str.lower().replace('unkown', 'unknown').replace('yes/drug or alcohol use','drug or alcohol use').replace('unknown ','unknown')

        # Grouping encounter type 
        df.encounter_type_draft = df.encounter_type_draft.str.lower()
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('part 1 violent crime'), "part 1 violent crime", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('domestic distu'), "domestic disturbance", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('person with '), "person with a weapon", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('traffic'), "traffic stop", df.encounter_type_draft)
        df.encounter_type_draft = np.where(df['encounter_type_draft'].str.contains('other'), "other", df.encounter_type_draft)
        
        # cause of death grouping
        df.cause_of_death = df.cause_of_death.str.lower()
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('gunshot'), "gunshot", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('taser'), "taser", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('asphyxiated'), "physical restraint", df.cause_of_death)
        df.cause_of_death = np.where(df['cause_of_death'].str.contains('pepper spray'), "pepper spray", df.cause_of_death)

        # 

        

        df.to_csv('prepped_data.csv')












    elif cached == True:
        # creates dataframe from cached csv file
        df = pd.read_csv('prepped_data.csv')
        
        


        
    return df


