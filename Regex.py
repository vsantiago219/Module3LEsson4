import re
#Given email list
text = "Emails: user1@domain.com, user2@Exclude.com, user3@domain.com"

# Find all emails ending with 'exclude.com' (case-insensitive)
emails_to_exclude = re.findall(r'\b[A-Za-z0-9._%+-]+@exclude\.com\b', text, re.IGNORECASE)

# Remove any email ending with 'exclude.com'
new_text = text
for email in emails_to_exclude:
    new_text = new_text.replace(email, '')


print(new_text)