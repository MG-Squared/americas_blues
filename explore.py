import pandas as pd
import numpy as np

# Visualizations
import seaborn as sns
import matplotlib.pyplot as plt

# Hypothesis tests
from scipy import stats
from scipy.stats import chi2_contingency
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind

#Feature Engineering
from sklearn.feature_selection import SelectKBest, f_regression, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from scipy import stats

# Split data
from sklearn.model_selection import train_test_split

# Evaluate models
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support 

# Create models for classification ML:
# Decision Tree  
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# Random Forest
from sklearn.ensemble import RandomForestClassifier

# K-Nearest Neighbor(KNN)  
from sklearn.neighbors import KNeighborsClassifier

# Logistic Regression
from sklearn.linear_model import LogisticRegression





##########################################################################################

# Zero's and NULLs

##########################################################################################



#----------------------------------------------------------------------------------------#
###### Identifying Zeros and Nulls in columns and rows


def missing_zero_values_table(df):
    '''
    
    Description:
    -----------
    This function takes in a dataframe and counts number of Zero values and NULL values. Returns a Table with counts and percentages of each value type.
    
    Parameters:
    ----------
    df: Dataframe
    
    '''
    zero_val = (df == 0.00).astype(int).sum(axis=0)
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mz_table = pd.concat([zero_val, mis_val, mis_val_percent], axis=1)
    mz_table = mz_table.rename(
    columns = {0 : 'Zero Values', 1 : 'NULL Values', 2 : '% of Total NULL Values'})
    mz_table['Total Zero\'s plus NULL Values'] = mz_table['Zero Values'] + mz_table['NULL Values']
    mz_table['% Total Zero\'s plus NULL Values'] = 100 * mz_table['Total Zero\'s plus NULL Values'] / len(df)
    mz_table['Data Type'] = df.dtypes
    mz_table = mz_table[
        mz_table.iloc[:,1] >= 0].sort_values(
    '% of Total NULL Values', ascending=False).round(1)
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
        "There are " + str((mz_table['NULL Values'] != 0).sum()) +
          " columns that have NULL values.")
    #       mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
    return mz_table



def missing_columns(df):
    '''
    
    Description:
    -----------
    This function takes a dataframe, counts the number of null values in each row, and converts the information into another dataframe. Adds percent of total columns.
    
    Parameters:
    ----------
    df: Dataframe
    
    '''
    missing_cols_df = pd.Series(data=df.isnull().sum(axis = 1).value_counts().sort_index(ascending=False))
    missing_cols_df = pd.DataFrame(missing_cols_df)
    missing_cols_df = missing_cols_df.reset_index()
    missing_cols_df.columns = ['total_missing_cols','num_rows']
    missing_cols_df['percent_cols_missing'] = round(100 * missing_cols_df.total_missing_cols / df.shape[1], 2)
    missing_cols_df['percent_rows_affected'] = round(100 * missing_cols_df.num_rows / df.shape[0], 2)
    
    return missing_cols_df


#----------------------------------------------------------------------------------------#
###### Do things to the above zeros and nulls ^^

def handle_missing_values(df, drop_col_proportion, drop_row_proportion):
    '''
    
    Description:
    -----------
    This function takes in a dataframe and returns a dataframe with columns and rows that fit the input criteria removed.
    
    Parameters:
    ---------
    df: Dataframe
    drop_col_proportion: float
        a number between 0 and 1 that represents the proportion, for each column, of rows with non-missing values required to keep the column, 
    drop_row_proportion: float
        a number between 0 and 1 that represents the proportion, for each row, of columns/variables with non-missing values required to keep the row, and returns the dataframe with the columns and rows dropped as indicated.
        
    '''
    # drop cols > thresh, axis = 1 == cols
    df = df.dropna(axis=1, thresh = drop_col_proportion * df.shape[0])
    # drop rows > thresh, axis = 0 == rows
    df = df.dropna(axis=0, thresh = drop_row_proportion * df.shape[1])
    return df



##########################################################################################

# Split - train, validate, test

##########################################################################################



#function to split data
def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test







##########################################################################################

# Visualiation Exploration

##########################################################################################



###################### ________________________________________
### Univariate

