****************************************
Twitter Keyphrase-Search  
****************************************
A simple website that allows users to enter a short search-string of words, and then receive a rundown of 
key phrases from popular, related tweets. 

The analysis takes between 5-10 minutes, and results are sent to the user's provided email. 

Motivation
#############
This is a learning/showcase project for building a serverless application on AWS in general, 
and in particular experimenting with the various offerings for NLP (Natural Language Processing). 

An early version of this application was aimed at topic modelling and sentiment analysis, but
these turned out to require a much greater volume of data and take much longer to process by Comprehend. 
To make the showcase more responsive and less demanding on my wallet, I then shifted to simple key phrases.

This is an entirely serverless architecture aside from Redshift, which needs to be 
provisioned. As the application is currently, Redshift doesn't in fact do much. I still decided to  
include it, in case I want to add some features to the data and do more proper 
analysis/visualization in the future.

Getting Started
#################

Cloudformation

Tech used
#############

**Built with**

* AWS S3 (website hosting)
* AWS API Gateway (DNS & directing requests to lambda)
* AWS Lambda (runtime for python)
* AWS Comprehend (key phrase -detection)
* Amazon DynamoDB (metadata from searches)
* Amazon Redshift (keyphrase data)

License
#############
MIT © 2020 Johannes Jolkkonen

