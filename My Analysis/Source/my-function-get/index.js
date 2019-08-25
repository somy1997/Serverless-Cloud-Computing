// Code for GET calls

const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();
var tableName = "CustomerDetails";

exports.handler = (event, context, callback) => 
{
    var useremail;
    
    if(event.queryStringParameters && event.queryStringParameters.EmailID)
    {    
        // Call from URL
        console.log("URL call | ");
        useremail = event.queryStringParameters.EmailID;
    }
    else if(event.EmailID)
    {
        // Call from Lambda Test with EmailID specified
        console.log("Lambda Test call | ");
        useremail = event.EmailID;
    }
    else
    {
        // Call from Lambda Test without specifying EmailID, using default
        console.log("Call without EmailID | ")
        useremail = "janedoe@gmail.com";
    }
        
    // Setting params for DB Call    
    var params = 
    {
        TableName : tableName,
        Key:
        {
            "EmailID" : useremail
        }
    }
    
    // DB CALL 
    var start = Date.now();
    docClient.get(params, function(err,data)
    {
        var end = Date.now();
        var time = end - start;
        var response;
        if(err)
        {
            console.log(err);
            response = 
            {
                statusCode: 200,
                body: err.toString()
            };
        }
        else
        {
            response = 
            {
                statusCode: 200,
                body: JSON.stringify(data)+"$"+time.toString()
            };
        }
        callback(err, response);
    })
    
    // Testing if the function executes even after callback
    //setTimeout(function() {console.log("Logged after timeout of 2 sec | ")}, 2000);
    //setTimeout(function() {console.log("Logged after timeout of 4 sec | ")}, 4000);
};