def explore_univariate(train, categorical_vars, quant_vars):
    '''
    
    Description:
    -----------
    Takes in a dataframe and a categorical variable and returns a frequency table and barplot of the frequencies, for a given categorical variable, compute the frequency count and percent split and return a dataframe of those values along with the different classes, and takes in a dataframequantitative variable and returns descriptive stats table, histogram, and boxplot of the distributions
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    categorical_vars: list containing strings
        List of categorical variables within the train dataframe
    quant_vars: list containing strings
        List of quantitative variables within the train dataframe
        
    '''
    for cat_var in categorical_vars:
        explore_univariate_categorical(train, cat_var)
        print('_________________________________________________________________')
    for quant in quant_vars:
        p, descriptive_stats = explore_univariate_quant(train, quant)
        plt.show(p)
        print(descriptive_stats)

def explore_univariate_categorical(train, cat_var):
    '''
    
    Description:
    -----------
    Takes in a dataframe and a categorical variable and returns
    a frequency table and barplot of the frequencies. 
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    cat_var: str
        A categorical variable within the train dataframe

    '''
    frequency_table = freq_table(train, cat_var)
    plt.figure(figsize=(16,6))
    sns.barplot(x=cat_var, y='Count', data=frequency_table, color='lightseagreen')
    plt.title(cat_var)
    plt.xticks(rotation = 90)
    plt.show()
    print(frequency_table)

def explore_univariate_quant(train, quant):
    '''
    
    Description:
    -----------
    Takes in a dataframe and a quantitative variable and returns
    descriptive stats table, histogram, and boxplot of the distributions. 
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    quant: str
        A quantitative variable within the train dataframe
        
    '''
    descriptive_stats = train[quant].describe()
    plt.figure(figsize=(8,2))

    p = plt.subplot(1, 2, 1)
    p = plt.hist(train[quant], color='lightseagreen')
    p = plt.title(quant)

    # second plot: box plot
    p = plt.subplot(1, 2, 2)
    p = plt.boxplot(train[quant])
    p = plt.title(quant)
    return p, descriptive_stats
    
def freq_table(train, cat_var):
    '''
    
    Description:
    -----------
    For a given categorical variable, compute the frequency count and percent split
    and return a dataframe of those values along with the different classes. 
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    cat_var: str
        A categorical variable within the train dataframe
        
    '''
    class_labels = list(train[cat_var].unique())

    frequency_table = (
        pd.DataFrame({cat_var: class_labels,
                      'Count': train[cat_var].value_counts(normalize=False), 
                      'Percent': round(train[cat_var].value_counts(normalize=True)*100,2)}
                    )
    )
    return frequency_table

###################### ________________________________________
#### Bivariate


def explore_bivariate(train, categorical_target, continuous_target, binary_vars, quant_vars):
    '''
    
    Description:
    -----------
    This function makes use of explore_bivariate_categorical and explore_bivariate_quant functions. 
    Each of those take in a continuous target and a binned/cut version of the target to have a categorical target. 
    the categorical function takes in a binary independent variable and the quant function takes in a quantitative 
    independent variable. 
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    categorical_target: str
        The categorical target 
    continuous_target: str
        The continuous target
    binary_vars: list containing strings
        List of binary variables within the train dataframe
    quant_vars: list containing strings
        List of quantitative variables within the train dataframe
    
    '''
    for binary in binary_vars:
        explore_bivariate_categorical(train, categorical_target, continuous_target, binary)
    for quant in quant_vars:
        explore_bivariate_quant(train, categorical_target, continuous_target, quant)

###################### ________________________________________
## Bivariate Categorical

def explore_bivariate_categorical(train, categorical_target, continuous_target, binary):
    '''
    
    Description:
    -----------
    Takes in binary categorical variable and binned/categorical target variable, 
    returns a crosstab of frequencies
    runs a chi-square test for the proportions
    and creates a barplot, adding a horizontal line of the overall rate of the binary categorical variable. 
    
    Parameters:
    ----------
    train: Dataframe
        Dataframe used to train models 
    categorical_target: str
        The categorical target 
    continuous_target: str
        The continuous target
    binary: str
        A binary variable within the train dataframe
    
    '''
    print(binary, "\n_____________________\n")
    
    ct = pd.crosstab(train[binary], train[categorical_target], margins=True)
    chi2_summary, observed, expected = run_chi2(train, binary, categorical_target)
    mannwhitney = compare_means(train, continuous_target, binary, alt_hyp='two-sided')
    p = plot_cat_by_target(train, categorical_target, binary)
    
    print("\nMann Whitney Test Comparing Means: ", mannwhitney)
    print(chi2_summary)
