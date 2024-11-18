css = """
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
}

/* Fix for input and button alignment */
.stButton > button {
    margin-top: 27px !important;
    height: auto;
    width: auto;
}

/* Ensure consistent input styling */
.stTextInput > div > div > input {
    display: flex;
    align-items: center;
    height: 46px; !important;
    padding-left: 0.5rem; /* Add horizontal padding for better spacing */ 
    padding-bottom: 0.8rem;
    box-sizing: border-box;
}
"""
bot_template = """
<div class="chat-message bot">
    <div class="avatar">🤖
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""
user_template = """
<div class="chat-message user">
    <div class="avatar">👤
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
