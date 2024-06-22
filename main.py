def is_spam(sms):
    keywords = ["sale", "offer", "amazing deal", "discount"]
    
    for keyword in keywords:
        if keyword in sms:
            return True
    
    return False

def main():
    user_input = input("Type a message: ")
    
    if is_spam(user_input):
        print("SPAM detected!")
    else:
        print("Not spam.")
    
if __name__ == "__main__":
    main()