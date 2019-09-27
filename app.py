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
    if event.message.text == "안녕":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="안녕하세요!"))
    elif "재희" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="같이 놀아요!"))
    elif "예쁘다" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="꺄 고마워요!"))
    elif "뭐먹을까" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="재희님 먹고싶은거요!"))
    if event.message.text == "잘 지냈어":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="응 보고싶었어!"))
    if event.message.text == "사랑해":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="내가 더 많이 사랑해"))
    if event.message.text == "잘잤어":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="응 잘잤어, 너는?"))
if __name__ == '__main__':
    app.run()