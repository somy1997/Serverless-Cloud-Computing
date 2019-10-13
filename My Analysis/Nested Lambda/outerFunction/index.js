// Code for outer function

var aws = require('aws-sdk');
     
exports.handler = (event, context, callback) => 
{
    // TODO implement
    //console.log('Outer function called');
    
    var lambda = new aws.Lambda(
    {
        region: 'ap-south-1'
    });    
    
    var params = 
    {
      FunctionName: 'innerFunction', 
      InvocationType: 'RequestResponse',//'Event', 
      LogType: 'Tail', 
      Payload: JSON.stringify('No Parameters')
    };
    
    //console.log('Reached');
    
    var start = Date.now();
    lambda.invoke(params, function(err, data) 
    {
        // if (err) console.log(err, err.stack); // an error occurred
        // else     console.log(data);           // successful response
       
        var end = Date.now();
        var time = end - start;
        console.log(time.toString())
        
        const response = 
        {
            statusCode: 200,
            body: time.toString(),
        };
        
        callback(err,response);
    });
};
