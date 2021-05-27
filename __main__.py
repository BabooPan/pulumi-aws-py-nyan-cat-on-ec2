import pulumi
from pulumi_aws import ec2

# load the pulumi config
config = pulumi.Config()

sg = ec2.SecurityGroup('nyan-server',
    description='security group for web server',
    ingress=[
        # allow ping in
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        # allow ssh in
        {
            "protocol": "tcp",
            "from_port": 22,
            "to_port": 22,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        # allow http in
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
    egress=[
        # allow ec2 communicate with world wide
        {
            "protocol": "-1",
            "from_port": 0,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
    tags={
        "Name": "nyan-server",
    }
)

# Get AMI to provision EC2
ami = ec2.get_ami(
    owners=['amazon'],
    most_recent=True,
    filters=[ec2.GetAmiFilterArgs(
        name='name',
        values=['amzn2-ami-hvm-*-arm64-gp2'],
    )],
)

# Get default VPC
vpc = ec2.get_vpc(default=True)

# Provision EC2 Instance
server = ec2.Instance(
    'nyan-server',
    instance_type="t4g.micro",
    vpc_security_group_ids=[sg.id],
    ami=ami.id,
    user_data="""#!/bin/bash
sudo yum update -y
sudo yum install httpd git -y
git clone https://github.com/BabooPan/nyan-cat
sudo mv nyan-cat/* /var/www/html/
sudo systemctl start httpd &
""",
    tags={
        "Name": "nyan-server",
    },
)

# Export the instance's IP/host
pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
