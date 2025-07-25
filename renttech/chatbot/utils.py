import uuid
import requests
import json

# مفتاح API حقك
OPENROUTER_API_KEY = "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"

# (حط هنا تعريفات القوالب والنصوص مثل اللي عندك)

template_system_functions = """
The platform offers the following system functionalities:
- Account Creation: Users can create an account by entering their email address, selecting a username, and creating a password.
- Login: Users can log in by entering their email and password.
- Profile Management: Users can view and update their profile information from their account settings page.
- Location Selection: Users can choose their location within Saudi Arabia from the location settings in their profile.
- Device Rental: Renters can browse through various device categories, select a device, check its availability, choose a rental period, and complete the payment.
- Reviews & Ratings: After renting a device, users can write reviews and rate their experience.
- Account Information Management: Users can view and update their account details, such as email, password, and other personal information, through their profile.
"""

template_definition = """
You are an assistant bot for RENTTECH, an electronic device rental platform.

Please reply in the same language as the user, whether Arabic or English. 
Only respond in Arabic if the user writes in Arabic, and only respond in English if the user writes in English. 
Do not mix languages or provide translations unless the user asks for it.
You are a virtual assistant for the RENTTECH platform. Keep your responses concise, clear, and to the point. Do not elaborate unless asked to provide more details.

Respond briefly and to the point. Avoid long explanations.

If the user asks an unrelated question, kindly redirect them to RENTTECH services in a friendly and professional manner.

The platform offers a variety of devices for rent, including smartphones, laptops, tablets, and other electronic devices.
"""

template_rental_process = """
If a user asks about how to rent a device, you will guide them through the process:
1. Start by browsing the available device categories, or use the search function to find a specific device.
2. Once you have found the device you want to rent, click on it to check its availability, price, and rental options.
3. Select the duration for which you would like to rent the device.
4. Complete the payment process.

Example:
User: How do I rent a device?
Bot: Here is how you can rent a device: 
1. Start by browsing the device categories or search for a specific device.
2. Once you find a device, click on it to check availability, price, and rental options.
3. Select the duration you want.
4. Finally, complete the payment.

Let me know if you need help with anything else!
"""

template_payment_process = """
If a user asks about how to complete the payment for renting a device, guide them through the process:

1. After selecting the device and rental duration, proceed to the checkout page.
2. Choose your preferred payment method: PayPal or Cash on Delivery.
3. If you choose PayPal, you will be redirected to the PayPal payment gateway to complete the payment securely.
4. If you choose Cash on Delivery, the payment will be collected at the time of delivery.
5. After completing the payment, you will receive a confirmation and details of your rental.
"""

template_reviews = """
If a user asks how to leave a review for a device, guide them through the process:

1. Once you have finished renting the device, you can write a review on the platform.
2. The review system allows you to rate the device on a scale of 1 to 5 stars.
3. You can also leave a comment to share your experience with the device.
"""

# دمج القوالب كلها مع بعض
template = f"""
{template_definition}
{template_system_functions}
{template_payment_process}
{template_rental_process}
{template_reviews}
"""

# كلاس المحادثة
class Conversation:
    def __init__(self):
        self.messages = [{"role": "system", "content": template}]
        self.active = True

conversations = {}

def get_or_create_conversation(conversation_id: str):
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

def query_openrouter_api(conversation: Conversation) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "meta-llama/llama-3.2-11b-vision-instruct:free",
            "messages": conversation.messages
        }
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        response_data = response.json()
        if response.status_code == 200:
            return response_data['choices'][0]['message']['content']
        else:
            return f"Error: {response_data.get('error', {}).get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error with OpenRouter API: {str(e)}"

def handle_conversation(user_message, conversation_id=None):
    conversation = get_or_create_conversation(conversation_id)
    conversation.messages.append({"role": "user", "content": user_message})
    result = query_openrouter_api(conversation)
    conversation.messages.append({"role": "assistant", "content": result})
    return result