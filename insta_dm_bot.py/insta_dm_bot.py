def generate_dm_replies(niche, product):
    replies = {
        "price": [
            f"Hey! Thanks for your interest in {product} 😊 The price is $XX. Want the link?",
            f"Hi there! {product} is currently on sale. DM me 'PRICE' for details.",
            f"Hello! Our {product} starts at $XX. Shall I send you the catalog?"
        ],
        "order": [
            f"Awesome! To order {product}, please share your email and city. I'll send the invoice.",
            f"Great choice! DM me your WhatsApp number and I'll place the order for {product}.",
            f"Perfect! Just send 'ORDER {product}' and your details."
        ],
        "faq": [
            f"Yes, we ship {product} worldwide 🌍 Delivery in 3-5 days.",
            f"{product} has a 30-day return policy. 100% guaranteed.",
            f"We accept PayPal, Card, and COD for {product}."
        ]
    }
    
    print("="*50)
    print(f" INSTAGRAM DM REPLY SCRIPTS FOR: {product}")
    print("="*50)
    
    print("\n[1] PRICE INQUIRY REPLIES:")
    for r in replies["price"]: print(f"- {r}")
    
    print("\n[2] ORDER REPLIES:")
    for r in replies["order"]: print(f"- {r}")
    
    print("\n[3] FAQ REPLIES:")
    for r in replies["faq"]: print(f"- {r}")
    
    filename = f"{niche}_DM_Scripts.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for cat, msgs in replies.items():
            f.write(f"--- {cat.upper()} ---\n")
            for msg in msgs: f.write(msg + "\n\n")
    print(f"\n✅ Saved to: {filename}")

if __name__ == "__main__":
    print(" INSTAGRAM DM SCRIPT GENERATOR BOT ")
    niche = input("Enter Niche [fashion, skincare, gym, etc]: ")
    product = input("Enter Product Name: ")
    generate_dm_replies(niche, product)