#     print("\nobserved:\n", ct)
    print("\nexpected:\n", expected)
    plt.show(p)
    print("\n_____________________\n")
    

    
def run_chi2(train, binary, categorical_target):
    observed = pd.crosstab(train[binary], train[categorical_target])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    chi2_summary = pd.DataFrame({'chi2': [chi2], 'p-value': [p], 
                                 'degrees of freedom': [degf]})
    expected = pd.DataFrame(expected)
    return chi2_summary, observed, expected


def plot_cat_by_target(train, categorical_target, binary):
    p = plt.figure(figsize=(2,2))
    p = sns.barplot(categorical_target, binary, data=train, alpha=.8, color='lightseagreen')
    overall_rate = train[binary].mean()
    p = plt.axhline(overall_rate, ls='--', color='gray')
    return p

    
def compare_means(train, continuous_target, binary, alt_hyp='two-sided'):
    x = train[train[binary]==0][continuous_target]
    y = train[train[binary]==1][continuous_target]
    return stats.mannwhitneyu(x, y, use_continuity=True, alternative=alt_hyp)

###################### ________________________________________
## Bivariate Quant

def explore_bivariate_quant(train, categorical_target, continuous_target, quant):
    '''
    descriptive stats by each target class. 
    compare means across 2 target groups 
    boxenplot of target x quant
    swarmplot of target x quant
    '''
    print(quant, "\n____________________\n")
    descriptive_stats = train.groupby(categorical_target)[quant].describe().T
    spearmans = compare_relationship(train, continuous_target, quant)
    plt.figure(figsize=(4,4))
    boxen = plot_boxen(train, categorical_target, quant)
#     swarm = plot_swarm(train, categorical_target, quant)
    plt.show()
    scatter = plot_scatter(train, categorical_target, continuous_target, quant)
    plt.show()
    print(descriptive_stats, "\n")
    print("\nSpearman's Correlation Test:\n", spearmans)
    print("\n____________________\n")


def compare_relationship(train, continuous_target, quant):
    return stats.spearmanr(train[quant], train[continuous_target], axis=0)

def plot_swarm(train, categorical_target, quant):
    average = train[quant].mean()
    p = sns.swarmplot(data=train, x=categorical_target, y=quant, color='lightgray')
    p = plt.title(quant)
    p = plt.axhline(average, ls='--', color='black')
    return p

def plot_boxen(train, categorical_target, quant):
    average = train[quant].mean()
    p = sns.boxenplot(data=train, x=categorical_target, y=quant, color='lightseagreen')
    p = plt.title(quant)
    p = plt.axhline(average, ls='--', color='black')
    return p

def plot_scatter(train, categorical_target, continuous_target, quant):
    p = sns.scatterplot(x=quant, y=continuous_target, hue=categorical_target, data=train)
    p = plt.title(quant)
    return p


def get_object_cols(df):
    '''

    Description:
    -----------
    This function takes in a dataframe and identifies the columns that are object types
    and returns a list of those column names. 
    
    Parameters:
    ----------
    df: Dataframe
    
    '''
    # create a mask of columns whether they are object type or not
    mask = np.array(df.dtypes == "object")
        
    # get a list of the column names that are objects (from the mask)
    object_cols = df.iloc[:, mask].columns.tolist()
    
    return object_cols



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats
import datetime as dt



##########################################################################################

# Stats

##########################################################################################



def run_stats_on_everything(train, categorical_target, continuous_target, binary_vars, quant_vars):
    '''
    
    Description:
    -----------
    This function takes in the train dataframe and the segregated columns and runs statistical tests based on the variable type.
    
    Parameters:
    ----------
    train: df
        train dataframe
    categorical_target: str
        String of the categorical target variable
    continuous_target: str
        String of the continuous target variable
    binary_vars: str or list of str
        String or list of variable that are binary
    quant_vars: str or list
        String or list of variables that are continuous
    
    '''
    
    # Cycles through binary variables creates a crosstab, runs a chi2 test and a manwhitney
    for binary in binary_vars:
        
        ct = pd.crosstab(train[binary], train[categorical_target], margins=True)
        chi2_summary, observed, expected = run_chi2(train, binary, categorical_target)
        mannwhitney = compare_means(train, continuous_target, binary, alt_hyp='two-sided')
        
        # prints results 
        print(binary, "\n_____________________\n")
        print("\nMann Whitney Test Comparing Means: ", mannwhitney)
        print(chi2_summary)
    #     print("\nobserved:\n", ct)
        print("\nexpected:\n", expected)
        print("\n_____________________\n")
    
    
    plt.figure(figsize=(16,12))
    sns.heatmap(train.corr(), cmap='BuGn')
    plt.show()
    
    # Cycles through quantitative variables runs spearmans correlation against continuous targets
    for quant in quant_vars:

        spearmans = compare_relationship(train, continuous_target, quant)
        
        # Prints results
        print(quant, "\n____________________\n")
        print("Spearman's Correlation Test:\n")
        print(spearmans)
        print("\n____________________")
        print("____________________\n")

        

        
