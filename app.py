from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('j8Fj6mTrcGeDwdNiys9a1FeN+E2GVIdl11YcybRqxl78gXKN36JDt8w8P3Y4WzpwoMzt86a0zAuiOyi+Q0fLjizf8Ey+ZAjft1Beh2hm6h3L4yX/f/6QSY3JRnfEKI/PwpckLWIKOvI1URV6cvfiAQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('64a670f0b7384b02b6dcb3ba1acbcd74')


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()