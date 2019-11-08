// Code for outer function

var aws = require('aws-sdk');
     
exports.handler = (event, context, callback) => 
{
    // TODO implement
    //console.log('Outer function called');
    
    var loca = 'ap-northeast-1';
    var func = 'innerFunction';
    var db = false;
    
    if(event.body)
    {
        console.log("URL call with JSON payload | ");
        var parsedbody = JSON.parse(event.body);
        if(parsedbody.DB)
            db = true;
        if(parsedbody.Location)
            loca = parsedbody.Location;
    }
    else if(event.Location)
    {
        console.log("Lambda Test call | ");
        loca = event.Location;
        if(event.DB)
            db = true;
    }
    else
    {
        console.log("Call without Location | ");
    }
    
    if(db)
        func = 'innerFunctionDB'
    
    // Setting params for Lambda call
    
    var lambda = new aws.Lambda(
    {
        region: loca
    });    
    
    var params = 
    {
      FunctionName: func, 
      InvocationType: 'RequestResponse',//'Event', 
      LogType: 'Tail', 
      Payload: JSON.stringify(event)
    };
    
    //console.log('Reached');
    
    var start = Date.now();
    lambda.invoke(params, function(err, data) 
    {
        // if (err) console.log(err, err.stack); // an error occurred
        // else     console.log(data);           // successful response
       
        var end = Date.now();
        var time = end - start;
        //console.log(time.toString());
        //console.log(data);
        var parsedata = JSON.parse(data.Payload);
        //console.log(parsedata);
        var parsebody = JSON.parse(parsedata.body);
        //console.log(parsebody);
        var response;
        if(db)
        {
            response = 
            {
                statusCode: 200,
                body: time.toString()+"$"+parsebody.toString(),
            };
        }
        else
        {
            response = 
            {
                statusCode: 200,
                body: time.toString(),
            };
        }
        callback(err,response);
    });
};