def t_test(population_1, population_2, alpha=0.05, sample=1, tail=2, tail_dir='higher'):
    '''
    
    Description:
    -----------
    This function takes in 2 populations, and an alpha confidence level and outputs the results of a t-test.
    
    Parameters:
    ----------
    population_1: Series
        A series that is a subgroup of the total population. 
    population_2: Series
        When sample = 1, population_2 must be a series that is the total population; 
        When sample = 2,  population_2 can be another subgroup of the same population
    alpha: float
        Default = 0.05, 0 < alpha < 1, Alpha value = 1 - confidence level 
    sample: {1 or 2}, 
        Default = 1, functions performs 1 or 2 sample t-test.
    tail: {1 or 2}, 
        Default = 2, Need to be used in conjuction with tail_dir. performs a 1 or 2 sample t-test. 
    tail_dir: {'higher' or 'lower'}, 
        default = 'higher'
        
    '''
    
    # One sample, two tail T-test
    if sample == 1 and tail == 2:
        
        # run stats.ttest_1samp
        t, p = stats.ttest_1samp(population_1, population_2.mean())
        
        # prints t-statistic and p value of test
        print(f't-stat = {round(t,4)}')
        print(f'p     = {round(p,4)}\n')
        
        # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value
        if p < alpha:
            print(f'Because the p-value: {round(p, 4)} is less than the alpha: {alpha}, we can reject the null hypothesis')
        else:
            print('There is insufficient evidence to reject the null hypothesis')
    
    # One sample, one tail T-test
    elif sample==1 and tail == 1:
        
        # run stats.ttest_1samp
        t, p = stats.ttest_1samp(population_1, population_2.mean())
        
        # prints t-statistic and p value of test
        print(f't-stat = {round(t,4)}')
        print(f'p     = {round(p,4)}\n')
        
        # sets the direction to check the if population_1 is greater than the total population
        if tail_dir == "higher":
            
            # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value and the t-statistic
            if (p/2) < alpha and t > 0:
                print(f'Because the p-value: {round(p, 4)} is less than the alpha: {alpha}, and the t-stat: {round(t,4)} is greater than 0, we can reject the null hypothesis')
            else:
                print('There is insufficient evidence to reject the null hypothesis')
        
        # sets the direction to check the if population_1 is lower than the total population
        elif tail_dir == "lower":
            
            # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value and the t-statistic
            if (p/2) < alpha and t < 0:
                print(f'Because the p-value: {round(p, 4)} is less than the alpha: {alpha}, and the t-stat: {round(t,4)} is less than 0, we can reject the null hypothesis')
            else:
                print('There is insufficient evidence to reject the null hypothesis')
    
    # Two sample, Two tailed T-test
    elif sample==2 and tail == 2:
        
        # run stats.ttest_ind on two subgroups of the total population
        t, p = stats.ttest_ind(population_1, population_2)
    
        # prints t-statistic and p value of test
        print(f't-stat = {round(t,4)}')
        print(f'p     = {round(p,4)}\n')
        
        # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value
        if p < alpha:
            print(f'Because the p-value: {round(p, 4)} is less than the alpha: {alpha}, we reject the null hypothesis')
        else:
            print('There is insufficient evidence to reject the null hypothesis')
    
    # Two sample, One tailed T-test
    elif sample == 2 and tail == 1:
        
        # run stats.ttest_ind on two subgroups of the total population
        t, p = stats.ttest_ind(population_1, population_2)
        
        # prints t-statistic and p value of test
        print(f't-stat = {round(t,4)}')
        print(f'p     = {round(p,4)}\n')
        
        # sets the direction to check the if population_1 is greater than population_2
        if tail_dir == "higher":
            
            # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value and the t-statistic
            if (p/2) < alpha and t > 0:
                print(f'Because the p-value: {round(p, 4)} is less than alpha: {alpha}, and t-stat: {round(t,4)} is greater than 0, we reject the null hypothesis')
            else:
                print('There is insufficient evidence to reject the null hypothesis')
        
        # sets the direction to check the if population_1 is lower than population_2
        elif tail_dir == "lower":
            
            # runs check if the test rejects the null hypothesis or failed to reject the null hypothesis based on the alpha value and the t-statistic
            if (p/2) < alpha and t < 0:
                print(f'Because the p-value: {round(p, 4)} is less than alpha: {alpha} and the t-stat: {round(t,4)} is less than 0, we reject the null hypothesis')
            else:
                print('There is insufficient evidence to reject the null hypothesis')
    
    # Prints instructions to fix parameters
    else:
        print('sample must be 1 or 2, tail must be 1 or 2, tail_dir must be "higher" or "lower"')
    



