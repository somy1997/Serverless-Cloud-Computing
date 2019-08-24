// exports.handler = async (event) => 
// {
//     // TODO implement
//     const response = 
//     {
//         statusCode: 200,
//         body: JSON.stringify('Hello from Lambda!'),
//     };
//     return response;
// };


// Code for GET calls

const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();

var tableName = "CustomerDetails";

exports.handler = (event, context, callback) => 
{
    console.log(event);
    //console.log(event.EmailID);
    //console.log(typeof(event.EmailID))
    
    // if(event.queryStringParameters && event.queryStringParameters.EmailID)
        console.log("Came to if part")
        // console.log(event.queryStringParameters.EmailID)
        var useremail = "";
        if(event.queryStringParameters && event.queryStringParameters.EmailID)
            useremail = event.queryStringParameters.EmailID;
        
        var params = 
        {
            TableName : tableName,
            Key:
            {
                "EmailID" : useremail
            }
        }
        
        
    
        // DB CALL 
        // var start = new Date().getTime();
        docClient.get(params, function(err,data)
        {
        //     // var end = new Date().getTime();
        //     // var time = end - start;
            const response = 
        {
            statusCode: 200,
            body: JSON.stringify(data),
        };
        callback(err, response);
            // callback(err, data);
        //     // if (err) console.log(err);
            // else console.log(data);
        })
    // else
    // {
    //     console.log("Came to else part");
    //     // var useremail = "";
    //     // var samplestring = "This is sample string";
    //     // console.log(typeof(event.queryStringParameters.EmailID));
    //     // if(event.queryStringParameters && event.queryStringParameters.EmailID)
    //     //     useremail = event.queryStringParameters.EmailID;
    //     const response = 
    //     {
    //         statusCode: 200,
    //         body: JSON.stringify('This is else part'),
    //     };
    //     callback(null, response);
    //     console.log("This is after callback")
    // }
};