# financial_yt_sentiment_analyzor-ui
This is a user interface (UI) for the [Financial YouTube Sentiment Analyzor](https://github.com/cdemoll/financial_yt_sentiment_analyzor) project, which uses natural language processing (NLP) techniques to analyze the sentiment of YouTube comments related to finance and investing. The UI allows users to d view the sentiment analysis results in an easy-to-read format from a entire.   

![UI capture](https://i.imgur.com/qapzgfw.png) 

The project is built using Python and the Dash framework, with the sentiment analysis performed using a FinBERT model. The UI is designed with the Dash Bootstrap library providing responsive design.  

## Get a taste of it

An AWS environnement has been setup for you to take a look at the project without having to do anything else then clickign this link:  

**[Access Youtube Financial Sentiment Analyzor UI](http://13.38.250.148/)**
> **_NOTE:_**  Since AWS Free Tier is used for production, uptime is limited to 750hours/month. The website might not be available as the time of reading.

## Configure

> :warning: **Mandatory file not included:** ***secret_keys.py*** should contains all your login fields for MongoDB

## Running the code

To use the Financial YouTube Sentiment Analyzor UI on your local machine, simply clone the repository and run the app.py file. You'll need to setup your own MongoDB cluster,db,collection then dataset.

> :warning: **You will need to setup your own MongoDB cluster prior**
```bash
python app.py
```









This project was created by cdemoll and is available under the AGPL V3 license. Contributions and feedback are welcome! DO NOT HESITATE TO FORK!
