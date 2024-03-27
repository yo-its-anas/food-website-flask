import stripe

stripe_public_key = 'your public key'
stripe_secret_key = 'your secret key'

stripe.api_key = stripe_secret_key

lineItems = []  # Define lineItems list globally

def handle_checkout(cart_items):
    global lineItems  # Access the global lineItems list
    
    # Clear lineItems list before adding new items
    lineItems.clear()
    
    # Loop through each cart item and add it to lineItems
    for item in cart_items:
        lineItems.append({
            'price': item['stripeUrl'],  # Assuming 'stripeUrl' contains the Stripe price ID
            'quantity': item['quantity']
        })
    
    # Print the updated lineItems list (optional)
    print("Updated lineItems:", lineItems)

def create_checkout_session():
    global lineItems  # Access the global lineItems list

    if not lineItems:
        raise ValueError("No line items found. Please ensure cart items are added.")

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=lineItems,
        mode='payment',
        success_url='http://localhost:5000/thanks?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://localhost:5000/',
    )
    return session
