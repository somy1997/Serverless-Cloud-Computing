// // Boilerplate code

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
    console.log(event.EmailID)
    
    var params = 
    {
        TableName : tableName,
        Key:
        {
            "EmailID" : event.EmailID
        }
    }
    
    var start = new Date().getTime();
    docClient.get(params, function(err,data)
    {
        var end = new Date().getTime();
        var time = end - start;
        callback(err, data + time);
    })
};

// Code for POST calls

// var AWS = require('aws-sdk');

// var docClient = new AWS.DynamoDB.DocumentClient();

// exports.handler = (event, context, callback) => 
// {
//     var tableName = "CustomerDetails";
    
//     var params = 
//     {
//         TableName : tableName,
//         Key:
//         {
//             "EmailID" : event.EmailID,
//             "FirstName" : event.FirstName,
//             "LastName" : event.LastName
//         }
//     }
    
//     var start = new Date().getTime();
    
//     docClient.put(params, function(err,data)
//     {
//         if(err) 
//         {
//             callback(err)
//         }
//         else
//         {
//             var end = new Date().getTime();
//             var time = end - start;
//             callback(err, data + time);    
//         }
//     })
// };