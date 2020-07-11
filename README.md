# Stock Circuit Notifier

This scripts gets the stock prices of the particular company and sends as a notification to telegram.

## Usage
### Creating IFTTT Service
Here we are using IFTTT applets to send notifications to telegram.
- To start with create a free account in [IFTTT](https://ifttt.com/)
- Then navigate to the [create](https://ifttt.com/create) page.
- Click on the big "This" text. Search for "WebHooks". Then click on "Receive a Web Request"
- Type an event name that will be used in the python script to trigger it.
- Click on "Create Trigger".
- Then click on "That".
- Search for "Telegram".
- You will be asked to authorise your telegram account. Once done, select "Send Message".
- Type in the message you want to send and finish the creation. For ex: Current {{Value1}} price is {{Value 2}}
- Here value1 and value2 can be anything that you send from python script. For ex: Company Name and Price.
- To get your user key, go to this [Link](https://ifttt.com/maker_webhooks) and select documentation.
- The URL will be something like this: https://maker.ifttt.com/trigger/{event}/with/key/{yourKey}
- This will be used to send the notifications by giving the appropriate event name and key.

### Getting API key from [AplhaVantage](https://www.alphavantage.co/)

- Create a free account in this website.
- Use the appropriate API based on you requirement with the help of the [documentation](https://www.alphavantage.co/documentation/)

