# police_violence

![readmebanner](https://i.pinimg.com/originals/80/0d/58/800d58c4377ac582c1174125dd83a4f4.png)

___

<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___
<a name="project-summary"></a><h1><img src="https://i.pinimg.com/originals/ae/b4/8f/aeb48f8665be081c8b679ae4314e7baf.png"></h1>



Using Pandas, Mathplotlib, and SciKit-Learn in Jupyter Lab, I prepped and explored strings of text scraped from Google's Github Repositories to create a model that predicted the primary coding language used in that repository. This predictive model out performed the baseline model by 28%.




<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/53/55/a5/5355a5558620d09f795dc54d0a267eae.png"></h1>
### Goal: 
The goal for this project is to create a model that will accurately predict the primary coding language of a Github Repository given text from a `README`.

### Initial Hypotheses:

> Hypothesis₁
>
> There is a relationship between mention of programming language in `README` and primary coding language used.
    
> Hypothesis₂
>
> `README` text length does **not** affect the programming language.

    
### Project Planning Initial Thoughts:
**First iteration:**
I'd like my first iteration to include a second feature of `README` length. 

**Second iteration:**
I'd like to use takeaways from my exploration to create another useful feature.

**Deliverables:**
- Final clean, interactive Py notebook.
- Presentation Slide Deck

    
    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/87/b7/5b/87b75b1da8b762d85d5137f7412f9bc4.png"/></h1>

## Exploration Key Findings:
- `Python` is the primary language of the most of amount of repos.
    - Followed by:
        - `C++`
        - `Go`
        - `Java`
        - `Javascript`
        
- Mean word count of Google Repos is 4920.
- Median is 2955
- Min: 10, Max: 142,109

- Long README's language varied
- There are a **lot** of languages to choose from in the Google repos, filtering that down will be essential.


    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/51/f4/89/51f489143dcbaee101c4ea0ed25238c6.png"/></h1>

- Google uses over 30 different languages in their repos, which drove down the accuracy. 

- The top common words used across the languages were verbs.

![languagewordclouds](https://i.pinimg.com/originals/df/43/84/df4384afbfa3a415c47abecb7ba1b6bf.png)


[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/a0/0a/4a/a00a4acc51f1e0f3007df0011b836917.png"/></h1>

| column_name     | description                                                           | key                          | dtype  |
|-----------------|-----------------------------------------------------------------------|------------------------------|--------|
| `repo`          | Link suffix in `username`/`repo_name` formatting.                     |                              | object |
| `language`      | Primary coding language used in the repo.                             |                              | object |
| `readme_contents`| String of text scraped from repo's README file.                      |                              | object |
| `readme_length`  | Length of `README` text                                              |                              | int64  |
| `clean_content`  | String of `README` text that has been cleaned by `clean()` function  |                              | object |
| `cleaned_length` | Length of `clean_content` text                                       |                              | int64  |




[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/22/c7/0a/22c70a2c5b466c225205d379180115dd.png"/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the [pre-scraped repo data: `google_readmes1020.csv`](google_readmes1020.csv) located in this [repository](https://github.com/o0amandagomez0o/nlp_project-readme_prediction).
   


**Prep your repo.**

2. Create a new repo to house this project, and clone it into your terminal by copying the SSH link:
    ![prep your repo](https://i.pinimg.com/originals/93/d2/89/93d2890b4712500dbea92ebf9756e71a.png)
> <code>git clone </code> (Cmd+V)
    

3. Create a `.gitignore` that includes any files you dont want shared on the internet and **push it**! 
    
    - (This can include your newly downloaded .csv files)
> <code>code .gitignore</code>



4. Create a `README.md` file to begin notating steps taken so far.
    
><code>code README.md</code>


5. Transfer your .csv file(s) into your newly established folder.


6. Create a Jupyter Lab environment to continue working in.
> <code>jupyter lab</code>


7. Create Jupyter Notebook to begin the data pipeline. 

![jlablauncher](https://i.pinimg.com/originals/98/92/c5/9892c5042934750b5ba073f2d49f6184.png)
    




[Jump to Navigation](#navigation)








































