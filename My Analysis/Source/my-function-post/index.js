// Code for POST calls

var AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();

exports.handler = (event, context, callback) => 
{
    var tableName = "CustomerDetails";
    
    var useremail = "johndoe@gmail.com", firstname = "John", lastname = "Doe";
    
    if(event.queryStringParameters && event.queryStringParameters.EmailID)
    {
        console.log("URL call | ");
        useremail = event.queryStringParameters.EmailID;
        if(event.queryStringParameters.FirstName)
            firstname = event.queryStringParameters.FirstName;
        if(event.queryStringParameters.LastName)
            lastname = event.queryStringParameters.LastName;
    }
    else if(event.body)
    {
        console.log("URL call with JSON payload | ");
        var parsedbody = JSON.parse(event.body);
        if(parsedbody.EmailID)
            useremail = parsedbody.EmailID;
        if(parsedbody.FirstName)
            firstname = parsedbody.FirstName;
        if(parsedbody.LastName)
            lastname = parsedbody.LastName;
    }
    else if(event.EmailID)
    {
        console.log("Lambda Test call | ");
        useremail = event.EmailID;
        if(event.FirstName)
            firstname = event.FirstName;
        if(event.LastName)
            lastname = event.LastName;
    }
    else
    {
        console.log("Call without EmailID | ");
    }
    
    // Setting params for DB call
    var params = 
    {
        TableName : tableName,
        Item:
        {
            "EmailID" : useremail,
            "FirstName" : firstname,
            "LastName" : lastname
        }
    }
    
    // DB call
    var start = Date.now();
    docClient.put(params, function(err,data)
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
};