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
                    'alleged_threat_lvl', 'fleeing', 'body_camera', 'wapo_id', 'off_duty_killing', 'geography', 'mpv_id', \
                    'fatal_encounters_id', 'encounter_type_draft', 'initial_reported_reason_for_encounter_draft', \
                    'names_of_officers_involved_draft', 'race_of_officers_involved_draft', 'known_past_shootings_of_Officer_draft', \
                    'call_for_service_draft'
                    ]
        df.columns = columns

        # Fill in ages and names of records with null values
        #---------------------------------------#
        # Harmony Wolfgram was 41 according to Westword News
        df.loc[313,'age'] = 41
        # Rodolfo Caraballo Moreno was 57 according to his obituary
        df.loc[383,'age'] = 57
        # John Moreno was 32 according to Nogales International
        df.loc[409, 'age'] = 32
        # Tracey Leon McKinney was 41 according to his obituary
        df.loc[525, 'age'] = 41
        # Leicester D.A. Released the name and age of the victim of this incident
        df.loc[1, 'name'] = 'Zachary Richardson'
        df.loc[1, 'age'] = 24
        # Kingman PD released the name and age of 29–year old Kingman resident, Bradley Michael Rose.
        df.loc[53, 'name'] = 'Bradley Michael Rose'
        df.loc[53, 'age'] = 29
        # Steven Verdone was 57
        df.loc[320, 'age'] = 57
        # Amanda Falkner was 48 years old
        df.loc[375, 'age'] = 48
        # Name not released but age is 40-45 will make age 43
        df.loc[516, 'age'] = 43
        #---------------------------------------#

        df.to_csv('prepped_data.csv')

    elif cached == True:
        # creates dataframe from cached csv file
        df = pd.read_csv('prepped_data.csv')
        
        


        
    return df