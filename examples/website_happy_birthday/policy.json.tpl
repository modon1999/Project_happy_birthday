{
    "Version": "2012-10-17",
    "Id": "Policy1647687086912",
    "Statement": [
        {
            "Sid": "Stmt1647687084473",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::${name_bucket}/*"
        }
    ]
}
