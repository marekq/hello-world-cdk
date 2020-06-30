from aws_cdk import (
    core, 
    aws_lambda,
    aws_apigateway
)

class HelloWorldCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create a lambda function
        lambdafunc = aws_lambda.Function(self, "lambda",
            runtime = aws_lambda.Runtime.PYTHON_3_8,
            code = aws_lambda.Code.from_asset("./lambda"),
            handler = "lambda.lambda_handler",
            timeout = core.Duration.seconds(3),
            memory_size = 128,
            retry_attempts = 0,
            tracing = aws_lambda.Tracing.ACTIVE
        )

        # create an api gateway
        apigw = aws_apigateway.LambdaRestApi(self, 'RestApi', handler=lambdafunc)
