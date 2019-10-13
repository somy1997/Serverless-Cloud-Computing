// Code for inner function
     
exports.handler = async (event) => 
{
    // TODO implement
    console.log('Inner function called');
    
    console.log(event);
    
    const response = 
    {
        statusCode: 200,
        body: JSON.stringify('Hello from Inner Lambda Function!'),
    };
    return response;
};
