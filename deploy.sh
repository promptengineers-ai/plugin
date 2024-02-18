#!/bin/bash

ENV_FILE=".env"

### Set Environment Variables
set -a # automatically export all variables
source $ENV_FILE
set +a

curl -X POST "https://api.vercel.com/v13/deployments" -H "Authorization: Bearer $VERCEL_TOKEN" -H "Content-Type: application/json" -d '{
  "name": "hello-world-python-vercel",
  "projectSettings": {
    "framework": null,
    "buildCommand": "",
    "outputDirectory": "",
    "installCommand": "pip install -r requirements.txt",
    "devCommand": ""
  },
  "files": [
    {
      "file": "server/api.py",
      "encoding": "base64",
      "data": "ZnJvbSBmYXN0YXBpIGltcG9ydCBGYXN0QVBJCgphcHAgPSBGYXN0QVBJKCkKCkBhcHAuZ2V0KCIvIiwgdGFncz1bIlJvb3QiXSkKYXN5bmMgZGVmIHJlYWRfcm9vdCgpOgogIHJldHVybiB7IAogICAgIm1lc3NhZ2UiOiAiV2VsY29tZSB0byBteSBub3RlcyBhcHBsaWNhdGlvbiwgdXNlIHRoZSAvZG9jcyByb3V0ZSB0byBwcm9jZWVkIgogICB9"
    },
    {
      "file": "main.py",
      "encoding": "base64",
      "data": "aW1wb3J0IHV2aWNvcm4KCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgdXZpY29ybi5ydW4oInNlcnZlci5hcGk6YXBwIiwgaG9zdD0iMC4wLjAuMCIsIHBvcnQ9ODAwMSwgcmVsb2FkPVRydWUp"
    },
    {
      "file": "requirements.txt",
      "encoding": "base64",
      "data": "ZmFzdGFwaQp1dmljb3Ju"
    },
    {
      "file": "vercel.json",
      "encoding": "base64",
      "data": "ewogICAgImJ1aWxkcyI6IFsKICAgICAgeyJzcmMiOiAiL3NlcnZlci9hcGkucHkiLCAidXNlIjogIkB2ZXJjZWwvcHl0aG9uIn0KICAgIF0sCiAgICAicm91dGVzIjogWwogICAgICB7InNyYyI6ICIvKC4qKSIsICJkZXN0IjogInNlcnZlci9hcGkucHkifQogICAgXQp9"
    }
  ],
  "env": [
    {
      "type": "plain",
      "key": "VERCEL_URL",
      "value": "plugin.promptengineers.ai"
    }
  ],
  "alias": ["plugin.promptengineers.ai"]
}' | jq

# curl -X POST "https://api.vercel.com/v9/now/deployments/{deploymentId}/aliases" \
#      -H "Authorization: Bearer $VERCEL_TOKEN" \
#      -H "Content-Type: application/json" \
#      -d '{"alias":"your-custom-domain.com"}'