from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='82GuCE7DZfiHSiKGmAVXIfmfoFKHSd7PkF1Tjs600/qrHgI+IG7l3B76LJZ4ANvJJJ+zgNNGsKAktA/vZioZUkQd/Crt5APCKBVX5GcO647MK0RflDhDWaGEFvlYU5jTvABtWE9nBVin6RYxL+/sEgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d86fd7a88b7df1bb3dca5669163efbc9')


@app.route("/callback", methods=['POST'])
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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        msg = event.message.text
        r = '我看不懂你說什麼'

        if msg == 'hi':
            r = 'hi'
        elif msg == '你吃飯了嗎'
            r = '還沒'

        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=r)]
            )
        )

if __name__ == "__main__":
    app.run()