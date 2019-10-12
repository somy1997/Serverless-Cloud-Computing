# Serverless-Cloud-Computing

All the work is manually being logged in Serverless-CLoud-Computing/Weeks.txt

## Sau Paulo

Commit URL : https://github.com/somy1997/Serverless-Cloud-Computing/tree/a8d548d4526481bcceef1430475ff4ce48c866ce

Lambda Function Source files : Serverless-Cloud-Computing/My Analysis/Source  
Statistics Generator Source  : Serverless-Cloud-Computing/My Analysis/Collecting Stats/Stats_Sau_Paulo.ipynb  
Statistics Generator Result  : Serverless-Cloud-Computing/My Analysis/Collecting Stats/  

## Mumbai

After porting the code to dedicated account, regenerated statistics for Mumbai region

Commit URL : https://github.com/somy1997/Serverless-Cloud-Computing/tree/9a30652923bcf8340eb59b708201a10e1b53fa3d

Lambda Function Source files : Serverless-Cloud-Computing/My Analysis/Source  
Statistics Generator Source  : Serverless-Cloud-Computing/My Analysis/Collecting Stats/Mumbai.ipynb  
Statistics Generator Result  : Serverless-Cloud-Computing/My Analysis/Collecting Stats/stats/  

## Checking Global Variables

Checked if the global variables are being shared by multiple lambda calls. The global variables are share between multiple lambda calls sharing same session (when they share the same server instance). For different sessions, the global variables are not shared.

Commit URL : https://github.com/somy1997/Serverless-Cloud-Computing/tree/54d83ab663a8b7b93c04c3a451c915e255ad12f0

Lambda Function Source files : Serverless-Cloud-Computing/My Analysis/Checking Global Lambda

## Single Server Multiple Client

Checked how the billed duration varies with changing location of the client, ideally, the billed duration should only depend on the duration for which the lambda function was run and should not include the latency incurred due to distance between client and the server.  
Used Mumbai for Server location and tested client locations from Mumbai, North California, London, Sidney, Tokyo.

Commit URL : https://github.com/somy1997/Serverless-Cloud-Computing/tree/145401cbd348d4f1bba2fdbb944fb4c3be3f8558

Statistics Generator Source : Serverless-Cloud-Computing/My Analysis/Single Server Multiple Client/  
Statistics Generator Result : Serverless-Cloud-Computing/My Analysis/Single Server Multiple Client/statsServerMumbai/
