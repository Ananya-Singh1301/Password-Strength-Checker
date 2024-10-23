import re
def check_password_strength(password):
    #Initialize the strength score & feedback messages
    strength_score = 0
    feedback = []
    
    if not password.strip():
        return "Invalid", ["Password cannot be empty. Please provide a valid password."]
    
    length_criteria = len(password) >=8
    lowercase_criteria = re.search(r'[a-z]',password) is not None
    uppercase_criteria = re.search(r'[A-Z]',password) is not None
    number_criteria = re.search(r'[0-9]',password) is not None
    special_char_criteria = re.search(r'[!@#$%^*(),.?":{}|<>+=_]',password) is not None
    
    #Assessing the strength of the password
    if length_criteria:
        strength_score +=1
    else:
        feedback.append("Your password be at least 8 characters long.")
        
    if lowercase_criteria:
        strength_score +=1
    else:
        feedback.append("Your password should contain at least one lowercase letter.")
        
    if uppercase_criteria:
        strength_score +=1
    else:
        feedback.append("Your password should contain at least one uppercase letter.")
        
    if number_criteria:
        strength_score +=1
    else:
        feedback.append("Your password should contain at least one number.")
        
    if special_char_criteria:
        strength_score +=1
    else:
        feedback.append("Your password should contain at least one special character.")
        
    #Feedback on password strength
    if strength_score == 5:
        strength_level = "Very Strong"
        feedback.append("Great Job! Your password is very strong.")
    elif strength_score == 4:
        strength_level = "strong"
        feedback.append("Your password is strong, but consider adding more variety.")
    elif strength_score == 3:
        strength_level = "Moderate"
        feedback.append("Your password is moderate. Consider using a longer password with a mixture of characters.")
    else:
        strength_level = "Weak" 
        feedback.append("Your password is weak. Consider using a strong password.")
             
    return strength_level, feedback

#Main function to interact with user
def main():
    print("Welcome to The Password Strength Checker!")
    user_password = input("Enter your password:")
    
    strength_level, feedback = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {strength_level}")
    print("feedback")
    for suggestion in feedback:
        print(f"- {suggestion}")
        
if  __name__ == "__main__":
    main()