var globalcount = 0

exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    globalcount++;
    console.log(globalcount.toString());
    return response;
};
