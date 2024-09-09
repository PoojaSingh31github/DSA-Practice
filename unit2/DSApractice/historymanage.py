import streamlit as st

class BrowserHistory:
    def __init__(self):
        self.back_stack = []  # Stack to hold the back history
        self.forward_stack = []  # Stack to hold the forward history
        self.current_page = None  # Current page the user is on

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)  # Push current page to back stack
        self.current_page = url  # Update current page
        self.forward_stack.clear()  # Clear forward stack as new page is visited
        print(f"Visited: {self.current_page}")

    def back(self):
        if not self.back_stack:
            print("No back history.")
            return
        self.forward_stack.append(self.current_page)  # Push current page to forward stack
        self.current_page = self.back_stack.pop()  # Pop from back stack to current
        print(f"Back to: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("No forward history.")
            return
        self.back_stack.append(self.current_page)  # Push current page to back stack
        self.current_page = self.forward_stack.pop()  # Pop from forward stack to current
        print(f"Forward to: {self.current_page}")

    def current(self):
        if self.current_page:
            print(f"Current page: {self.current_page}")
        else:
            print("No page currently visited.")


# Initialize browser history object
history = BrowserHistory()

# Streamlit UI components
st.title("Simple Browser History Navigation")

# Input for visiting a new URL
new_url = st.text_input("Enter a URL to visit:")

if st.button("Visit"):
    if new_url:
        current_page = history.visit(new_url)
        st.success(f"Visited: {current_page}")
    else:
        st.warning("Please enter a valid URL.")

# Back button
if st.button("Back"):
    current_page = history.back()
    st.info(f"Back to: {current_page}")

# Forward button
if st.button("Forward"):
    current_page = history.forward()
    st.info(f"Forward to: {current_page}")

# Display current page
current_page = history.current()
st.write(f"**Current Page:** {current_page}")

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("github.com")
browser.visit("stackoverflow.com")
browser.back()  # Go back to github.com
browser.back()  # Go back to google.com
browser.forward()  # Forward to github.com
browser.current()  # Display current page
