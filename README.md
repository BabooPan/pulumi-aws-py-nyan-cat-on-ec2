# Welcome to pulumi-aws-py-nyan-cat-on-ec2

This is a nyan-cat page stored in EC2 Instance writen in Python development with [Pulumi](https://www.pulumi.com/).

## Steps

Launch a `virtualenv` for this project. We’ll need to activate it to install dependencies:

```bash
# Activate the virtual environment
$ venv env
$ source venv/bin/activate
# Install the packages
$ pip install -r requirements.txt
...
...
Successfully installed ...
```

Deploy with `pulumi up`, and hold the seconds, the endpoint of website would print out.

```bash
# Get the stack info, the stack name for this is `dev`
$ pulumi preview
Previewing update (dev) # the stack name

View Live: https://app.pulumi.com/xxx/pulumi-aws-py-nyan-cat-on-ec2/dev/previews/STACK_ID

     Type                      Name                               Plan       
 +   pulumi:pulumi:Stack       pulumi-aws-py-nyan-cat-on-ec2-dev  create     
 +   ├─ aws:ec2:SecurityGroup  sg                                 create     
 +   └─ aws:ec2:Instance       nyan-server                        create     
 
Resources:
    + 3 to create
# Deploy the stack
$ pulumi up
Previewing update (dev)

     Type                      Name                               Plan       
 +   pulumi:pulumi:Stack       pulumi-aws-py-nyan-cat-on-ec2-dev  create     
 +   ├─ aws:ec2:SecurityGroup  sg                                 create     
 +   └─ aws:ec2:Instance       nyan-server                        create     
 
Resources:
    + 3 to create
# It would preview first, select `yes` to deploy
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details

Updating (dev)

View Live: https://app.pulumi.com/xxx/pulumi-aws-py-nyan-cat-on-ec2/dev/updates/DEPLOY_VERSION

     Type                      Name                               Status      
 +   pulumi:pulumi:Stack       pulumi-aws-py-nyan-cat-on-ec2-dev  created     
 +   ├─ aws:ec2:SecurityGroup  nyan-server                        created     
 +   └─ aws:ec2:Instance       nyan-server                        created 

# Access the web page with this endpoints
Outputs:
  + publicHostName: "ec2-100-21-18-148.us-west-2.compute.amazonaws.com"
  + publicIp      : "100.21.18.148"

Resources:
    + 3 created

Duration: 37s
```

![nyan-cat](./images/nyan-cat.jpg)

After that, remember to clean up this stack with `pulumi destory` and `pulumi stack rm STACK_NAME`.

## Reference

* web page for nyan-cat [cristurm/nyan-cat](https://github.com/cristurm/nyan-cat)
* [AWS Modernization with Pulumi](https://pulumi.awsworkshop.io/)
