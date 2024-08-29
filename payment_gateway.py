def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"])*100
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount" : amount,
            "currency": "INR",
            "receipt": "order reciept",
            "notes": {"email":"user_email@example.com",},

        }
        order = client.order.create(data=payment_data)

        context =  {
            "key": settings.RAZORPAY_API_KEY,
            "amount": order["amount"],
            "currency": order["currency"],
            "name": "Your Company Name",
            "description": "Payment for your Product",

            
            "order_id": order["id"],    

        }
