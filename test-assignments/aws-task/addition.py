import json

'''
Reference:-> https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html

Input on AWS Lambda console:
{
    "num1": 10,
    "num2": 20
}
'''

def lambda_handler(event, context):
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')
        if num1 is None or num2 is None:
            raise ValueError("Missing required parameters: 'num1' and 'num2'")
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
