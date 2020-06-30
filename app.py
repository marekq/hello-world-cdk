#!/usr/bin/env python3

from aws_cdk import core

from hello_world_cdk.hello_world_cdk_stack import HelloWorldCdkStack


app = core.App()
HelloWorldCdkStack(app, "hello-world-cdk")

app.synth()