def chi2_matts(df, var, target, alpha=0.05):
    '''
    Description:
    -----------
    This function takes in a df, variable, a target variable, and the alpha, and runs a chi squared test. Statistical analysis is printed in the output.
    
    Parameters;
    ---------
    df: Dataframe
    var: str
       Categorical variable to be compared to the target variable
    target: str
        Target categorical variable
    alpha: float
        Default = 0.05, 0 < alpha < 1, Alpha value = 1 - confidence level
        
    '''
    # creates a crosstab of the data
    observed = pd.crosstab(df[var], df[target])
    
    # runs a chi_squared test and returns chi_squared stat, p-value, degrees of freedom, and explected values.
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # Prints the data above
    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}\n')
    
    # Tests whether the chi_squared test rejects the null hypothesis or not. 
    if p < alpha:
        print(f'Because the p-value: {round(p, 4)} is less than alpha: {alpha}, we can reject the null hypothesis')
    else:
        print('There is insufficient evidence to reject the null hypothesis')
    



#################################################################################

# Feature Selection

#################################################################################





def select_kbest(X, y, n):
    '''
    Description:
    -----------
    SelectKbest selects features according to the k highest scores.

    Parameters:
    ----------
    x: df
        Uses the X_train dataframe
    y: series
        The series of the target variable, (y_train) 
    k = int
        The number of features to return for modeling
    '''
    # parameters: f_regression stats test
    f_selector = SelectKBest(chi2, k=n)
    # find the top 2 X-feats correlated with y
    f_selector.fit(X, y)
    # boolean mask of whether the column was selected or not. 
    feature_mask = f_selector.get_support()
    # get list of top K features. 
    f_feature = X.iloc[:,feature_mask].columns.tolist()
    return f_feature

    
def rfe(X, y, n):
    '''
    Description:
    -----------
    Feature ranking with recursive feature elimination..

    Parameters:
    ----------
    x: df
        Uses the X_train dataframe
    y: series
        The series of the target variable, (y_train) 
    k = int
        The number of features to return for modeling
    '''
    # initialize the ML algorithm
    lm = LogisticRegression()
    # create the rfe object, indicating the ML object (lm) and the number of features I want to end up with. 
    rfe = RFE(lm, n)
    # fit the data using RFE
    rfe.fit(X,y)  
    # get the mask of the columns selected
    feature_mask = rfe.support_
    # get list of the column names. 
    rfe_feature = X.iloc[:,feature_mask].columns.tolist()
    return rfe_feature
 





#################################################################################

# Natural Language Processing (NLP) Functions

#################################################################################


import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd




#################################################################################

# Prepare NLP Basic Functions

#################################################################################



def basic_clean(string):
    '''
    Description:
    -----------
    This functiong takes a string and normalizes it by:
        making all text lowercase,
        removing special characters,
        removing characters that are not alphanumeric, whitespace, or a single quote, and
        removing the new line indicator.
    
    Parameters:
    string: str
        String to be normalized.
        
    Example:
    Use in list comprehension with a pandas series
        list_of_strings = ([basic_clean(string) for string in pd.Series])
    '''
    # lowercase all text
    string = string.lower()
    # normalize text by removing special characters 
    string = unicodedata.normalize('NFKD', string)\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')
    # replace anything that is not a letter, number, whitespace or a single quote. 
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    # remove '\n' from string
    # string = string.replace('\n', '')
    
    return string




