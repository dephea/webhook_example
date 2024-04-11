from flask import Flask, request
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def onEvent():
    data = request.get_json()

    if "typeWebhook" in data:
        typeWebhook = data["typeWebhook"]

        if typeWebhook == 'incomingMessageReceived':
            return onIncomingMessageReceived(data)
        elif typeWebhook == 'deviceInfo':
            return onDeviceInfo(data)
        elif typeWebhook == 'incomingCall':
            return onIncomingCall(data)
        elif typeWebhook == 'incomingMessageReceived':
            return onIncomingMessageReceived(data)
        elif typeWebhook == 'outgoingAPIMessageReceived':
            return onOutgoingAPIMessageReceived(data)
        elif typeWebhook == 'outgoingMessageReceived':
            return onOutgoingMessageReceived(data)
        elif typeWebhook == 'outgoingMessageStatus':
            return onOutgoingMessageStatus(data)
        elif typeWebhook == 'stateInstanceChanged':
            return onStateInstanceChanged(data)
        elif typeWebhook == 'statusInstanceChanged':
            return onStatusInstanceChanged(data)
        else:
            #save undefined webhook somewhere and return 200
            return "", 200

    else:
        print("No 'typeWebhook' key found in the request data")
        return "No typeWebhook found", 400


def onIncomingMessageReceived(body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
              + 'At ' + str(eventDate) + ' Incoming from ' \
              + json.dumps(senderData, ensure_ascii=False) \
              + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    print(TextOut)
    return "", 200

def onIncomingCall(body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    fromWho = body['from']
    TextOut = idMessage + ': ' \
              + 'Call from ' + fromWho \
              + ' at ' + str(eventDate)
    print(TextOut)
    return "", 200


def onDeviceInfo(body: object):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    deviceData = body['deviceData']
    TextOut = 'At ' + str(eventDate) + ': ' \
              + json.dumps(deviceData, ensure_ascii=False)
    print(TextOut)
    return "", 200


def onOutgoingMessageReceived(body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
              + 'At ' + str(eventDate) + ' Outgoing from ' \
              + json.dumps(senderData, ensure_ascii=False) \
              + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    print(TextOut)
    return "", 200


def onOutgoingAPIMessageReceived(body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
              + 'At ' + str(eventDate) + ' API outgoing from ' \
              + json.dumps(senderData, ensure_ascii=False) + \
              ' message = ' + json.dumps(messageData, ensure_ascii=False)
    print(TextOut)
    return "", 200


def onOutgoingMessageStatus(body: object):
    idMessage = body['idMessage']
    status = body['status']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    TextOut = idMessage + ': ' + str(eventDate) + ' status = ' + status
    print(TextOut)
    return "", 200


def onStateInstanceChanged(body: object):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    stateInstance = body['stateInstance']
    TextOut = 'At ' + str(eventDate) + ' state instance = ' \
              + json.dumps(stateInstance, ensure_ascii=False)
    print(TextOut)
    return "", 200


def onStatusInstanceChanged(body: object):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    statusInstance = body['statusInstance']
    TextOut = 'At ' + str(eventDate) + ' status instance = ' \
              + json.dumps(statusInstance, ensure_ascii=False)
    print(TextOut)
    return "", 200


if __name__ == "__main__":
    app.run()