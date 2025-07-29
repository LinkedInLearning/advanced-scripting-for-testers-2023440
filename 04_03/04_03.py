import requests

webhook_url = (
    "https://hooks.slack.com/services/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"
)

message = {
    "text": "This is an automated message from my Python script!",
}

response = requests.post(webhook_url, json=message)