def tokenize(string):
    '''
    Description:
    -----------
    This functiong tokenizes a string.
    
    Parameters:
    string: str
        String to be tokenized.
        
    Example:
    Use in list comprehension with a pandas series
        list_of_strings = ([tokenize(string) for string in pd.Series])    
    '''
    
    # Create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()

    # Use the tokenizer
    string = tokenizer.tokenize(string, return_str = True)
    
    return string



def stem(string):
    '''
    Description:
    -----------
    This function stems a string.
    
    Parameters:
    ----------
    string: str
        String to be stemmed.
        
    Example:
    -------
    Use in list comprehension with a pandas series
        list_of_strings = ([stem(string) for string in pd.Series]) 
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Apply the stemmer to each word in our string
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again
    stemmed_string = ' '.join(stems)
    
    return stemmed_string
    


def lemmatize(string):
    '''
    Description:
    -----------
    This function stems a string.
    
    Parameters:
    ----------
    string: str
        String to be lemmatized.
        
    Example:
    -------
    Use in list comprehension with a pandas series
        list_of_strings = ([lemmatize(string) for string in pd.Series]) 
    '''
    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again; assign to a variable to save changes.
    lemmatized_string = ' '.join(lemmas)
    
    return lemmatized_string




def remove_stopwords(string, extra_words=None, exclude_words=None):
    '''
    Description:
    -----------
    This function removes stopwrods from a string.
    
    Parameters:
    ----------
    string: str
        String to have stopwords removed.
    extra_words: str or list
        default=None, list of words that you would like to be added to the stopwords list
    exclude_words: str or list 
        default=None, list of words that you would like to remove from the stopwords list
 
    '''
    # creates a list of stopwords
    stopword_list = stopwords.words('english')
    # splits the string into a list of words
    words = string.split()
    
    
    # if extra_words is set to None don't change anything
    if extra_words == None:
        stopword_list = stopword_list
    # if extra_words is a list, append the individual words in the list
    elif type(extra_words) == list:
        for word in extra_words:
            stopword_list.append(word)
    # if extra_words is a string, append the individual word
    elif type(extra_words) == str:
        stopword_list.append(extra_words)
    # somethings wrong text
    else:
        print('extra_words should be a string or a list')
    
    
    # if exclude_words is set to None don't change anything
    if exclude_words == None:
        stopword_list = stopword_list
    # if exclude_words is a list, append the individual words in the list
    elif type(exclude_words) == list:
        for word in exclude_words:
            stopword_list.remove(word)
    # if exclude_words is a string, append the individual word
    elif type(extra_words) == str:
        stopword_list.remove(exclude_words)
    # something's wrong text
    else:
        print('exclude_words should be a string or list')

        
    # filters out stopwords from string
    filtered_words = [word for word in words if word not in stopword_list]
    # rejoins the string 
    string_without_stopwords = ' '.join(filtered_words)
    
    
    return string_without_stopwords




#################################################################################

# Prepare NLP Compund Functions

#################################################################################



def clean_stem_stop(string):
    '''
    Desciption:
    ----------
    This is a one stop function that takes a string and does the following:
    cleans: 
        normalizes it by:
        making all text lowercase,
        removing special characters,
        removing characters that are not alphanumeric, whitespace, or a single quote, and
        removing the new line indicator.
    tokenizes, 
    stems, and 
    removes stopwords. 
    '''
    return remove_stopwords(stem(tokenize(basic_clean(string))))


def clean_lem_stop(string):
    '''
    Desciption:
    ----------
    This is a one stop function that takes a string and does the following:
    cleans: 
        normalizes it by:
        making all text lowercase,
        removing special characters,
        removing characters that are not alphanumeric, whitespace, or a single quote, and
        removing the new line indicator.
    tokenizes, 
    lemmatizes, and 
    removes stopwords. 
    '''
    return remove_stopwords(lemmatize(tokenize(basic_clean(string))))


def clean_and_toke(string):
    '''
    Desciption:
    ----------
    This is a one stop function that takes a string and does the following:
    cleans: 
        normalizes it by:
        making all text lowercase,
        removing special characters,
        removing characters that are not alphanumeric, whitespace, or a single quote, and
        removing the new line '\n' indicator
    and tokenizes. 
    '''
    return tokenize(basic_clean(string))




ADDITIONAL_STOPWORDS = ['r', 'u', '2', 'ltgt']

def ryans_clean(text):
    'A simple function to cleanup text data'
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
    text = (unicodedata.normalize('NFKD', text)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', text).split()
    return ' '.join([wnl.lemmatize(word) for word in words if word not in stopwords])