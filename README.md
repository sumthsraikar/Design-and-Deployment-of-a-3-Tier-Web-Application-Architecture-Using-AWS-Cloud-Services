# 🧑‍🎓 Student Resume Uploader (AWS 3-Tier App)

This project is a 3-tier serverless web application built using **S3 (Static Website)**, **Lambda**, **API Gateway**, and **DynamoDB**. It allows students to upload their resume in PDF format, along with personal details.

## Technologies Used
- AWS S3 (Static Hosting for Frontend)
- AWS Lambda (Backend logic)
- API Gateway (Routing HTTP requests)
- DynamoDB (Storing student details)
- IAM (Permissions)

## Folder Structure
- `frontend/index.html` — Static HTML form
- `backend/lambda_function.py` — AWS Lambda handler
- `README.md` — Project documentation

## Setup Instructions
1. Deploy `index.html` to an S3 bucket and enable static hosting.
2. Deploy `lambda_function.py` as a Lambda function.
3. Connect it with API Gateway using POST method.
4. Update the API URL in the HTML.
5. Ensure Lambda has permissions for `PutObject` to S3 and `PutItem` to DynamoDB.
